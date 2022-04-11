# from faker import Faker
from common.contants import *
import random
from faker import Faker
from datetime import date
from datetime import timedelta
import jmespath

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
    da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
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


class EnvData:
    """
    用于参数传递，获取动态参数
    """
    ip = create_ip()
    tel = create_phone()
    card = create_card()
    name = create_name()
    generator = generator()

    def re_par_new(self, par, resp, re_cls):
        """
        par: jsonpath_exp_save 列表嵌套字典
        resp：请求返回值
        re_cls：用例类
        作用：jsonpath_exp_save提取特定返回值，并存储于特定类的属性中
        """
        error_list = []
        success_list = []
        if isinstance(par, list):
            for exp in par:
                for k, v in exp.items():
                    cashu = jmespath.search(v, resp)
                    if cashu or cashu == 0:
                        setattr(re_cls, k, cashu)
                        success_list.append(k)
                    # elif cashu == 0:
                    #     setattr(re_cls, k, cashu)
                    else:
                        setattr(re_cls, k, None)
                        error_list.append(k)
            if error_list:
                return (f'{success_list}提取成功,{error_list}没有正常提取，手动设置None')
            else:
                return (f'{success_list}提取成功')
        else:
            return (f'{par}格式错误')


if __name__ == '__main__':
    print(create_ip())
    print(create_phone())
    print(create_name())
    print(create_card())
    print(generator())
