import unittest
from  selenium import  webdriver
import ddt
import  time


from web_unittest.PageObjects.login_page import LoginPage
from web_unittest.PageObjects.user_page import UserPage
from web_unittest.PageObjects.index_page import IndexPage
from web_unittest.PageObjects.demo_page import BidPage
from web_unittest.TestDatas import invest_datas as id
from web_unittest.TestDatas import common_datas as cd


@ddt.ddt
class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("{}/Index/login.html".format(cd.base_url))
        cls.driver.maximize_window()
        #登录
        LoginPage(cls.driver).login(id.success_data["user"], id.success_data["passwd"])
        # 去投标
        BidPage(cls.driver).invest()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    # def tearDown(self):
    #     self.driver.refresh()
    #正常充值
    # def test_2_invest_success(self):
    #     # LoginPage(self.driver).login(id.success_data["user"],id.success_data["passwd"])
    #     # #去投标
    #     # BidPage(self.driver).invest()
    #     #获取金额
    #     self.driver.refresh()
    #     first_money = IndexPage(self.driver).ord_money()
    #     print(first_money)
    #     #投标
    #     BidPage(self.driver).send_money(id.success_data["money"])
    #     self.assertEqual(id.success_data["check"],IndexPage(self.driver).click_invest_button())
    #     time.sleep(0.5)
    #     #刷新页面
    #     self.driver.refresh()
    #     #第二次获取金额
    #     second_money=IndexPage(self.driver).ord_money()
    #     print(second_money)
    #     self.assertEqual(float(second_money)+int(id.success_data["money"]),float(first_money))
    #异常用例-金额非10的整数倍
    def test_1_invest_failed_by_wrong(self):
        BidPage(self.driver).send_money_null(id.wrong_datas["money"])
        self.assertEqual(id.wrong_datas["check"],IndexPage(self.driver).toubiao_button())
    #异常用例-金额为空，数值不是100的整数倍
    # @ddt.data(*id.fail_datas)
    # def test_0_invest_failed_by_fail(self,data):
    #     BidPage(self.driver).send_money(data["money"])
    #     self.assertEqual(data["check"],IndexPage(self.driver).tools())