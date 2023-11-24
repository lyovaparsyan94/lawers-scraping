import requests
from test import x

from configs.constants import CERT_PATH


class GoogleSearch:

    def __init__(self, config):
        self.base_url = config['url']
        self.proxies = {
            'http': config['http_proxy'],
            'https': config['https_proxy']
        }

    def process(self, person, university):
        query = self.create_query(person=person, university=university)
        return self.search(query=query)

    def search(self, query):
        url = f'{self.base_url}{query}'
        return requests.get(url=url, proxies=self.proxies, verify=CERT_PATH)

    @staticmethod
    def create_query(person, university):
        return f'q={person} {university} contact info&brd_json=1'
