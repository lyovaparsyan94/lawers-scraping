class DataCollector:
    all_data = {}

    def __init__(self):
        self.clean_data = {}
        self.end_marker = "]"
        self.phone_start_marker = "phone_numbers = ["
        self.email_start_marker = "email_addresses = ["

    def collect_data(self, person, data):
        emails = self.extract_data(data, start_marker=self.email_start_marker)
        phone_numbers = self.extract_data(data, start_marker=self.phone_start_marker)
        data = {person: {'emails': emails, 'phone': phone_numbers}}
        if DataCollector.all_data.get(person) is None:
            DataCollector.all_data = DataCollector.all_data | data
        else:
            DataCollector.all_data[person]['emails'].extend(emails)
            DataCollector.all_data[person]['phone'].extend(phone_numbers)

    def extract_data(self, data, start_marker):
        start_marker = start_marker
        start_index = data.find(start_marker) + len(start_marker)
        end_index = data.find(self.end_marker, start_index)
        extracted_info = data[start_index:end_index]
        info_to_list = extracted_info.split(',')
        for index, element in enumerate(info_to_list):
            info_to_list[index] = element.strip(' ')
        cleaned_list = list(set(info_to_list))
        return cleaned_list
