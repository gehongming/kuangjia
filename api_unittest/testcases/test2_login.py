import json
import unittest
from ddt import ddt, data, unpack  # 装饰器
from api_unittest.common import contants
from api_unittest.common import openexcel
from api_unittest.common.http_request import HttpCookies
from api_unittest.common import log
from api_unittest.common.context import Context
import warnings
logger = log.get_logger(__name__)

@ddt
class LoginCase(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'login')
    cases = excel.read()

    def setUp(self):
        logger.info('准备测试前置')
        self.http_request= HttpCookies()
        self.context=Context()
        warnings.simplefilter("ignore", ResourceWarning)

    @data(*cases)
    @unpack
    def test_login(self,url,method,data,expected,case_id,title,result,check_sql):
        logger.info('开始测试：{0}'.format(title))
        data = self.context.replace(json.dumps(data))  #转换成str
        resp=self.http_request.http_request(url,json.loads(data),method)# 实际值 ，data,转换成json
        resp2=json.dumps(resp,ensure_ascii=False) #转换成字符串
        logger.info('请求是:{}'.format(data))
        # print('''用例编号{}，用例标题{}'''.format(case_id,title))
        try:
            self.assertEqual(expected,resp)
            result='PASS'
        except AssertionError as e:
            result = 'FALSE'
            logger.error("报错了，{0}".format(e))
            raise e
        finally:
            logger.info('响应结果是：{}'.format(result))
            self.excel.write(int(case_id) + 1, resp, result)

    def tearDown(self):
        logger.info('测试后置处理')
