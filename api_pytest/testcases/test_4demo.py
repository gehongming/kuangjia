import json
import os

import pytest
import allure
import time
import warnings

from common.context import Context
from common.contants import *
from common import log
from common.do_excel import HandleExcel

logger = log.get_logger(__name__)


@allure.feature('B2C每日用例-wap')
@pytest.mark.usefixtures("open_url")
class TestDemo:
    sheet_name = "demo"
    filename = demo_file
    excel = HandleExcel(filename,sheet_name)
    cases = excel.read_data()

    @pytest.mark.parametrize("data", cases)
    @pytest.mark.wap
    @allure.story('日常用例')
    def test_wap(self, open_url, data):

        allure.dynamic.title(data["title"])
        expected = eval(data["expected"])
        row = data["case_id"] + 1
        actual = data.get("actual")
        resp = open_url[0].http_request(data)
        status_code = resp.status_code

        open_url[0].assert_res(self, expected, status_code, data, self.resp, self.excel, row, actual)

        logger.info('结束测试：{}'.format(data["title"]))
