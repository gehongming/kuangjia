import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from  selenium.webdriver.common.by import By
from week_11.PageLocators.user_page_locator import UserPageLocator as up
class UserPage:

    # 属性
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
    #获取当前金额
    def get_user_left_money(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(up.user_money))
        return up.user_money.text