#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 21:17

import pytest
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage

@pytest.mark.usefixtures("init_app")
class TestLogin:

    def test_login_success(self,init_app):
        #切换到我的柠檬
        IndexPage(init_app).click_nav_by_name("我")
        #点击头像#登陆操作
        lp = LoginPage(init_app)
        lp.click_login_avatar().login_action("18684720553","720553")
        # 获取登陆状态
        assert lp.get_login_status() is True


