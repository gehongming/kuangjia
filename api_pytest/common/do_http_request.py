# __author__="G"
# date: 2019/4/11
from requests import request
import requests
import pytest
import json
import time
import jmespath
from common.do_config import *
from common.do_create_data import EnvData
from common.do_context import Context
from common.do_log import log
config = ReadConfig()

headrs = {}


class HttpCookies:

    @staticmethod
    def http_request(case, re_cls=EnvData):

        if not case.get("skip"):
            time.sleep(int(case.get('sleep'))) if case.get('sleep') else time.sleep(0)
            if case.get('data'):
                data = json.loads(Context().re_replace(case["data"]))
                log.info(f"用例--{case['title']}请求数据：{data}")
            else:
                data = None
                log.info(f"用例--{case['title']}请求数据：为空")
            # 获取用例中的请求方法、平台
            method = case["method"]
            target = case['target'].lower()
            # 根据客户端不同 获取不同的cookies, url
            cookies = Context().re_replace({"Cookie": f"#{target}_cookie#"})
            cookies = json.loads(cookies.replace("'", '"'))

            url = Context().re_replace(case["interface"])
            # 配置文件还要改
            url = config.get('env', f"base_{target}_url") + url

            log.info(f"用例--{case['title']}---请求url：{url}")
            # 请求方法。
            if method.lower() in ['get', 'delete']:
                resp = request(method=method, url=url, cookies=cookies, verify=False)
            elif method.lower() in ['post', 'put']:
                if case["content-type"] == "json":
                    resp = request(method=method, url=url, json=data, cookies=cookies, verify=False)
                else:
                    resp = request(method=method, url=url, data=data, cookies=cookies, verify=False)
            else:
                return "Method is not [get, delete, post, put]"
            par = case.get('jsonpath_exp_save')
            if par:
                re_par = EnvData().re_par_new(eval(par), resp.json(), re_cls=re_cls)
                print(re_par)
            return resp
        else:
            log.info("用例跳过")
            response = request(method='post', url='http://www.baidu.com')
            return response

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
                assert jsons == actual  # 可参考unittest继续增加类型选择。暂时就不先加了
                log.info(f"用例--{case['title']}--执行通过")
            except AssertionError as e:
                log.error(f"用例--{case['title']}--执行未通过")
                log.exception(e)
                # 结果回写excel中
                # excel.write_data(row=row, column=8, value="未通过")
                raise e
            log.info(f"用例--{case['title']}--预期结果：{expected}")
            log.info(f"用例--{case['title']}--实际结果：{response.text}")
        #     else:
        #         # 结果回写excel中
        #         # excel.write_data(row=row, column=8, value="通过")
        else:
            log.info(f"用例--{case['title']}--用例跳过")

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
