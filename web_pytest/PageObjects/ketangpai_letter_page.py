import selenium
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from web_pytest.PageLocators.ketangpai_homeworkpage_locator import HomeworkLocator as hw
from web_pytest.PageLocators.ketangpai_letterpage_locator import LetterLocator as ll
from web_pytest.PageLocators.ketangpai_mainpage_locator import MainLocator as ml
from web_pytest.common.basepage import BasePage
import time
class LetterPage(BasePage):

    #发送私信
    def search_man(self,man,letter):
        self.input_text(ll.search_man,"输入搜索人",man),Keys.ENTER
        time.sleep(0.5)
        self.click_element(ll.check_man,"选择对象")
        time.sleep(1)
        self.input_text(ll.input_message,"输入信息",letter)
        self.click_element(ll.send_message,"点击发送")
    #获取发送信息
    # def get_send_message(self):
    #     self.get_element_text(ll.)





