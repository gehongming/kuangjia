#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 17:28

from Common.basepage import BasePage
from PageLocators.indexPage_locator import IndexPageLocator as loc
from Common import logger
import logging


class IndexPage(BasePage):

    #点击导航栏内容
    def click_nav_by_name(self,nav_name):
        """
        :param nav_name: 导航名称。值为：首页、题库、我
        :return: None
        """
        if nav_name == "首页":
            self.click_element(loc.home_nav_loc,"首页_点击主页按钮")
        elif nav_name == "题库":
            self.click_element(loc.tiku_nav_loc,"首页_点击题库按钮")
        elif nav_name == "我":
            self.click_element(loc.my_nav_loc,"首页_点击我的柠檬按钮")
        else:
            logging.ERROR("没有此导航名称！！")
