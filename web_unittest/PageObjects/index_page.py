from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC
from  selenium.webdriver.common.by import  By
import time

from web_unittest.PageLocators.deom_locator import LoginPageLocator as loc
from web_unittest.PageLocators.user_page_locator import UserPageLocator as up
from web_unittest.common.basepage import BasePage

class IndexPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver
    #正常登陆功能
    def check_nick_name_exists(self):
        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((By.XPATH,'//a[text()="关于我们"]')))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True
        except:
            return False

        # 点击投标按钮
    # def click_invest_button(self):
    #     WebDriverWait(self.driver,20).until(
    #         EC.visibility_of_element_located((By.XPATH,'//div[text()="投标成功！"]')))
    #
    #     return self.driver.find_element(By.XPATH,'//div[text()="投标成功！"]').text
    def click_invest_button(self):
        text=self.get_element_text((By.XPATH,'//div[text()="投标成功！"]'),"点击投标按钮")
        return text
    # #剩余金额
    # def less_money(self):
    #     WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(up.less_money))
    #     return self.driver.find_element(*up.less_money).text
    #获取充值输入框用户金额
    def ord_money(self):
        # WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(up.input_money))
        # return self.driver.find_element(*up.input_money).get_attribute("data-amount")
        attribute=self.get_element_attribute(up.input_money,"data-amount","充值输入框用户金额")
        return attribute
    #弹框文案
    def tools(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(up.invest_tools))
        # return self.driver.find_element(*up.invest_tools).text
        text=self.get_element_text(up.invest_tools,"弹框文案")
        return  text
    #按钮文案
    def toubiao_button(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(up.invest_button))
        # return self.driver.find_element(*up.invest_button).text
        text=self.get_element_text(up.invest_button,"按钮文案")
        return text





