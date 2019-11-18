#__author__="G"
#date: 2019/6/15
#encoding:utf-8
import time
from urllib.parse import unquote
import allure
import pytest
from PageObjects.pc.index_page import IndexPage as ip
from PageObjects.pc.login_page import LoginPage as lp
from PageObjects.pc.order_page import OrderPage as op
from PageObjects.pc.product_page import ProductPage as pp
from PageObjects.pc.shopping_page import ShopPage as sp
from PageObjects.pc.cgzx_page import CgzxPage as cp
from PageObjects.pc.home_page import HomePage as hp
from Testdates import buy_datas  as bd

@allure.feature("每日用例-加购")
@pytest.mark.usefixtures("open_url1")
class TestLogin:

#验证码登录
    @allure.story('登录')
    @allure.title('测试登录正常')
    @allure.description('这是验证码登录的成功用例')
    @allure.link('www.baidu.com')
    @pytest.mark.demo
    def test_login(self,open_url1):
        try:
            lp(open_url1).login_code(bd.login_data["user"],bd.login_data["passwd"])
            time.sleep(5)
            assert True == ip(open_url1).login_check()
        except:
            with open("attach.png", "rb") as f:
                context = f.read()
                allure.attach(context, "错误图片", attachment_type=allure.attachment_type.PNG)
            raise f
#隐形眼镜加入购物车
    @allure.story('测试隐形眼镜加入购物车')
    @allure.title('测试隐形眼镜加入购物车')
    @allure.description('这是隐形眼镜加入购物车的成功用例')
    @pytest.mark.smoke
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
    @allure.story('测试护理液加入购物车')
    @allure.title('测试护理液加入购物车')
    @allure.description('这是护理液加入购物车的成功用例')
    @pytest.mark.smoke
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
#进入购物车,选择商品并结算
    @pytest.mark.smoke
    @allure.story('测试购物车结算')
    @allure.title('测试购物车结算')
    @allure.description('这是定制片加入购物车的成功用例')
    def test_orders(self,open_url1):
        hp(open_url1).click_cart()
        time.sleep(1.5)
        sp(open_url1).check_goods()
        time.sleep(2)
        op(open_url1).generate_orders(bd.to_order["message"])
        time.sleep(3)
        assert open_url1.current_url==bd.to_order["check_url"]
#进入采购单
    # @pytest.mark.demo
    # @allure.story('进入采购单')
    # @allure.title('测试进入采购单')
    # @allure.description('这是进入采购单的成功用例')
    # def test_go_purchase_order(self, open_url1):
    #     hp(open_url1).purchase_order()
    #     time.sleep(0.2)
#取消订单
    @allure.story('测试取消订单')
    @allure.title('测试取消订单')
    @allure.description('这是取消采购中心订单的成功用例')
    @pytest.mark.smoke
    def test_cancel_order_yes(self,open_url1):
        time.sleep(0.2)
        cp(open_url1).cancel_order_yes()
        time.sleep(3)

















