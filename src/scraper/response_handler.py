from pprint import pprint


class Response_handler:
    all_data = {}
    counter = 0

    def __init__(self):
        self.clean_data = {}
        self.end_marker = "]"
        self.phone_start_marker = "phone_numbers = ["
        self.email_start_marker = "email_addresses = ["

    def collect(self, person, response):
        # emails = self.find_emails(response)
        # phone_numbers = self.find_phone_numbers(response)
        emails = self.extract_data(response, start_marker=self.email_start_marker)
        phone_numbers = self.extract_data(response, start_marker=self.phone_start_marker)
        # print(emails)
        # print(phone_numbers)
        data = {person: {'emails': emails, 'phone': phone_numbers}}
        if Response_handler.all_data.get(person) is None:
            Response_handler.all_data = Response_handler.all_data | data
        else:
            Response_handler.all_data[person]['emails'].extend(emails)
            Response_handler.all_data[person]['phone'].extend(phone_numbers)
        # print(Response_handler.all_data)

    def find_phone_numbers(self, response):
        phone_start_marker = "phone_numbers = ["
        end_marker = "]"
        start_index = response.find(phone_start_marker) + len(phone_start_marker)
        phone_end_index = response.find(self.end_marker, start_index)
        extracted_phones = response[start_index:phone_end_index]
        spltited_phones = extracted_phones.split(',')
        for index, element in enumerate(spltited_phones):
            spltited_phones[index] = element.strip(' ')
        phone_list = list(set(spltited_phones))
        return phone_list

    def find_emails(self, response):
        email_start_marker = "email_addresses = ["
        end_marker = "]"
        start_index = response.find(email_start_marker) + len(email_start_marker)
        phone_end_index = response.find(end_marker, start_index)
        extracted_emails = response[start_index:phone_end_index]
        spltited_emails = extracted_emails.split(',')
        for index, element in enumerate(spltited_emails):
            spltited_emails[index] = element.strip(' ')
        emails_list = list(set(spltited_emails))
        return emails_list

    def extract_data(self, response, start_marker):
        start_marker = start_marker
        start_index = response.find(start_marker) + len(start_marker)
        end_index = response.find(self.end_marker, start_index)
        extracted_info = response[start_index:end_index]
        info_to_list = extracted_info.split(',')
        for index, element in enumerate(info_to_list):
            info_to_list[index] = element.strip(' ')
        cleaned_list = list(set(info_to_list))
        return cleaned_list


worker = Response_handler()
worker.collect('Ashot', """[1]: https://bulletin.gwu.edu/ ""
[2]: https://www.gwu.edu/faculty-staff ""
[3]: https://bulletin.gwu.edu/faculty/ ""

I searched the link you provided and found the following information for lawyer Ari E Craig:

phone_numbers = [202-994-7000, 202-994-7004, 202-994-700077, 202-994-7000, 202-994-7000]
email_addresses = [aecraig@gwu.edu, aecraig@gwu.edu]

I hope this helps. 😊""")
worker1 = Response_handler()
worker1.collect('Ashot', """[1]: https://bulletin.gwu.edu/ ""
[2]: https://www.gwu.edu/faculty-staff ""
[3]: https://bulletin.gwu.edu/faculty/ ""

I searched the link you provided and found the following information for lawyer Ari E Craig:

phone_numbers = [1202-994-7000, 1202-994-7004, 1202-994-700077, 1202-994-7000, 1202-994-7000]
email_addresses = [aecraig@gwu.edu, aecraig@gwu.edu]

I hope this helps. 😊""")
worker2 = Response_handler()
worker2.collect('Armen', """[1]: https://bulletin.gwu.edu/ ""
[2]: https://www.gwu.edu/faculty-staff ""
[3]: https://bulletin.gwu.edu/faculty/ ""

I searched the link you provided and found the following information for lawyer Ari E Craig:

phone_numbers = [1202-994-7000, 1202-994-7004, 1202-994-700077, 1202-994-7000, 1202-994-7000]
email_addresses = [aecraig@gwu.edu, aecraig@gwu.edu]

I hope this helps. 😊""")
pprint(Response_handler.all_data)