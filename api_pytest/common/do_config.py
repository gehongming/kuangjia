import configparser
import os

from common import contants



class ReadConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file)
        switch = self.config.get('switch', 'on')  # 读取value
        file = os.path.join(contants.config_dir, f'config_{switch.lower()}.conf')
        self.config.read(file, encoding='utf-8')

    def get(self, section, option):
        try:
            options = self.config.get(section,option)
            return options
        except:
            print(f'配置文件下{section}没有{option}')


config = ReadConfig()
if __name__ == '__main__':
    host = config.get('mysql', 'host')
    print(host)