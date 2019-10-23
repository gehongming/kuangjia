import json
import unittest
from ddt import ddt, data, unpack  # 装饰器
from api_unittest.common import do_mysql
from api_unittest.common import openexcel
from api_unittest.common.http_request import HttpCookies
from api_unittest.common.context import Context
from api_unittest.common import contants
from api_unittest.common import log
import warnings
logger = log.get_logger(__name__)


@ddt
class RegisterCase(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'register')
    cases = excel.read()


    def setUp(self):
        logger.info('准备测试前置')
        self.http_request= HttpCookies()
        self.mysql= do_mysql.DoMysql()
        self.context = Context()
        warnings.simplefilter("ignore", ResourceWarning)
    @data(*cases)
    @unpack
    def test_register(self,url,method,data,expected,case_id,title,result,check_sql):
        logger.info('开始测试：{}'.format(title))
        logger.info('请求是:{}'.format(data))
        if data['mobilephone']=='register_mobile':
            sql = 'select max(mobilephone) from future.member'
            max_phone = self.mysql.fetch_one(sql)[0]  # 查询最大手机号码
            max_phone=int(max_phone)+1
            data['mobilephone']=max_phone
            print(data['mobilephone'])
        resp=self.http_request.http_request(url,data,method)# 实际值
        resp2=json.dumps(resp,ensure_ascii=False) #转换成字符串
        try:
            self.assertEqual(expected,resp)
            result = 'PASS'
            if check_sql is not None:
                sql = eval(check_sql)['sql1']
                mobilephone = self.mysql.fetch_one(sql)
                print(mobilephone['mobilephone'])
                after = mobilephone['mobilephone']
                self.assertEqual(data['mobilephone'], after)
        except AssertionError as e:
            result = 'FALSE'
            logger.error("报错了，{0}".format(e))
            raise e
        finally:
           logger.info('响应结果是：{}'.format(result))
           self.excel.write(int(case_id) + 1, resp, result)
           logger.info('结束测试：{0}'.format(title))


        def tearDown(self):
            self.mysql.close()

