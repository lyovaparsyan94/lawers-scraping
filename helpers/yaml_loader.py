import os
from os.path import abspath, dirname, join

ROOT_DIR = os.getcwd()
CONFIGS_DIR = abspath(dirname(__file__))
CONFIG_FILE_PATH = join(CONFIGS_DIR, 'config.yaml')
LOGGING_CONFIG_PATH = join(CONFIGS_DIR, 'logger.yaml')