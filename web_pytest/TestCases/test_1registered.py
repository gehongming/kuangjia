#__author__="G"
#date: 2019/6/15
#encoding:utf-8
import time
from urllib.parse import unquote
import allure
import pytest
from PageObjects.pc.index_page import IndexPage as ip
from PageObjects.pc.registered_page import RegisteredPage as rp
from Testdates import registered_datas  as rd


@pytest.mark.usefixtures("open_url_register")
@allure.feature('每日用例-注册')
class TestLogin:
#申请店铺不上传医疗许可证
    @pytest.mark.register2
    def test_login(self,open_url_register):
        time.sleep(0.1)
        rp(open_url_register).aggre()
        rp(open_url_register).check_phone(rd.zhanghao_data["phone"],rd.zhanghao_data["code"])
        time.sleep(2)
        assert True == ip(open_url_register).register_check()
        rp(open_url_register).register(rd.store_data["storename"],rd.store_data["address"],rd.store_data["contact"])
        rp(open_url_register).update_business(rd.store_data["b_address"])
        time.sleep(0.5)
        # rp(open_url_register).tijiao()
        time.sleep(5)

    # 申请店铺上传医疗许可证
    @pytest.mark.smoke
    def test_login2(self,open_url_register):
        time.sleep(0.1)
        rp(open_url_register).aggre()
        rp(open_url_register).check_phone(rd.zhanghao_data["phone"],rd.zhanghao_data["code"])
        time.sleep(2)
        assert True == ip(open_url_register).register_check()
        rp(open_url_register).register(rd.store_data["storename"],rd.store_data["address"],rd.store_data["contact"])
        rp(open_url_register).update_business(rd.store_data["b_address"])
        rp(open_url_register).update_medical(rd.store_data["m_address"])
        time.sleep(2)
        rp(open_url_register).tijiao()
        assert True==ip(open_url_register).success_register()
        time.sleep(5)




















