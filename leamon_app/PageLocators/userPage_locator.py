#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 17:37
from appium.webdriver.common.mobileby import MobileBy as MB
class UserPageLocator:
    # 点击登陆头像
    login_avatar_loc = (MB.ID, "com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")

    #收藏记录条数
    fav_count_loc = (MB.ID,"com.lemon.lemonban:id/fragment_my_lemon_collection_count")

    #请假记录条数
    leave_count_loc = (MB.ID,"com.lemon.lemonban:id/fragment_my_lemon_leave_count")

    #旷课记录条数
    absent_count_loc = (MB.ID,"com.lemon.lemonban:id/fragment_my_lemon_absent_count")

    #本周课表
    week_classes_loc = (MB.ID,"com.lemon.lemonban:id/fragment_my_lemon_expend_layout")

    #收藏列表中-收藏的类型
    #收藏列表当中-类型下对应的题目个数