#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_tiku
# Author: 简
# Time: 2019/3/27

import pytest
from PageObjects.index_page import IndexPage
from PageObjects.tiku_page import TikuPage
import random

@pytest.mark.usefixtures("start_app")
class TestTiku:

    def test_enter_tiku_suites(self,start_app):
        #切换到题库
        IndexPage(start_app).click_nav_by_name("题库")
        tk = TikuPage(start_app)
        # 获取所有的题库类型
        tk.get_all_tiku_type_names()
        #随机题库类型
        index = random.randint(0,len(tk.tiku_types_list)-1)
        # 选择题库类型
        tk.select_tiku_type_by_name(tk.tiku_types_list[index])
        #选择题库难易程序
        tk.select_topic_level("初级")
        #选择套题
        tk.select_topic_suite_by_random()

    def test_favirate_topic(self):
        pass

    def test_open_topic_answer(self):
        pass

