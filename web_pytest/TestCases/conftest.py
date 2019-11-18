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

from Testdates import common_datas as cd
from common import contants


# 删除指定目录下的文件
def remove_files_in_dir(dir):
    files = os.listdir(dir)
    for item in files:
        c_path = os.path.join(dir,item)
        if os.path.isdir(c_path):
            remove_files_in_dir(c_path)
        else:
            os.remove(c_path)

# session级别的
@pytest.fixture(scope="session",autouse=True)  #默认调用
@allure.step('测试开始')
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    # 清除测试报告、截图目录
    # remove_files_in_dir(contants.reports_log)
    remove_files_in_dir(contants.reports_screen)
    yield
    allure.step('测试结束')
    print("===== 会话结束，测试用例全部执行完成！=====")

@pytest.fixture(scope="class")
@allure.step('启动浏览器，打开网址')
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





