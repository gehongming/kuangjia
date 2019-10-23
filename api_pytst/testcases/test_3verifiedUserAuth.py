import json
import unittest
from ddt import ddt, data, unpack  # 装饰器
from api_pytst.common import do_mysql
from api_pytst.common import openexcel
from api_pytst.common.webservice_request import WebService
from api_pytst.common import context
from api_pytst.common.context import Context
from api_pytst.common import contants
from api_pytst.common import log
import warnings
from api_pytst.common import create_data
logger = log.get_logger(__name__)
@ddt
class RegisterCase(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'verifiedUserAuth')
    cases = excel.read()
    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request= WebService()
        cls.mysql= do_mysql.DoMysql()
        warnings.simplefilter("ignore", ResourceWarning)
    @data(*cases)
    @unpack
    def test_register(self,url,data,method,expected,case_id,title,result,check_sql):
        data = Context().re_replace(data) #正则替换 千万不能少
        print(data)
        logger.info('开始测试第{}条：{}'.format(case_id, title))

        new_ip = create_data.create_ip()
        logger.info('IP是:{}'.format(new_ip))
        data = context.replace(data, 'random_ip', str(new_ip))

        true_user = create_data.create_name()
        logger.info("随机姓名是：{}".format(true_user))
        data = context.replace(data, 'true_user', str(true_user))

        user_cre_id = create_data.generator()
        logger.info("身份证是：{}".format(user_cre_id))
        data = context.replace(data, 'user_cre_id', str(user_cre_id))
        if case_id==1:
            new_phone= create_data.create_phone()
            logger.info('手机号是：{}'.format(new_phone))
            data = context.replace(data,'register_phone', str(new_phone))
            setattr(Context, "register_phone", str(new_phone))
            # print(context.Context.register_phone)
        if data.find('user_name')>-1: #找到username
            if check_sql:
                sql=eval(check_sql)['sql1']
                user_name=create_data.create_name()
                logger.info('uesename是{}'.format(user_name))
                all_user=self.mysql.fetch_all(sql)
                while True:
                    if (user_name,) in all_user:
                        user_name =create_data.create_name()

                        continue #防止名字与数据库数据重复
                    else:
                        break
                data=context.replace(data,'user_name',str(user_name))
        logger.info('请求数据是:{}'.format(data))
        resp=self.http_request.webservice(url,data,method)# 实际值

        try:
            if title =='成功发送短信验证码':
                sql=eval(check_sql)['sql1']
                logger.info('执行sql语句:{}'.format(sql))

                verify_code = self.mysql.fetch_one_dict(sql)['Fverify_code']
                logger.info('验证码:{}'.format(verify_code))
                setattr(Context, "verify_code", str(verify_code))
                # print(context.Context.verify_code)

            if title == '注册成功':
                sql=eval(check_sql)['sql2']
                sql=context.replace(sql,"user_name",str(user_name))
                logger.info('执行的sql{}'.format(sql))

                sql_res=self.mysql.fetch_one_dict(sql)
                Fuid=sql_res['Fuid']
                logger.info('sql执行结果Fuid:{}'.format(Fuid))
                setattr(Context,"Fuid",str(Fuid))
            if title == '实名认证成功':
                sql=eval(check_sql)['sql1']
                sql=Context().re_replace(sql)
                logger.info('sql执行语句是:{}'.format(sql))

                sql_res=self.mysql.fetch_all(sql)
                len_res=len(sql_res)
                logger.info('sql执行结果:{}'.format(sql_res))
                self.assertEqual(len_res, 1)
            self.assertEqual(expected,resp)
            result = 'Pass'
        except AssertionError as e:
            result = 'False'
            logger.error("报错了，{0}".format(e))
            raise e
        finally:
           logger.info('响应结果是：{}'.format(result))
           self.excel.write(int(case_id) + 1, str(resp), result)
           logger.info('结束测试：{0}'.format(title))
    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()