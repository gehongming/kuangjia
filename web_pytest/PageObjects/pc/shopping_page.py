#__author__="G"
#date: 2019/6/15

import time
import  allure
from PageLocators.pc.shopping_page_locator import ShoppingPageLocator as sp
from common.basepage import BasePage


class ShopPage(BasePage):
    #勾选普通商品去结算
    @allure.step('选择普通商品，并结算')
    def  check_goods(self):
        self.click_element2(sp.gogogo,'勾选赛目商品')
        if self.wait_eleExist_true(sp.gogogo_2,'非赛目大B'):
            self.click_element2(sp.gogogo_2, '勾选非赛目商品')
            self.click_element(sp.to_buyer,'去结算')
        else:
            self.click_element(sp.to_buyer, '去结算')
    #勾选定制商品去结算
    @allure.step('选择定制商品，并结算')
    def  check_goods_dz(self):
        self.click_element(sp.check_dz,'切换到定制片')
        time.sleep(0.5)
        self.click_element2(sp.gogogo,'勾选赛目商品')
        if self.wait_eleExist_true(sp.gogogo_2,'非赛目大B'):
            self.click_element2(sp.gogogo_2, '勾选非赛目商品')
            self.click_element(sp.to_buyer,'去结算')
        else:
            self.click_element(sp.to_buyer, '去结算')

