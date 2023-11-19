from configs.constants import CONFIG_FILE_PATH
from helpers.file_handler import load_config
from src.manager import Manager

config = load_config(file=CONFIG_FILE_PATH)


def run():
    manager = Manager(config=config)
    manager.start()


if __name__ == '__main__':
    run()
