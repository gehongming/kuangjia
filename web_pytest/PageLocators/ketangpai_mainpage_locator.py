#__author__="G"
#date: 2019/6/27
from selenium.webdriver.common.by import By
from web_pytest.TestDatas import work_datas as wd

class MainLocator:
    #加入课程
    join_class=(By.XPATH,'//div[@class="ktcon1l fl"]')
   #输入上课码
    input_code=(By.XPATH,'//input[@placeholder="请输入课程加课验证码"]')
    #加入
    join=(By.XPATH,'//a[text()="加入"]')
    #加入成功提示
    sucess_message=(By.XPATH,'//div[@id="show-tip"]/span[text()="加入课堂成功"]')
    #课堂设置
    class_set=(By.XPATH,'//dt[@class="bgclass2"]/a[@class="kdmore"]')
    #退课
    quit_class=(By.XPATH,'//dt[@class="bgclass2"]/ul[@class="kdcgd"]/li[@class="kdli3"]/a[text()="退课"]')
    #退课密码校验
    quit_pwd=(By.XPATH,'//input[@type="password"]')
    #退课按钮
    button_quit=(By.XPATH,'//li[@class="dli2"]/a[text()="退课"]')
    #退课成功提示
    quit_message=(By.XPATH,'//div[@id="show-tip"]/span[text()="课程退课成功"]')
    # 进入所在班级
    into_class = (By.XPATH, '//strong/a[@href="/Course/Homework/courseid/MDAwMDAwMDAwMLOspd2Gz79r.html"]')
    #进入私信
    sixin=(By.XPATH,'//a[@href="/Letter/index.html" and text()="私信"]')
    #用户信息
    uesr=(By.XPATH,'//img[@src="/Public/Common/img/40/29.png"]')

