#__author__="G"
#date: 2019/6/15

import time
import  allure
from PageLocators.pc.shopping_page_locator import ShoppingPageLocator as sp
from common.basepage import BasePage


class ShopPage(BasePage):
    #勾选商品去结算
    @allure.step('选择商品，并结算')
    def  check_goods(self):
        self.click_element2(sp.gogogo,'勾选商品')
        time.sleep(0.3)
        self.click_element(sp.to_buyer,'去结算')
