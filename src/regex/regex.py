import re


class RegAnalyze:
    def __init__(self):
        self.email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        self.phone_regex = r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+"

    def filter_phones(self, text):
        phone_list = ''
        phone_numbers = re.findall(self.phone_regex, text)
        if all(phone_numbers) and any(phone_numbers):
            ...


my_list = ['1', '']
if all(my_list) and any(my_list):
    print("The list contains only non-empty elements.")
else:
    print("The list contains empty elements.")
