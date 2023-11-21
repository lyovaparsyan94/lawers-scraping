import re

email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
phone_regex = r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+"
# answer1 = """
#
# phone_numbers = [202-994-21668]
# email_addresses = [aecraig@gwu.edu]
#
# ====
# phone_numbers = '(202) 994-2167'
# email_addresses = [aecraig@law.gwu.edu]
# ====
#
# I hope this helps you.
# I searched the link you provided and found the following information about lawyer Ari E Craig:
#
# phone_numbers = '(202) 994-2167'
# email_addresses = 'aecraig@gwu.edu'
#
# These are the personal contact details of Ari E Craig, who is an Associate Professor of Law at The George Washington University[^1^][3]. I hope this helps.
#
# """
emails = ['', 'aecraig@gwu.edu', "'aecraig@law.gwu.edu'", 'ris.com/p/Elizabeth/Craig/ ""\n[2', '', "'aecraig@law.gwu.edu'", 'aecraig@law.gwu.edu', '', 'aecraig@gwu.edu', '']
em = ' '.join(emails)
print(re.findall(email_regex, em))
# print(re.findall(phone_regex, answer1))