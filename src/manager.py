from configs.constants import XLSX_FILE_PATH
from helpers.file_handler import load_xlsx

from src.google_search_api.google_search import GoogleSearch
from src.chat_gpt.gpt_4 import ChatGPT


class Manager:

    def __init__(self, config):
        self.config = config
        self.search_api = GoogleSearch(config['serp'])
        self.chat_gpt = ChatGPT()

    def start(self):
        df = load_xlsx(file=XLSX_FILE_PATH)
        for index, row in df.iterrows():
            person, university = row[0], row[1]
            response = self.search_api.process(person=person, university=university)
            for info in response['organic']:
                if 'linkedin' not in info['link']:
                    content = f"I need lawyer {person} phone number and email address from this link {info['link']}," \
                              f"if it's provided there. Provide information in this format: \n====\n " \
                              f"phone_numbers = [list of founded phone numbers]\n" \
                              f"email_addresses = [list of founded email addresses]\n====\n (==== symbols required)" \
                              f"phone_numbers and email_addresses should be provided in python list format." \
                              f"I don't need any general number of {university}, please do not provide urls, provide " \
                              f"only personal information." \
                              f"Please provide a short response less than 300 letters / symbols"
                    result = self.chat_gpt.run(content=content)
                    # TODO scrape result, save into list, after collecting all results, needed compare are results
                    #  and get duplicated emails and phone numbers

