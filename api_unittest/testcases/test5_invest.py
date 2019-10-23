import json
import unittest

from ddt import ddt, data, unpack  # 装饰器
from api_unittest.common import contants
from api_unittest.common import openexcel
from api_unittest.common.http_request import HttpSessions
from api_unittest.common.context import Context
from api_unittest.common import  log
from api_unittest.common.do_mysql import DoMysql
import warnings

logger=log.get_logger(__name__)

@ddt
class InvestCase(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'invest')
    cases = excel.read()
    @classmethod
    def setUpClass(cls):
        cls.http_request= HttpSessions()
        logger.info('准备测试前置')
        cls.context=Context()
        cls.mysql=DoMysql()
        warnings.simplefilter("ignore", ResourceWarning)


    @data(*cases)
    @unpack
    def test_invest(self,url,method,data,expected,case_id,title,result,check_sql):
        data = self.context.replace(json.dumps(data))
        logger.info('用例标题是:{}'.format(title))
        logger.info('请求是:{}'.format(data))
        if title=='投资人正常投资' and check_sql is not None:
            sql = eval(check_sql)['sql1']
            member = self.mysql.fetch_one(sql)
            print(member['leaveamount'])
            before = member['leaveamount']
            print(before)
        resp=self.http_request.http_request(method,url,json.loads(data))# 实际值
        resp2=json.loads(resp)['code']#转换成字符串
        resp3=json.loads(resp)['msg']
        try:
            self.assertEqual(expected,int(resp2))
            result = 'PASS'
            if resp3 == "加标成功" and check_sql is not None:
                sql = eval(check_sql)['sql2']
                loan_id = self.mysql.fetch_one(sql)['id']
                print('标的ID：', loan_id)
                # 保存到类属性里面
                setattr(Context, "loan_id", str(loan_id))
            if resp3 == "竞标成功" and check_sql is not None:
                sql = eval(check_sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print(member['leaveamount'])
                after = member['leaveamount']#剩余金额
                print(after)
                recharge_amount = int(json.loads(data)['amount'])  # 竞标金额
                print(recharge_amount)
                self.assertEqual(before , after)
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