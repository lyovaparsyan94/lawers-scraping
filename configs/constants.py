import os
from os.path import abspath, dirname, join

ROOT_DIR = os.getcwd()
CONFIGS_DIR = abspath(dirname(__file__))
CONFIG_FILE_PATH = join(CONFIGS_DIR, 'config.yaml')
LOGGING_CONFIG_PATH = join(CONFIGS_DIR, 'logger.yaml')

# SERP API
CERT_PATH = join(CONFIGS_DIR, 'ca.crt')
XLSX_FILE_PATH = join(ROOT_DIR, join('data', 'result_filtered_alphabetically.xlsx'))

SERP_DATA_PATH = join(ROOT_DIR, 'serp_data')