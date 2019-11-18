#__author__="G"
#date: 2019/11/14

from selenium.webdriver.common.by import  By

class CgzxPageLocator:
    cancel_order=(By.XPATH,'//a[text()="取消订单"]')

    yes=(By.XPATH,'//button[@class="ant-btn ant-btn-primary ant-btn-sm"]')

    wait_for_pay = (By.XPATH, '//li[text()="待付款"]')

    wait_for_pay_number=(By.XPATH,'//li[text()="待付款"]/span[@class="ml4 colorRed"]')

