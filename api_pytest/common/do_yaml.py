import yaml
import os
from common import do_contants


class DoYaml:
    def __init__(self, yamlfilepath):
        if os.path.exists(yamlfilepath):
            self.yamlfilepath = yamlfilepath
        else:
            raise FileNotFoundError('文件不存在！')

    def read_yaml(self):
        with open(self.yamlfilepath, 'rb') as f:
            y = yaml.load(f, Loader=yaml.FullLoader)
        return y

    def write_yaml(self, num, key, value):
        with open(self.yamlfilepath, 'rb') as f:
            y = yaml.load(f, Loader=yaml.FullLoader)
            y[int(num - 1)][key] = value

        with open(self.yamlfilepath, 'w', encoding='utf-8') as w_f:
            # 覆盖原先的配置文件
            yaml.dump(y, w_f, allow_unicode=True)
            # y = yaml.load(f, Loader=yaml.FullLoader)
        return y


if __name__ == '__main__':
    a = DoYaml(do_contants.case_file + '\\wap_day.yaml')
    b = a.read_yaml()
    print(b)
    # print(
    # a.write_yaml(b,'result','false'))
