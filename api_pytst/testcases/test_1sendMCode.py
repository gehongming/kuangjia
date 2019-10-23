import json
import pytest

from api_pytst.common import openexcel
from api_pytst.common import contants
from api_pytst.common import log
import warnings
logger = log.get_logger(__name__)



@pytest.mark.usefixtures("open_url")
class TestRegister:
    excel = openexcel.DoExcel(contants.case_file, 'sendMCode')
    cases = excel.read()

    @pytest.mark.parametrize("data", cases)
    @pytest.mark.demo
    def test_sendMCode(self,open_url,data):
        #data["url"], data["data"], data["method"], data["expected"], data["case_id"], data["title"], data["result"], data["check_sql"]
        logger.info('开始测试：{}'.format(data["title"]))
        logger.info('请求数据是:{}'.format(data["data"]))

        resp=open_url[0].webservice(data["url"],data["data"],data["method"])# 实际值
        # resp2=json.dumps(resp,ensure_ascii=False) #转换成字符串
        try:
            # self.assertIn(data["expected"],resp)
            assert data["expected"] in resp
            result = 'PASS'
            if data["check_sql"] is not None:
                sql = eval(data["check_sql"])['sql1']
                Fverify_code = open_url[1].fetch_one(sql)
                logger.info('验证码是：{}'.format(Fverify_code[2]))
        except AssertionError as e:
            result = 'FALSE'
            logger.error("报错了，{0}".format(e))
            raise e
        finally:
           logger.info('响应结果是：{}'.format(data["result"]))
           self.excel.write(int(data["case_id"]) + 1, str(resp), result)
           logger.info('结束测试：{0}'.format(data["title"]))


