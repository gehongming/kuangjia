#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/7/8
import pytest
import yaml
from app_framework.Common.contants import caps_dir
from appium import webdriver

@pytest.fixture
def startApp():
    # 启动会话
    driver = base_driver()
    yield driver
    driver.close_app()

@pytest.fixture
def startApp_reset():
    # 启动会话
    driver = base_driver(False)
    yield driver
    driver.close_app()

@pytest.fixture
def loginApp():
    # 启动会话
    driver = base_driver()
    # 判断登陆状态并根据状态做不同的处理。

    pass


def base_driver(noReset=True,port=4723,**kwargs):
    # 固定启动参数 - 字典
    # 读取yaml的数据文件
    fs = open(caps_dir , encoding="utf-8")
    desired_caps = yaml.load(fs, Loader=yaml.BaseLoader)
    # 如果有更多的启动参数，动态添加。
    if noReset is False:
        desired_caps["noReset"] = False
    if kwargs:
        for key,value in kwargs.items():
            desired_caps[key] = value
    # 根据启动参数，启动会话。
    driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port),desired_caps)
    return driver


#

