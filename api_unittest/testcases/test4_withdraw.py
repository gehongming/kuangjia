import json
import unittest
from ddt import ddt, data, unpack  # 装饰器
from api_unittest.common import openexcel
from api_unittest.common.http_request import HttpSessions
from api_unittest.common import contants
from api_unittest.common import log
import warnings
from api_unittest.common.context import Context
logger=log.get_logger(__name__)
@ddt
class WithDraw(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'withdraw')
    cases = excel.read()
    @classmethod
    def setUpClass(cls):

        cls.http_request= HttpSessions()
        warnings.simplefilter("ignore", ResourceWarning)
        cls.context = Context()
    @data(*cases)
    @unpack
    def test_withdraw(self,url,method,data,expected,case_id,title,result,check_sql):
        data = self.context.replace(json.dumps(data)) #替换data
        logger.info('开始测试：{0}'.format(title))
        logger.info('请求是:{}'.format(data))
        resp=self.http_request.http_request(method,url,json.loads(data))# 实际值 data,转成json格式
        resp2=json.loads(resp)['code']#转换成字符串
        try:
            self.assertEqual(expected,int(resp2))
            result = 'PASS'
        except AssertionError as e:
            result = 'FALSE'
            logger.error("报错了，{0}".format(e))
            raise e
        finally:
            logger.info('响应结果是：{}'.format(result))
            self.excel.write(int(case_id) + 1, resp, result)
    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()