#__author__="G"
#date: 2019/6/15

from selenium.webdriver.common.by import  By

class LoginPageLocator:
    #输入手机号/账号
    uesr_loc=(By.XPATH,'//input[@name="phone"]')
    #输入密码
    password=(By.XPATH,'//input[@name="phoneCode"]')
    #登录
    login=(By.XPATH,'//a[@class="login"]')
