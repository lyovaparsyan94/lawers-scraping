import requests
from pprint import pprint

proxies = {
    'http': 'http://brd-customer-hl_23bd325f-zone-serp:834ucdyvfehn@brd.superproxy.io:22225',
    'https': 'http://brd-customer-hl_23bd325f-zone-serp:834ucdyvfehn@brd.superproxy.io:22225'
}
# TODO need improve certificat path, to get it from env
response = requests.get('https://www.google.com/search?q=pizza&brd_json=1', proxies=proxies, verify=r"C:\Users\1\Downloads\ca.crt")
pprint(response.json())

