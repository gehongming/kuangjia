import configparser
import re

import jmespath

from common.config import config
from common.create_data import *

class Context:

    date_time = get_current_stamp()
    startTime = date_time[0]
    endTime = date_time[1]
    updateStartTime = date_time[0]
    updateEndTime = date_time[1]
    date = date_time[3]
    dateStartTime = date_time[4]
    dateEndTime = date_time[5]
    today_time = date_time[-1]
    name = "新增客户资料" + str(time.time())
    tels = create_phone()
    names = create_name()
    ip = create_ip()
    card = create_card()

    p = '#(.*?)#'  # 正则表达式

    def re_replace(self, data):
        while re.search(self.p, data):
            # print(data)
            # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
            m = re.search(self.p, data)
            g = m.group(1)
            print(g)
            try:
                v = config.get('data', g)  # 根据KEY取配置文件里面的值
            except configparser.NoOptionError as e:
                if hasattr(Context, g):
                    v = getattr(Context, g)
                else:
                    print('找不到参数化的值')
                    raise e
            data = re.sub(self.p, v, data, count=1)  # 替换
        return data

    def re_par(self, par, resp):
        """
        par: 列表格式
        resp：请求返回值
        """
        error_list = []
        if isinstance(par, list):
            for exp in par:
                for k,v in exp.items():
                    cashu = jmespath.search(v, resp)
                    if cashu:
                        setattr(Context, k, cashu)
                    elif cashu == 0:
                        setattr(Context, k, cashu)
                    else:
                        setattr(Context, k, None)
                        error_list.append(k)
            return (f'转换成功,该字段--{error_list}--没有正常转换，手动转为None')
        else:
            return (f'{par}格式错误')


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
