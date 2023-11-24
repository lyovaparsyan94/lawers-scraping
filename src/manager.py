from configs.constants import XLSX_FILE_PATH
from helpers.file_handler import load_xlsx, write_to_xlsx, write_serp_json, check_existence, load_json
from src.scraper.datacollector import DataCollector
from src.google_search_api.google_search import GoogleSearch
from src.chat_gpt.gpt_4 import ChatGPT
from src.chat_gpt.fake_reponses import list_of_answers
from random import choice


class Manager:

    def __init__(self, config):
        self.config = config
        self.search_api = GoogleSearch(config['serp'])
        self.chat_gpt = ChatGPT()
        self.data_collector = DataCollector()

    def start(self):
        df = load_xlsx(file=XLSX_FILE_PATH)
        for index, row in df.iterrows():
            person, university = row[0], row[1]
            filename = f'{person.replace(" ", "_")}'
            if check_existence(filename=filename):
                json_response = load_json(filename=filename)
            else:
                response = self.search_api.process(person=person, university=university)
                json_response = response.json()
                write_serp_json(filename=filename, data=json_response)
            person_info = {}
            if json_response.get('organic') is not None:
                for info in json_response['organic']:

                    if person not in person_info:
                        person_info[person] = {
                            "phone": set(),
                            "email": set()
                        }
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
                        # result = choice(list_of_answers)

                        data = self.data_collector.collect_data(person=person, data=result)
                        person_info[person]['phone'].update(data[person]['phone'])
                        person_info[person]['email'].update(data[person]['email'])
                print(f"Write {person} info into xlsx\n{person_info}")
                write_to_xlsx(data_to_write=person_info)
