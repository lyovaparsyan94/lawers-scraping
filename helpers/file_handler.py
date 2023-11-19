import yaml
import pandas as pd


def load_config(file):
    with open(file) as stream:
        config = yaml.safe_load(stream=stream)
    return config


def load_xlsx(file):
    return pd.read_excel(file, usecols=['lawyer_name', 'undergrad school'])
