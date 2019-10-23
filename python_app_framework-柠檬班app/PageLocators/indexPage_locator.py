#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 14:59

from appium.webdriver.common.mobileby import MobileBy as MB

class IndexPageLocator:

    #导航栏
    #主页
    home_nav_loc = (MB.ID,"com.lemon.lemonban:id/navigation_home")
    #题库
    tiku_nav_loc = (MB.ID,"com.lemon.lemonban:id/navigation_tiku")
    #我的柠檬
    my_nav_loc = (MB.ID,"com.lemon.lemonban:id/navigation_my")
