#__author__="G"
#date: 2019/6/27
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC
from  selenium.webdriver.common.by import  By

from web_pytest.PageLocators.ketangpai_homeworkpage_locator import HomeworkLocator as hw
from web_pytest.PageLocators.ketangpai_letterpage_locator import LetterLocator as ll
from web_pytest.PageLocators.ketangpai_mainpage_locator import MainLocator as ml
import time
from web_pytest.common.basepage import BasePage

class HomeworkPage(BasePage):
    #上传作业
    def input_work(self,file,message):


        self.click_element(hw.input_file,"点击上传作业")
        self.click_element(hw.file, "点击上传文件")
        self.upload(file,"上传文件")
        self.click_element(hw.check_message,"点击留言")
        self.input_text(hw.input_message,"输入留言",message)
        self.click_element(hw.save_message,"保存")
    #     self.click_element(hw.tijiao,"提交作业")
    #     self.wait_eleVisible(hw.get,"等待知道了出现")
    #     self.click_element(hw.get,"点击知道了")
    # #获取作业提交成功提示
    # def get_success_file(self):
    #     self.wait_eleVisible(hw.success_tijiao,"等待作业提交提示")
    #     self.get_element_text(hw.success_tijiao,"作业提交成功提示")

