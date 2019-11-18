#__author__="G"
#date: 2019/6/15
import time

from  selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class IndexPage:
    def __init__(self,driver):
        self.driver=driver
    #登录成功校验
    def login_check(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID,'gosupplier')))
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath('//a[contains(text(),"您好")]')
            return True
        except:
            return False
    #加入购物车成功校验
    def jiaru_success(self):
        try:
            WebDriverWait(self.driver,20).until(
                EC.visibility_of_element_located((By.XPATH,'//div[text()="已成功加入购物车"]')))
            return  True
        except:
            return False
     #进入店铺注册信息填写校验
    #进入店铺信息填写页校验
    def register_check(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,'//p[text() = "以下信息需要审核填写真实信息"]')))
            return  True
        except:
            return False
    #注册成功校验
    def success_register(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,'// p[text() = "提交成功"]')))
            return  True
        except:
            return False



