import configparser
import re

from api_unittest.common.config import config


class Context:
    loan_id = None
    p = '#(.*?)#'  # 正则表达式

    def replace(self,data):
        while re.search(self.p,data):
            # print(data)
            m=re.search(self.p,data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
            g=m.group(1)
            try:
                v=config.get('data',g) # 根据KEY取配置文件里面的值
            except configparser.NoOptionError as e:
                if hasattr(Context,g):
                    v=getattr(Context,g)
                else:
                    print('找不到参数化的值')
                    raise e
            # print(v)
            data = re.sub(self.p, v, data, count=1)  # 替换
        return data

if __name__ == '__main__':
    data='{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
    a=Context()
    b=a.replace(data)
    print(b)