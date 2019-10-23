#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/15 21:28

from appium.webdriver.common.mobileby import MobileBy as MB

class LoginPageLocator:

    #点击登陆头像
    login_avatar_loc = (MB.ID,"com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")
    # 用户名文本元素
    avatar_title_loc = (MB.ID,"com.lemon.lemonban:id/fragment_my_lemon_avatar_title")

    #用户名输入框
    user_loc = (MB.ID,"com.lemon.lemonban:id/et_mobile")
    #密码输入框
    passwd_loc = (MB.ID,"com.lemon.lemonban:id/et_password")
    #登陆按钮
    loginButton_loc = (MB.ID,"com.lemon.lemonban:id/btn_login")
