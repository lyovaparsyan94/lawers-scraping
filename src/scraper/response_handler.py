class Response_handler:
    data = {}


    def __init__(self):
        self.clean_data = {}

    def collect(self, person, response):
        self.person = person
        self.clean_data = {self.person: {'email': [], 'phones': []}}
        emails = self.find_emails(response)
        phone_numbers = self.find_phone_numbers(response)

        if self.clean_data.keys() == Response_handler.data.keys():
            self.clean_data[person]['email'].extend(emails)
            self.clean_data[person]['phones'].extend(phone_numbers)
            Response_handler.data = Response_handler.data | self.clean_data
        else:
            Response_handler.data = Response_handler.data | self.clean_data


    def find_phone_numbers(self, response):
        phone_start_marker = "phone_numbers = ["
        end_marker = "]"
        phone_start_index = response.find(phone_start_marker) + len(phone_start_marker)
        phone_end_index = response.find(end_marker, phone_start_index)
        extracted_phones = response[phone_start_index:phone_end_index]
        spltited_phones = extracted_phones.split(' , ')
        phone_list = list(set(spltited_phones))
        return phone_list

    def find_emails(self, response):
        email_start_marker = "email_addresses = ["
        end_marker = "]"
        phone_start_index = response.find(email_start_marker) + len(email_start_marker)
        phone_end_index = response.find(end_marker, phone_start_index)
        extracted_emails = response[phone_start_index:phone_end_index]
        spltited_emails = extracted_emails.split(' , ')
        emails_list = list(set(spltited_emails))
        return emails_list


worker = Response_handler()
worker.collect('Ashot', """[1]: https://bulletin.gwu.edu/ ""
[2]: https://www.gwu.edu/faculty-staff ""
[3]: https://bulletin.gwu.edu/faculty/ ""

I searched the link you provided and found the following information for lawyer Ari E Craig:

phone_numbers = [202-994-7000, 202-994-7004, 202-994-700077]
email_addresses = [aecraig@gwu.edu]

I hope this helps. 😊""")
worker1 = Response_handler()
worker.collect('Ashot', """[1]: https://bulletin.gwu.edu/ ""
[2]: https://www.gwu.edu/faculty-staff ""
[3]: https://bulletin.gwu.edu/faculty/ ""

I searched the link you provided and found the following information for lawyer Ari E Craig:

phone_numbers = [1202-994-7000, 1202-994-7004, 1202-994-700077]
email_addresses = [aecraig@gwu.edu]

I hope this helps. 😊""")

# x = {'Ashot': {'email': [1]}}
# y = {'Ashot1': {'email': [2]}}
# z = x | y
# print(z)
print(Response_handler.data)