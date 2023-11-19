import requests
from pprint import pprint
from configs.constants import CERT_PATH

proxies = {
    'http': 'http://brd-customer-hl_23bd325f-zone-serp:834ucdyvfehn@brd.superproxy.io:22225',
    'https': 'http://brd-customer-hl_23bd325f-zone-serp:834ucdyvfehn@brd.superproxy.io:22225'
}
response = requests.get('https://www.google.com/search?q=pizza&brd_json=1', proxies=proxies, verify=CERT_PATH)
pprint(response.json())

