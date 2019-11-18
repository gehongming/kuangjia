# from faker import Faker
from common.contants import *
import random
# import socket
# import struct
from faker import Faker
from datetime import date
from datetime import timedelta
f=Faker(locale='zh_CN')
#生成ip
def create_ip():
    ip=f.ipv4()
    return  ip

def create_phone():
    # 随机生成手机号码
    phone = random.choice(['300', '400', '500', '600', '700', '800','900','456','123']) + "".join(random.choice("0123456789") for i in range(5))+''.join('321')
    # phone = faker.phone_number()
    return phone
#生成银行卡号
def create_card():
    card=f.credit_card_number()
    return  card
#生成姓名
def create_name():
    name =f.name()
    return name

def getdistrictcode():
    codelist = []
    file = open(os.path.join(config_dir,'districtcode.txt'))
    lines = file.readlines()  # 逐行读取
    for line in lines:
        # 如果每行中去重后不为空，并且6位数字中最后两位不为00，则添加到列表里。（最后两位为00时为省份或地级市代码）
        if line.lstrip().rstrip().strip() != '' and (line.lstrip().rstrip().strip())[:6][
                                                    -2:] != '00':
            codelist.append(line[:6])
            # print(line[:6])
            # print(codelist)
    return codelist
#生成身份证号
def generator():
    codelist = getdistrictcode()

    id = codelist[random.randint(0, len(codelist) - 1)].split(" ")[0]  # 地区项
    id = id + str(random.randint(1980, 2019))  # 年份项
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
    id = id + da.strftime('%m%d')
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    # print(type(count))
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode ={'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5',
                '8': '5', '9': '3', '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
       count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count%11)]  # 算出校验码
    return id

if __name__ == '__main__':
    print(create_ip())
    print(create_phone())
    print(create_name())
    print(create_card())
    print(generator())
