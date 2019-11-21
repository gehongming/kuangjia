#__author__="G"
#date: 2019/6/15
#encoding:utf-8
import time
from urllib.parse import unquote
import allure
import pytest
from common.file import get_filelist
from PageObjects.pc.index_page import IndexPage as ip
from PageObjects.pc.login_page import LoginPage as lp
from PageObjects.pc.order_page import OrderPage as op
from PageObjects.pc.product_page import ProductPage as pp
from PageObjects.pc.shopping_page import ShopPage as sp
from PageObjects.pc.cgzx_page import CgzxPage as cp
from PageObjects.pc.home_page import HomePage as hp
from Testdates import buy_datas  as bd
from common import contants




@allure.feature("每日用例-加购")
@pytest.mark.usefixtures("open_url1")
class TestLogin:

#验证码登录
    @pytest.mark.smoke
    @allure.story('登录')
    @allure.title('测试登录正常')
    @allure.description('这是验证码登录的成功用例')
    def test_login(self,open_url1):
        try:
            lp(open_url1).login_code(bd.login_data["user"],bd.login_data["passwd"])
            time.sleep(5)
            assert True == ip(open_url1).login_check()
        except AssertionError as e:
            Filelist = get_filelist(contants.reports_screen)
            with open(Filelist[0], "rb") as f:
                context = f.read()
                allure.attach(context, "错误图片", attachment_type=allure.attachment_type.PNG)
                raise e


#隐形眼镜加入购物车

    @pytest.mark.smoke
    @allure.story('测试隐形眼镜加入购物车')
    @allure.title('测试隐形眼镜加入购物车')
    @allure.description('这是隐形眼镜加入购物车的成功用例')
    def test_buy_yx(self,open_url1):
        #搜索隐形眼镜商品
        hp(open_url1).search(bd.success_data_yxyj["title"])
        time.sleep(2)
        #是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8')== bd.success_data_yxyj["check_url"]
        #点击进入商品详情页,并切换窗口
        hp(open_url1).click_yx()
        time.sleep(5)
        #验证是否进入
        assert unquote(open_url1.current_url, encoding='utf-8')==bd.success_data_yxyj["check_product_url"]
        #选择sku
        pp(open_url1).yxyj()
        assert True == ip(open_url1).jiaru_success()

#护理液加入购物车
    @pytest.mark.smoke
    @allure.story('测试护理液加入购物车')
    @allure.title('测试护理液加入购物车')
    @allure.description('这是护理液加入购物车的成功用例')
    def test_buy_hl(self, open_url1):
        hp(open_url1).search(bd.success_data_huliye["title"])
        time.sleep(2)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_huliye["check_url"]
        # 点击进入商品详情页,并切换窗口
        hp(open_url1).click_hl()
        # 验证是否进入
        time.sleep(3)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_huliye["check_product_url"]
        # 选择数量并加入购物车
        pp(open_url1).huliye('1')
        assert True == ip(open_url1).jiaru_success()

#定制片加入购物车
    @pytest.mark.smoke
    @allure.story('测试定制片加入购物车')
    @allure.title('测试定制片加入购物车')
    @allure.description('这是定制片加入购物车的成功用例')
    def test_buy_dzp(self, open_url1):
        hp(open_url1).search(bd.success_data_dzp["title"])
        time.sleep(2)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_dzp["check_url"]
        # 点击进入商品详情页,并切换窗口
        hp(open_url1).click_dz()
        # 验证是否进入
        time.sleep(3)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_dzp["check_product_url"]
        # 选择sku并加入购物车
        pp(open_url1).dingzhi(bd.success_data_dzp["sku"][0],bd.success_data_dzp["sku"][1],bd.success_data_dzp["sku"][2],
        bd.success_data_dzp["sku"][3],bd.success_data_dzp["sku"][4])

        assert True == ip(open_url1).jiaru_success()

#多彩伴侣盒加入购物车
    @pytest.mark.smoke
    @allure.story('测试伴侣盒加入购物车')
    @allure.title('测试伴侣盒加入购物车')
    @allure.description('这是伴侣盒加入购物车的成功用例')
    def test_buy_blh(self, open_url1):
        hp(open_url1).search(bd.success_data_blh["title"])
        time.sleep(2)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_blh["check_url"]
        # 点击进入商品详情页,并切换窗口
        hp(open_url1).click_blh()
        # 验证是否进入
        time.sleep(3)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_blh["check_product_url"]
        # 选择sku并加入购物车
        pp(open_url1).banlvhe(bd.success_data_blh["count"])
        assert True == ip(open_url1).jiaru_success()

#镜片加入购物车
    @pytest.mark.smoke
    @allure.story('测试镜片加入购物车')
    @allure.title('测试镜片加入购物车')
    @allure.description('这是镜片加入购物车的成功用例')
    def test_buy_jp(self, open_url1):
        hp(open_url1).search(bd.success_data_jp["title"])
        time.sleep(2)
        # 是否进入搜索结果页
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_jp["check_url"]
        # 点击进入商品详情页,并切换窗口
        hp(open_url1).click_jp()
        # 验证是否进入
        time.sleep(3)
        assert unquote(open_url1.current_url, encoding='utf-8') == bd.success_data_jp["check_product_url"]
        # 选择sku并加入购物车
        pp(open_url1).jingpian(bd.success_data_jp["count"])
        assert True == ip(open_url1).jiaru_success()

    #进入购物车,选择普通商品并结算
    @pytest.mark.smoke
    @allure.story('测试购物车结算')
    @allure.title('测试购物车结算')
    @allure.description('这是普通片加入购物车的成功用例')
    def test_orders(self,open_url1):
        hp(open_url1).click_cart()
        time.sleep(1.5)
        sp(open_url1).check_goods()
        time.sleep(2)
        op(open_url1).generate_orders(bd.to_order["message"])
        time.sleep(3)
        assert open_url1.current_url==bd.to_order["check_url"]

    #进入购物车,选择定制商品并结算
    @pytest.mark.smoke
    @allure.story('测试购物车结算')
    @allure.title('测试购物车结算')
    @allure.description('这是定制片加入购物车的成功用例')
    def test_dz_orders(self,open_url1):
        hp(open_url1).click_cart_new()
        time.sleep(0.8)
        sp(open_url1).check_goods_dz()
        time.sleep(0.3)
        op(open_url1).generate_orders(bd.to_order["message"])
        time.sleep(3)
        assert open_url1.current_url==bd.to_order["check_url"]

    #进入采购单
    # @pytest.mark.ignore
    # @allure.story('进入采购单')
    # @allure.title('测试进入采购单')
    # @allure.description('这是进入采购单的成功用例')
    # def test_go_purchase_order(self, open_url1):
    #     hp(open_url1).purchase_order()
    #     time.sleep(0.2)

#取消订单
    @pytest.mark.smoke
    @allure.story('测试取消订单')
    @allure.title('测试取消订单')
    @allure.description('这是取消采购中心订单的成功用例')
    def test_cancel_order_yes(self,open_url1):
        time.sleep(0.2)
        cp(open_url1).cancel_order_yes()
        time.sleep(3)

















