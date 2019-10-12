import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-12s|process:%(process)-5s|thread:%(thread)-5s|funcName:%(funcName)s|message:%(message)s",
    handlers=[
        # logging.FileHandler('fileName.log'),
        logging.StreamHandler()
    ])


def export_settings():
    logging.info('Export settings VSCode started...')
    appdata_folder = os.getenv('APPDATA')
    logging.debug(f'appdata_folder = {appdata_folder}')
    os.system(
        f'COPY {appdata_folder}\\Code\\User\\settings.json settings.json')
    os.system(
        f'COPY {appdata_folder}\\Code\\User\\snippets\\python.json python.json')
    os.system(
        f'COPY {appdata_folder}\\Code\\User\\snippets\\typescript.json typescript.json')
    logging.info('Export settings VSCode completed')


def export_plugin_list():
    logging.info('Export plugin list VSCode started...')
    os.system(f'code --list-extensions > plugin-list.txt')
    logging.info('Export plugin list VSCode completed')


if __name__ == "__main__":
    logging.info('Export settings for VSCode started...')
    export_settings()
    export_plugin_list()
    logging.info('Export settings for VSCode completed')
    logging.info('GoodLuck and HaveFun for using python with VSCode ;-)')
