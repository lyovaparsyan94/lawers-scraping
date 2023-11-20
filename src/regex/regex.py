import re


class RegAnalyze:
    def __init__(self):
        self.email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        self.phone_regex = r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+"

    def filter_phones(self, text):
        phone_list = ''
        phone_numbers = re.findall(self.phone_regex, text)
        if all(phone_numbers) and any(phone_numbers):
            phone_numbers = re.findall(self.phone_regex, text)


# my_list = ['1', '']
# if all(my_list) and any(my_list):
#     print("The list contains only non-empty elements.")
# else:
#     print("The list contains empty elements.")

answer1 = """

phone_numbers = [202-994-21668]
email_addresses = [aecraig@gwu.edu]

====
phone_numbers = '(202) 994-2167'
email_addresses = [aecraig@law.gwu.edu]
====

I hope this helps you. 
I searched the link you provided and found the following information about lawyer Ari E Craig:

phone_numbers = '(202) 994-2167'
email_addresses = 'aecraig@gwu.edu'

These are the personal contact details of Ari E Craig, who is an Associate Professor of Law at The George Washington University[^1^][3]. I hope this helps.

"""

phone_start_marker = "phone_numbers = ["
end_marker = "]"

phone_start_index = answer1.find(phone_start_marker) + len(phone_start_marker)
phone_end_index = answer1.find(end_marker, phone_start_index)

extracted_content = answer1[phone_start_index:phone_end_index]

print(extracted_content)

phone_start_marker = "phone_numbers = ["
end_marker = "]"

phone_start_index = answer1.find(phone_start_marker) + len(phone_start_marker)
phone_end_index = answer1.find(end_marker, phone_start_index)

extracted_content = answer1[phone_start_index:phone_end_index]

print(extracted_content)
