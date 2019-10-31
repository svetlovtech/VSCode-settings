import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)-12s|process:%(process)-5s|thread:%(thread)-5s|funcName:%(funcName)s|message:%(message)s",
    handlers=[
        # logging.FileHandler('fileName.log'),
        logging.StreamHandler()
    ])


def install_plugins():
    logging.info('Install plugins for VSCode started...')
    with open('plugin-list.txt', mode='r', encoding='UTF-8') as plugin_file:
        plugin_list = [x.replace("\n", "") for x in plugin_file.readlines()]
        installed_plugin_list = os.popen(
            'code --list-extensions').read().split('\n')
        for plugin_number, plugin_name in enumerate(plugin_list):
            if plugin_name in installed_plugin_list:
                logging.info(f'{plugin_name} is already installed')
                continue
            logging.info(
                f'Installing {plugin_number + 1} of {len(plugin_list)} plugins...')
            logging.debug(f'plugin_name = {plugin_name}')
            code_line = 'code --install-extension ' + plugin_name.replace("\\n", "")
            logging.debug(f'code_line = {code_line}')
            os.system(code_line)
    logging.info('Install plugins for VSCode completed')


def copy_files():
    logging.info('Copy files started...')
    appdata_folder = os.getenv('APPDATA')
    logging.debug(f'appdata_folder = {appdata_folder}')
    os.system(
        f'COPY settings.json {appdata_folder}\\Code\\User\\settings.json')
    os.system(
        f'COPY python.json {appdata_folder}\\Code\\User\\snippets\\python.json')
    os.system(
        f'COPY typescript.json {appdata_folder}\\Code\\User\\snippets\\typescript.json')
    logging.info('Copy files complited')


if __name__ == "__main__":
    logging.info('Install settings for VSCode started...')
    install_plugins()
    copy_files()
    logging.info('Install settings for VSCode completed')
    logging.info('GoodLuck and HaveFun for using python with VSCode ;-)')
