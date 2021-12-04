# from faker import Faker
from common.contants import *
import random
# import socket
# import struct
from faker import Faker
import datetime
import time
from datetime import timedelta
f = Faker(locale='zh_CN')


# 生成ip
def create_ip():
    ip = f.ipv4()
    return ip


def create_phone():
    # 随机生成手机号码
    phone = random.choice(['139', '188', '185', '136', '158', '151', '137', '150', '176']) + \
        "".join(random.choice("0123456789") for i in range(5)) + ''.join('321')
    # phone = faker.phone_number()
    return phone


# 生成银行卡号
def create_card():
    card = f.credit_card_number()
    return card


# 生成姓名
def create_name():
    name = f.name()
    return name


def getdistrictcode():
    codelist = []
    file = open(os.path.join(config_dir, 'districtcode.txt'))
    lines = file.readlines()  # 逐行读取
    for line in lines:
        # 如果每行中去重后不为空，并且6位数字中最后两位不为00，则添加到列表里。（最后两位为00时为省份或地级市代码）
        if line.lstrip().rstrip().strip() != '' and (
                line.lstrip().rstrip().strip())[:6][-2:] != '00':
            codelist.append(line[:6])
            # print(line[:6])
            # print(codelist)
    return codelist


# 生成身份证号
def generator():
    codelist = getdistrictcode()

    id = codelist[random.randint(0, len(codelist) - 1)].split(" ")[0]  # 地区项
    id = id + str(random.randint(1980, 2019))  # 年份项
    da = datetime.date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    # print(type(count))
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {
        '0': '1',
        '1': '0',
        '2': 'X',
        '3': '9',
        '4': '8',
        '5': '7',
        '6': '6',
        '7': '5',
        '8': '5',
        '9': '3',
        '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count % 11)]  # 算出校验码
    return id


def get_current_stamp():
    """获取当天的开始时间，结束时间戳"""

    # 今天日期
    today = datetime.date.today()
    # 昨天时间
    yesterday = today - datetime.timedelta(days=1)
    # 明天时间
    tomorrow = today + datetime.timedelta(days=1)
    acquire = today + datetime.timedelta(days=2)
    # 昨天开始时间戳
    yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
    # 昨天结束时间戳
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    # 今天开始时间戳
    today_start_time = str(yesterday_end_time + 1)
    # 今天结束时间戳
    today_end_time = str(int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1)
    # # 明天开始时间戳
    # tomorrow_start_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')))
    # # 明天结束时间戳
    # tomorrow_end_time = int(time.mktime(time.strptime(str(acquire), '%Y-%m-%d'))) - 1
    # 当前时间时间戳（毫秒）
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    today_time = int(str(int(time.mktime(time.strptime(ts, '%Y-%m-%d %H:%M:%S')))) + '000')
    # 获取格式化日期2021-09-03
    date = time.strftime("%Y-%m-%d", time.localtime())
    # 获取形如2021-09-03 18:59:59的时间
    date_start_time = date + " 00:00:00"
    date_end_time = date + " 23:59:59"
    # YYMMDD格式的日期20210903
    date1 = date.split("-")
    today_date = ''.join(date1)

    return today_start_time, today_end_time, date, today_date, date_start_time, date_end_time, today_time


if __name__ == '__main__':
    print(create_ip())
    print(create_phone())
    print(create_name())
    print(create_card())
    print(generator())

