import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from  selenium.webdriver.common.by import By
from web_unittest.PageLocators.user_page_locator import UserPageLocator as up
import time
from web_unittest.common.basepage import BasePage
class BidPage(BasePage):
    # 属性
    # def __init__(self, driver):
    #     # self.driver = webdriver.Chrome()
    #     self.driver = driver
    #点击投标
    def invest(self):
        # WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(up.qtoubiao))
        # self.driver.find_element(*up.qtoubiao).click()
        self.click_element(up.qtoubiao,"点击投标")
    #输入金额投标
    def send_money(self,money):
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(up.input_money))
        # self.driver.find_element(*up.input_money).send_keys(money)
        self.input_text(up.input_money,"投标输入金额",money)
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(up.toubiao))
            self.driver.find_element(*up.toubiao).click()
        except:
            pass
        try:
            # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(up.invent_tool_ok))
            # self.driver.find_element(*up.invent_tool_ok).click()
            self.click_element(up.invent_tool_ok,"点击提示弹框")
        except:
            pass
    # #查看用户最新金额
    # def get_user_left_money(self):
    #     WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(up.jihuo))
    #     self.driver.find_element(*up.jihuo).click()
    #     WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(up.less_money))
    # 输入金额
    def send_money_null(self, money):
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(up.input_money))
        # self.driver.find_element(*up.input_money).send_keys(money)
        self.input_text(up.input_money,"输入投标金额",money)






    # def get_bid_money(self,money):
    #     pass