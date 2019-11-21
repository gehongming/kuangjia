import unittest
from  selenium import  webdriver
import ddt

from web_unittest.PageObjects.login_page import LoginPage
from web_unittest.PageObjects.index_page import IndexPage
from web_unittest.TestDatas import login_datas as ld
from web_unittest.TestDatas import common_datas as cd

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("{}/Index/login.html".format(cd.base_url))
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def tearDown(self):
        self.driver.refresh()

    #正常登陆
    def test_2_login_success(self):
        LoginPage(self.driver).login(ld.success_data["user"],ld.success_data["passwd"])
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        self.assertEqual(self.driver.current_url,ld.success_data["check"])
    # #异常用例f
    # @ddt.data(*ld.wrong_datas)
    # def test_0_login_failed_by_wrong(self,data):
    #     LoginPage(self.driver).login(data["user"],data["passwd"])
    #     self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_loginForm())
    # #异常用例二
    # @ddt.data(*ld.fail_datas)
    # def test_1_login_failed_by_fail(self,data):
    #     LoginPage(self.driver).login(data["user"],data["passwd"])
    #
    #     self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_pageCenter())



    #