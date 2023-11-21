class Response_handler:
    all_data = {}

    def __init__(self):
        self.clean_data = {}
        self.end_marker = "]"
        self.phone_start_marker = "phone_numbers = ["
        self.email_start_marker = "email_addresses = ["

    def collect_data(self, person, response):
        emails = self.extract_data(response, start_marker=self.email_start_marker)
        phone_numbers = self.extract_data(response, start_marker=self.phone_start_marker)
        data = {person: {'emails': emails, 'phone': phone_numbers}}
        if Response_handler.all_data.get(person) is None:
            Response_handler.all_data = Response_handler.all_data | data
        else:
            Response_handler.all_data[person]['emails'].extend(emails)
            Response_handler.all_data[person]['phone'].extend(phone_numbers)

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
