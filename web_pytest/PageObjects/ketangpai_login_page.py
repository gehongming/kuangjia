#__author__="G"
#date: 2019/6/29
import selenium
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from web_pytest.PageLocators.ketangpai_homeworkpage_locator import HomeworkLocator as hw
from web_pytest.PageLocators.ketangpai_letterpage_locator import LetterLocator as ll
from web_pytest.PageLocators.ketangpai_mainpage_locator import MainLocator as ml
from web_pytest.PageLocators.ketangpai_loginpage_locator import LoginLocator as lo
from web_pytest.common.basepage import BasePage
class LoginPage(BasePage):
    def login(self,phone,pwd):
        self.input_text(lo.phone,"输入手机号",phone)
        self.input_text(lo.pwd,"输入密码",pwd)
        self.click_element(lo.login,"点击登录")
        self.click_element(lo.close,"关闭弹框")
    #登录信息获取
    def get_login_success(self):
        self.wait_eleVisible(ml.uesr,"等待用户信息出现")
        self.get_element_attribute(ml.uesr,'title',"获取用户名")
