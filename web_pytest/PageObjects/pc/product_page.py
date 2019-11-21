
import time
import  allure
from PageLocators.pc.product_page_locator import ProductPageLocator as ppl
from common.basepage import BasePage


class ProductPage(BasePage):

    #隐形眼睛加入购物车
    @allure.step('选择隐形眼镜sku，加入购物车')
    def yxyj(self):
        #选择花色及数量
        self.click_element(ppl.yx_huase,'选择花色')
        self.click_element(ppl.yx_dushu,'选择度数即数量')
        self.click_element(ppl.join_gwc,'加入购物车')
    def yxyj_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')

    # 护理液操作加入购物车
    @allure.step('选择隐形眼镜sku，加入购物车')
    def huliye(self,count):
        self.input_text(ppl.hl_count,'选择数量',count)
        self.click_element(ppl.join_gwc, '加入购物车')
    def hl_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')

    # 定制片操作加入购物车
    @allure.step('选择隐形眼镜sku，加入购物车')
    def dingzhi(self,zyy,qj,zj,zw,c):
        self.input_text(ppl.dz_zyy,'选择左右眼',zyy)
        self.input_text(ppl.dz_dzqj, '选择定制球镜', qj)
        self.input_text(ppl.dz_dzzj, '选择定制柱镜', zj)
        self.input_text(ppl.dz_zw, '选择轴位', zw)
        self.input_text(ppl.dz_count, '选择数量', c)
        time.sleep(2)
        self.click_element(ppl.join_gwc, '加入购物车')
    def dz_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')

# 多彩伴侣盒操作加入购物车
    @allure.step('选择隐形眼镜sku，加入购物车')
    def banlvhe(self,c):
        self.input_text(ppl.blh_count, '选择数量', c)
        time.sleep(2)
        self.click_element(ppl.join_gwc, '加入购物车')
    def blh_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')

# 镜片操作加入购物车
    @allure.step('选择隐形眼镜sku，加入购物车')
    def jingpian(self,c):
        self.input_text(ppl.jp_count, '选择数量', c)
        time.sleep(2)
        self.click_element(ppl.join_gwc, '加入购物车')
    def jp_success(self):
        return self.get_element_text(ppl.success_gwc,'加入购物车成功提示文案')


