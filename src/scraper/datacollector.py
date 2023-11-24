import re

from src.chat_gpt.fake_reponses import list_of_answers
from random import choice


class DataCollector:
    ALL_DATA = {}

    def __init__(self):
        self.clean_data = {}
        self.end_marker = "]"
        self.phone_start_marker = "phone_numbers = ["
        self.email_start_marker = "email_addresses = ["
        self.email_regex = [r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"]
        self.phone_regex = ["/^(\+)?[0-9][0-9]{7,14}$/"]
        # # self.phone_regex = [
        #     r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+",
        #     r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))"]

    def collect_data(self, person, data):
        emails = self.extract_data(data, start_marker=self.email_start_marker)
        emails = self.regex_check(data=emails, patterns=self.email_regex)
        phone_numbers = self.extract_data(data, start_marker=self.phone_start_marker)
        # phone_numbers = self.regex_check(data=phone_numbers, patterns=self.phone_regex)
        data = {person: {'email': set(emails), 'phone': set(phone_numbers)}}
        # if DataCollector.all_data.get(person) is None:
        #     DataCollector.all_data = DataCollector.all_data | data
        # else:
        #     DataCollector.all_data[person]['email'].extend(emails)
        #     DataCollector.all_data[person]['phone'].extend(phone_numbers)
        #     DataCollector.all_data[person]['email'] = list(set(DataCollector.all_data[person]['email']))
        #     DataCollector.all_data[person]['phone'] = list(set(DataCollector.all_data[person]['phone']))
        return data

    def extract_data(self, data, start_marker):
        cleaned_list = []
        if data:
            start_marker = start_marker
            start_index = data.find(start_marker)
            if start_index != -1:
                start_index = start_index + len(start_marker)
                end_index = data.find(self.end_marker, start_index)
                extracted_info = data[start_index:end_index]
                info = extracted_info.split(',')
                for index, element in enumerate(info):
                    cleaned_list.append(element.strip(' '))
            cleaned_list = list(set(cleaned_list))
        return cleaned_list

    def regex_check(self, data, patterns):
        if type(data) == list:
            data = ' '.join(data)
        result = []
        for pattern in patterns:
            tmp_res = re.findall(pattern, data)
            result += tmp_res
        result = list(set(result))
        return result
