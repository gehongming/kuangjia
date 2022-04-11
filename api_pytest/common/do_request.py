# __author__="G"
#date: 2019/4/11
import jmespath
import requests

from common import log
from common.config import config
from common.context import Context
import pytest

logger = log.get_logger(__name__)


class HttpCookies:

    @staticmethod
    def http_request(case):
        """
        request请求通用模板，可根据实际项目进行调整。verify写死为true了。
        """
        headers = case.get('headers')  # 请求头
        method = case.get('method')  # 请求方法
        data = Context().re_replace(case['data'])  # 请求参数
        url = config.get('api', 'pre_url') + case.get('url')  # url拼接
        logger.info(f"用例--{case['title']}请求url：{url}")
        logger.info(f"用例--{case['title']}请求数据：{data}")
        if not case.get("skip"):
            if method.lower() == 'get':
                resp = requests.get(url=url, params=data, headers=headers, verify=False)
            elif method.lower() == 'post':
                data = eval(data)
                if case["content-type"] == "json":
                    '''json格式'''
                    resp = requests.post(
                        url=url,
                        json=data,
                        headers=headers,
                        verify=True)
                elif case["content-type"] == "form-data":
                    '''form-data格式'''
                    resp = requests.post(
                        url=url,
                        files=data,
                        headers=headers,
                        verify=True)
            else:
                return "Method is not 'GET' or 'POST'"

            par = case.get('jsonpath_exp_save')
            if par:
                if par != None:
                    re_par = Context().re_par(eval(par), resp.json())
                    print(re_par)
        else:
            logger.info("用例跳过")
            response = requests.get(url='http://www.baidu.com')
            return response

    @staticmethod
    def actual_json(actual, jsons):
        """
        actual：列表格式，存放比对的字段key名
        jsons：实际的返回值
        """
        p = []
        for l in actual:
            q = jmespath.search(l, jsons)
            p.append(q)
        return p
    
    @staticmethod
    def assert_res(self, expected, status_code, case, response, excel, row, actual=None):
        """
        断言方法的封装
        """
        if not case.get('skip'):
            if expected.get("json"):
                jsons = expected.get("json")
                actual = HttpCookies.actual_json(actual, response.json())
            else:
                jsons = None
                actual = None
            try:
                assert expected["status_code"] == status_code
                assert jsons == actual
                logger.info("实际结果：{}".format(response.json()))
            except AssertionError as e:
                logger.error(f"用例--{case['title']}--执行未通过")
                logger.info(f"用例--{case['title']}预期结果：{expected}")
                logger.info(f"用例--{case['title']}实际结果：{response.text}")
                logger.exception(e)
                # 结果回写excel中
                excel.write_data(row=row, column=8, value="未通过")
                raise e
            else:
                # 结果回写excel中
                excel.write_data(row=row, column=8, value="通过")
        else:
            excel.write_data(row=row, column=8, value="跳过")

