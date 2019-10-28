#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 17:28

from Common.basepage import BasePage
from PageLocators.loginPage_locator import LoginPageLocator as loc

class LoginPage(BasePage):

    #点击头像进入登陆页面
    def click_login_avatar(self):
        self.click_element(loc.login_avatar_loc,"登陆页_点击登陆头像")
        return self

    #登陆操作
    def login_action(self,username,passwd):
        self.input_text(loc.user_loc,username,"登陆页_输入用户名")
        self.input_text(loc.passwd_loc,passwd,"登陆页_输入密码")
        self.click_element(loc.loginButton_loc,"登陆页_点击登陆按钮")
        return self

    # 获取登陆状态
    def get_login_status(self):
        status = self.get_text(loc.avatar_title_loc,"登陆页面_获取用户登陆状态")
        if status == "点击头像登录": # 未登陆
            return False
        else:
            return True  # 已登陆


