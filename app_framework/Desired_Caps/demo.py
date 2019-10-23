#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: demo
# Author: 简
# Time: 2019/7/8

import yaml

# 读取yaml的数据文件
fs = open("caps.yaml",encoding="utf-8")
dict_obj = yaml.load(fs,Loader=yaml.BaseLoader)
print(dict_obj)

