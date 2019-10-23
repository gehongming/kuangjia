import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from  selenium.webdriver.common.by import By

from web_pytest.PageLocators.ketangpai_homeworkpage_locator import HomeworkLocator as hw
from web_pytest.PageLocators.ketangpai_letterpage_locator import LetterLocator as ll
from web_pytest.PageLocators.ketangpai_mainpage_locator import MainLocator as ml
from web_pytest.common.basepage import BasePage
class MainPage(BasePage):
    #加入班级
    def join_class(self,code):
        #加入班级
        self.click_element(ml.join_class,"点击加入课程")
        #输入加课验证码
        self.input_text(ml.input_code,"输入加课验证码",code)
        #确定
        self.click_element(ml.join,"确定加入")
    #加课成功提示
    def get_success_join_message(self):
        self.wait_eleVisible(ml.sucess_message,"加入课堂成功信息")
        return self.get_element_text(ml.sucess_message,"加入课堂成功")
    #退课
    def level_class(self,pwd):
        self.click_element(ml.class_set,"点击课堂设置")
        self.click_element(ml.quit_class,"点击退课")
        self.input_text(ml.quit_pwd,"输入密码",pwd)
        self.click_element(ml.button_quit,"点击确定")
    #退课成功提示
    def get_success_quit_message(self):
        self.wait_eleVisible(ml.quit_message,"退课成功提示")
        return self.get_element_text(ml.quit_message,"退课成功提示")
    #进入班级
    def into_class(self):
        self.click_element(ml.into_class,"进入班级")
    #进入私信
    def into_letter(self):
        self.click_element(ml.sixin,"进入私信")



