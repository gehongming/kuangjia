import selenium
from  selenium.webdriver.common.by import By
from web_unittest.PageLocators.login_page_locator import LoginPageLocator as lc
from web_unittest.common.basepage import BasePage
class LoginPage(BasePage):

    #正常登陆
    def login(self, user, passwd):
        self.input_text(lc.user_loc,"登陆页面_输入用户名",user)
        self.input_text(lc.passwd_loc,"登陆页面_输入密码",passwd)
        self.click_element(lc.login_button_loc,"登陆页面_点击登陆按钮")
    #获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        self.get_element_text(lc.error_notify_from_loginForm,"登陆页面_表单区域错误信息")
        return self.get_element_text(lc.error_notify_from_loginForm, "登陆页面_表单区域错误信息")
    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        self.get_element_text(lc.error_notify_from_pageCenter, "登陆页面_页面中间错误信息")
        return self.get_element_text(lc.error_notify_from_pageCenter,"登陆页面_页面中间错误信息")