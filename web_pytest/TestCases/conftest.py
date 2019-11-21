#__author__="G"
#date: 2019/6/29
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/6/20

import os
import allure
import pytest
from selenium import webdriver
from common.delete_history import *
from Testdates import common_datas as cd
from common import contants




# session级别的
@pytest.fixture(scope="session",autouse=True)  #默认调用
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    #清除测试报告、截图目录
    # remove_files_in_dir(contants.reports_log)
    remove_files_in_dir(contants.reports_screen)
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")

@pytest.fixture(scope="class")
def open_url_register():
    # 前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.registered_url)
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()

@pytest.fixture(scope="class")
def open_url1():
    # 前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.base_url)
    yield (driver)  # yield之前代码是前置，之后的代码就是后置。
    #h后置
    driver.quit()

@pytest.fixture(scope="function")
def refresh(open_url1):
    yield
    open_url1[0].refresh()





