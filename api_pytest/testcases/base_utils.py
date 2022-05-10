# -*- coding: utf-8 -*-
"""
@Time ： 2022/4/11 16:42
@Auth ： ghm
@File ：base_utils.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json
import pytest

from common import openexcel
from common import do_contants
from common import do_log
from common import do_config
import warnings

config = do_config.ReadConfig()
