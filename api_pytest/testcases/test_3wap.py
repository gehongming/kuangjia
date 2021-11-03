import json
import pytest
import allure
from common.context import Context
from common import contants
from common import log
from common import do_yaml
import time
import warnings
logger = log.get_logger(__name__)


@allure.feature('B2C每日用例-wap')
@pytest.mark.usefixtures("open_url")
class TestMday:
    yaml = do_yaml.DoYaml(contants.case_file + '\\wap_day.yaml')
    cases = yaml.read_yaml()

    @pytest.mark.parametrize("data", cases)
    @pytest.mark.wap
    @allure.story('日常用例')
    def test_wap(self, open_url, data):
        # 每日用例的其中之一

        allure.dynamic.title(data["title"])

        # 更新data变量
        data["data"] = Context().re_replace(data["data"])  # 转换后是str需要转换成原本的格式
        # 先获取发送前验证码
        # if data['case_id'] == 1:
        #     data["check_sql"]["sql_1"] = Context().re_replace(data["check_sql"]["sql_1"])
        #     SMS = open_url[1].fetch_one_dict(data["check_sql"]["sql_1"])['VFCode']
        # else:
        #         pass
        # 发送请求
        resp = open_url.http_request(
            data["url"],
            eval(
                data["data"]),
            data["method"],
            headers=data["headers"])
        # resp = open_url[0].http_request(data["url"], eval(data["data"]), data["method"], headers=data["headers"])

        logger.info('开始测试：{}'.format(data["title"]))
        logger.info('请求数据是:{}'.format(data["data"]))
        logger.info('请求url是:{}'.format(data["url"]))

        try:
            if data['case_id'] in (1, 8, 9, 10, 14, 15):
                text = json.loads(resp.text)
                assert text['ErrorMessage'] == data['expected']
                # if data['case_id']==1:
                #     setattr(Context, "mark", text["Data"]["Mark"])
                # time.sleep(30)
                # SMS2 = open_url[1].fetch_one_dict(data["check_sql"]["sql_1"])['VFCode']
                # setattr(Context, "SMS", SMS2)
                # assert SMS!=SMS2
                if data['case_id'] in (10, 15):
                    setattr(
                        Context, 'order_code', json.loads(
                            resp.text)['Data']['OrderCode'])
                else:
                    pass
                text = text['ErrorMessage']
                result = 'Pass'
                self.yaml.write_yaml(data['case_id'], 'result', result)
            if data['case_id'] in (2, 3):
                text = json.loads(resp.text)
                if 'username' in text['data']:
                    assert text['data']['username'] == data['expected']
                    setattr(Context, "user_id", text['data']['userid'])
                    text = text['data']['username']
                    result = 'Pass'
                    self.yaml.write_yaml(data['case_id'], 'result', result)
                else:
                    assert True == False
            if data['case_id'] in (4, 7, 13):
                text = resp.status_code
                assert text == data['expected']
                if data['case_id'] in (7, 13):
                    setattr(
                        Context, 'cart_id', json.loads(
                            resp.text)['group'][0]['product'][0]['cartid'])
                result = 'Pass'
                self.yaml.write_yaml(data['case_id'], 'result', result)
            if data['case_id'] in (5, 6, 12):
                text = json.loads(resp.text)
                assert text['Data']['Reminder'] == data['expected']
                text = text['Data']['Reminder']
                result = 'Pass'
                self.yaml.write_yaml(data['case_id'], 'result', result)

            if data['case_id'] in (11, 16):
                text = json.loads(resp.text)['error_message']
                assert text == data['expected']
                result = 'Pass'
                self.yaml.write_yaml(data['case_id'], 'result', result)
        except AssertionError as e:
            result = 'FALSE'
            logger.error("报错了，{0}".format(e))
            self.yaml.write_yaml(data['case_id'], 'result', result)
            raise e
        finally:
            logger.info('响应结果是：{}'.format(text))
            logger.info('测试结果是：{}'.format(result))
            self.yaml.write_yaml(data['case_id'], 'actual', text)
            logger.info('结束测试：{}'.format(data["title"]))
