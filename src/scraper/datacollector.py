import re

from src.chat_gpt.fake_reponses import list_of_answers
from random import choice


class DataCollector:
    all_data = {}

    def __init__(self):
        self.clean_data = {}
        self.end_marker = "]"
        self.phone_start_marker = "phone_numbers = ["
        self.email_start_marker = "email_addresses = ["
        # self.email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        # self.phone_regex = r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+"
        # self.regex_retry = r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))"
        self.email_regex = [r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"]
        self.phone_regex = [r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+",
                            r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))"]

    def collect_data(self, person, data):
        emails = self.extract_data(data, start_marker=self.email_start_marker, regex_marker=self.email_regex)
        phone_numbers = self.extract_data(data, start_marker=self.phone_start_marker, regex_marker=self.phone_regex)
        data = {person: {'emails': emails, 'phone': phone_numbers}}
        if DataCollector.all_data.get(person) is None:
            DataCollector.all_data = DataCollector.all_data | data
        else:
            DataCollector.all_data[person]['emails'].extend(emails)
            DataCollector.all_data[person]['phone'].extend(phone_numbers)

    def extract_data(self, data, start_marker, regex_marker):
        start_marker = start_marker
        start_index = data.find(start_marker) + len(start_marker)
        end_index = data.find(self.end_marker, start_index)
        extracted_info = data[start_index:end_index]
        # extracted_regex_list = re.findall(regex_marker, extracted_info)
        info_to_list = extracted_info.split(',')
        for index, element in enumerate(info_to_list):
            info_to_list[index] = element.strip(' ')
        cleaned_list = list(set(info_to_list))
        # cleaned_list = list(set(extracted_regex_list))
        return cleaned_list


# worker = DataCollector()
# for i in range(10):
#     data = choice(list_of_answers)
#     worker.collect_data(data=data, person='Armen')
#
# print(worker.all_data)
q = r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+"
r = r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))"
data = ["'(202) 994-1000'", "'(202) 994-1000'", '', 'daris.com/p/Elizabeth/Craig/ ""\n[2', '', 'daris.com/p/Elizabeth/Craig/ ""\n[2', '202-994-7470', "'(202) 994-1000'", '', '202-994-2160']
phone_regex = [q, r]
data1 = ' '.join(data)
x = re.findall(q, data1)


def regex_check(data, patterns):
    result = []
    for pattern in patterns:
        tmp_res = re.findall(pattern, data)
        result += tmp_res
    result = list(set(result))
    return result

regex_check(data=data1, patterns=phone_regex)

