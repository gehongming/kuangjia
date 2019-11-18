from selenium.webdriver.common.by import  By

class ShoppingPageLocator:
    #勾选店铺商品
    gogogo=(By.XPATH,'//span[text()="赛目光学"]/parent::div/span/label/span/input')
    #去结算
    to_buyer=(By.XPATH,'//li[text()="去结算"]')
