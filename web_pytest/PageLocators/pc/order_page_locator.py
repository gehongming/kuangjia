#__author__="G"
#date: 2019/6/15

from selenium.webdriver.common.by import  By

class OrderPageLocator:
    #留言
    gogogo=(By.XPATH,'//textarea')
    #结算
    to_buyer=(By.XPATH,'//div[text()="确认采购"]')
    #总金额
    zongjine=(By.XPATH,'//ul[@class="settlement--value"]/li[1]')
    # 物流运费
    wuliu= (By.XPATH, '//ul[@class="settlement--value"]/li[2]')
    #优惠
    youhui=(By.XPATH, '//ul[@class="settlement--value"]/li[3]')
   #应付金额
    yingfu=(By.XPATH, '//ul[@class="settlement--value"]/li[4]')