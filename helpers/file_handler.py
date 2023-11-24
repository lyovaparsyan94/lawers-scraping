from os.path import join, exists
import yaml
import pandas as pd
import json
from openpyxl import load_workbook
from configs.constants import SERP_DATA_PATH


def load_config(file):
    with open(file) as stream:
        config = yaml.safe_load(stream=stream)
    return config


def load_xlsx(file):
    return pd.read_excel(file, usecols=['lawyer_name', 'undergrad school'])


def write_to_xlsx(data_to_write):
    if not exists('lawyers_phone_emails_file.xlsx'):
        df = pd.DataFrame(data_to_write)
        df = df.T
        df['lawyer_name'] = df.index
        df['email'] = df['email'].apply(', '.join)
        df['phone'] = df['phone'].apply(', '.join)
        df += df[['lawyer_name', 'email', 'phone']]
    else:
        df = pd.read_excel('lawyers_phone_emails_file.xlsx')
        name = list(data_to_write.keys())[0]
        data = [
            [name, ', '.join(data_to_write[name]['phone']), ', '.join(data_to_write[name]['email'])],
        ]
        df1 = pd.DataFrame(data, columns=['lawyer_name', 'email', 'phone'])
        df = pd.concat([df, df1], ignore_index=True)
    df.to_excel('lawyers_phone_emails_file.xlsx', index=False)


def write_serp_json(filename, data):
    with open(join(SERP_DATA_PATH, f'{filename}.json'), 'w') as f:
        json.dump(data, f)


def check_existence(filename):
    return exists(join(SERP_DATA_PATH, f'{filename}.json'))


def load_json(filename):
    with open(join(SERP_DATA_PATH, f'{filename}.json')) as f:
        data = json.load(f)
    return data
