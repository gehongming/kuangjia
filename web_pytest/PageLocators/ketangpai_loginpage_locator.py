#__author__="G"
#date: 2019/6/29


from  selenium.webdriver.common.by import By



class LoginLocator:
    #点击登录
    denglu=(By.XPATH,'//a[@class="login"]')

    #输入手机号
    phone=(By.XPATH,'//input[@type="text"and@name="account"]')

    #输入密码
    pwd=(By.XPATH,'//input[@type="password"]')

    #登录
    login=(By.XPATH,'//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')


    #关闭弹框
    close=(By.XPATH,'//a[@class="close"]')

