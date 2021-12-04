import configparser

from common import contants


class ReadConfig:

    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(contants.global_file)
        switch=self.config.getboolean('switch','on') #读取value
        if switch: #判断value值
            self.config.read(contants.online_file, encoding='utf-8')
        else:
            self.config.read(contants.test_file, encoding='utf-8')

    def get(self,section,option):
        return self.config.get(section,option)


config=ReadConfig()
if __name__ == '__main__':
    host=config.get('mysql','host')
    print(host)