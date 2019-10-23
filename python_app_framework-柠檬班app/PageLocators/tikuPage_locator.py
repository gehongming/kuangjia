#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 15:00
from appium.webdriver.common.mobileby import MobileBy as MB

class TikuPageLocator:

    #题库类别
    titu_type_loc = (MB.ID,"com.lemon.lemonban:id/fragment_category_type")

    #点击题库类型名称进入题库页面
    tiku_title_loc = (MB.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).\
scrollIntoView(new UiSelector().textMatches(\"{}\"))')

    #初级题库
    firstLevel_loc = (MB.ID,"com.lemon.lemonban:id/first_level")
    # 中级题库
    secondLevel_loc = (MB.ID,"com.lemon.lemonban:id/second_level")
    #高级题库
    thirdLevel_loc = (MB.ID,"com.lemon.lemonban:id/third_level")

    #套题 列表 - 套路标题
    suite_title_loc = (MB.ID,"com.lemon.lemonban:id/suit_subject_title")

    #收藏开关
    favirate_switch_loc = (MB.ID,"com.lemon.lemonban:id/action_favourite")
    #答案开关
    answer_switch_loc = (MB.ID,"com.lemon.lemonban:id/switch_button")
    #拖动开关
    drag_loc = (MB.ID,"com.lemon.lemonban:id/dpl_dragger")

    #收藏成功
    favirate_msg_loc = (MB.XPATH,'//*[contains(@text,"收藏成功")]')
    #取消收藏
    cancel_favirate_msg_loc = (MB.XPATH,'//*[contains(@text,"取消收藏")]')

    #答案区域
    answer_content_loc = (MB.ID,"com.lemon.lemonban:id/tvBody")

