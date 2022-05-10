import configparser
import os

from common import do_contants



class ReadConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(do_contants.global_file)
        switch = self.config.get('switch', 'on')  # 读取value
        file = os.path.join(do_contants.config_dir, f'config_{switch.lower()}.conf')
        self.config.read(file, encoding='utf-8')

    def get(self, section, option):
            return self.config.get(section,option)


class WriteConfig:

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(do_contants.global_file,encoding='utf-8')

    def write(self, value, section='switch', option='on'):
            self.config.read(do_contants.global_file)
            self.config.set(section, option, value)
            file_global = os.path.join(do_contants.global_file)
            with open(file_global, 'w') as wf:
                self.config.write(wf)


if __name__ == '__main__':
    config = ReadConfig()
    host = config.get('mysql', 'host')
    print(host)