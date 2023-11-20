answer1 = """
[1]: https://www.gwu.edu/faculty-staff ""
[2]: https://bulletin.gwu.edu/ ""
[3]: https://bulletin.gwu.edu/faculty/ ""

I searched the link you provided and found the following information about lawyer Ari E Craig:

phone_numbers = [202-994-2160]
email_addresses = [aecraig@gwu.edu]

These are the personal contact details of Ari E Craig, who is an Associate Professor of Law at The George Washington University[^1^][3]. I hope this helps. 😊
"""
phone_regex = r"\w\d \w\w \w\w \w\w \w\d|(?<=[^\d][^_][^_] )[^_]\d[^ ]\d[^ ][^ ]+|(?<= [^<]\w\w \w\w[^:]\w[^_][^ ][^,][^_] )(?: *[^<]\d+)+"
