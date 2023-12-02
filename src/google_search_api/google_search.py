import requests
from requests.exceptions import ProxyError
from time import sleep
from test import x

from configs.constants import CERT_PATH


class GoogleSearch:

    def __init__(self, config):
        self.base_url = config['url']
        self.proxies = {
            'http': config['http_proxy'],
            'https': config['https_proxy']
        }

    def process(self, person, university, retry=5, interval=5):
        response = None
        while not response and retry >= 1:
            try:
                query = self.create_query(person=person, university=university)
                return self.search(query=query)
            except ProxyError as e:
                print(e)
                retry -= 1
                sleep(interval)
                print(f"Retrying after PRoxyError {5 - retry} time")
            except Exception:
                retry -= 1
                sleep(interval)
                print(f"Retrying after PRoxyError {5 - retry} time")

    def search(self, query):
        url = f'{self.base_url}{query}'
        return requests.get(url=url, proxies=self.proxies, verify=CERT_PATH)

    @staticmethod
    def create_query(person, university):
        return f'q={person} {university} contact info&brd_json=1'
