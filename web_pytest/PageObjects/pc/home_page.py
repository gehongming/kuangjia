#__author__="G"
#date: 2019/6/15

from selenium.webdriver.common.keys import Keys
import allure
from PageLocators.pc.home_page_locator import HomePageLocator as hpl
from common.basepage import BasePage


class HomePage(BasePage):
    #搜索商品
    @allure.step('搜索商品')
    def search(self,title):
        self.input_text(hpl.search,'搜索商品',title,Keys.ENTER)

    #点击yx商品
    @allure.step('点击进入隐形眼镜商品详情页面')
    def click_yx(self):
        self.check_window(hpl.yx,'进入隐形商品详情页并切换窗口')

    #点击hl商品
    @allure.step('点击进入护理液商品详情页面')
    def click_hl(self):
        self.check_window(hpl.hl,'进入护理商品详情页面并切换窗口')

    # 点击dz商品
    @allure.step('点击进入定制商品详情页面')
    def click_dz(self):
        self.check_window(hpl.dz, '进入定制商品详情页面并切换窗口')

    #点击blh商品
    @allure.step('点击进入伴侣盒商品详情页面')
    def click_blh(self):
        self.check_window(hpl.blh,'进入伴侣盒商品详情页面并切换窗口')

    #点击jp商品
    @allure.step('点击进入镜片商品详情页面')
    def click_jp(self):
        self.check_window(hpl.jp,'进入镜片商品详情页面并切换窗口')

    # 老项目进入购物车
    @allure.step('点击进入购物车')
    def click_cart(self):
        self.click_element(hpl.go_cart, '进入购物车')

        # 新项目进入购物车
    @allure.step('点击进入购物车')
    def click_cart_new(self):
        self.check_window(hpl.go_cart_new, '进入购物车')

    #进入采购单
    @allure.step('进入采购单页面')
    def purchase_order(self):
        self.click_element(hpl.go_purchase_order, '进入采购单')




