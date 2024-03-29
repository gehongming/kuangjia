import configparser
import re
from common.do_config import *
config = ReadConfig()


class Context:

    p = '#(.*?)#'  # 正则表达式

    def re_replace(self, data, re_cls=None):
        data = str(data)  # 把数据强制转换成str，其他格式会报错
        while re.search(self.p, data):
            # print(data)
            # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
            m = re.search(self.p, data)
            g = m.group(1)
            # print(g)
            try:
                v = config.get('data', g)  # 根据KEY取配置文件里面的值
            except configparser.NoOptionError as e:
                from common.do_create_data import EnvData
                if hasattr(re_cls, g):
                    v = str(getattr(re_cls, g))  # 如果被替换的值是int，会报错，需要转换果格式
                elif hasattr(EnvData, g):
                    v = str(getattr(EnvData, g))
                else:
                    print(f'找不到{data}参数化的值')
                    raise e
            data = re.sub(self.p, v, data, count=1)  # 替换
        return data


def replace(para, old, new):
    if para.find(old) != -1:  # para中找到old
        # print(para.find(old))
        data = para.replace(old, new)
        return data
    else:
        return para


if __name__ == '__main__':
    # setattr(Context, "ghm", '123')
    # print(hasattr(Context,'ghm'))
    # v=getattr(Context, 'ghm')
    # print(v)

    data1 = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
    a = Context()
    b = a.re_replace(data1)
    print(b)
    #
    # data='{"mobilephone":"#register_phone#","pwd":"#verify_code#"}'
    # a=Context()
    # b=a.re_replace(data)
    # print(b)
