import json
import pytest

from api_pytst.common import openexcel
from api_pytst.common import context
from api_pytst.common.context import Context
from api_pytst.common import contants
from api_pytst.common import log
from api_pytst.common import create_data
import warnings
warnings.simplefilter("ignore", ResourceWarning)

logger = log.get_logger(__name__)

@pytest.mark.usefixtures("open_url")
class TestRegisterCase:
    excel = openexcel.DoExcel(contants.case_file, 'register')
    cases = excel.read()

    @pytest.mark.parametrize("data", cases)
    @pytest.mark.smoke
    def test_register(self,open_url,data):
        # data["url"], data["data"], data["method"], data["expected"], data["case_id"], data["title"], data["result"], data["check_sql"]
        data["data"] = Context().re_replace(data["data"]) #正则替换 千万不能少
        logger.info('开始测试第{}条：{}'.format(data["case_id"], data["title"]))
        if data["case_id"]==1:
            new_phone= create_data.create_phone()
            logger.info('手机号是：{}'.format(new_phone))
            data["data"] = context.replace(data["data"],'register_phone', str(new_phone))
            setattr(Context, "register_phone", str(new_phone))

        new_ip = create_data.create_ip()
        logger.info('IP是:{}'.format(new_ip))
        data["data"]=context.replace(data["data"],'random_ip', str(new_ip))
        if data["data"].find('user_name')>-1: #找到username
            if data["check_sql"]:
                sql=eval(data["check_sql"])['sql1']

                user_name=create_data.create_name()
                logger.info('uesename是{}'.format(user_name))
                all_user=open_url[1].fetch_all(sql)
                while True:
                    if (user_name,) in all_user:
                        user_name =create_data.create_name()
                        continue #防止名字与数据库数据重复
                    else:
                        break
                data["data"]=context.replace(data["data"],'user_name',str(user_name))
            logger.info('请求数据是:{}'.format(data["data"]))
        #验证码超时
        if data["data"].find('chaoshi') >-1:
            sql = eval(data["check_sql"])['sql1']
            chaoshi_code = open_url[1].fetch_one_dict(sql)['Fverify_code']
            chaoshi_phone = open_url[1].fetch_one_dict(sql)['Fmobile_no']
            data["data"] = data["data"].replace('chaoshi_code', str(chaoshi_code))
            data["data"] = data["data"].replace('chaoshi_phone', str(chaoshi_phone))
            logger.info('请求数据是:{}'.format(data))


        logger.info('请求是:{}'.format(data))
        resp=open_url[0].webservice(data["url"],data["data"],data["method"])# 实际值
        logger.info('实际值:{}'.format(resp))

        try:
            if data["title"] =='成功发送短信验证码':
                sql=eval(data["check_sql"])['sql1']

                logger.info('执行sql语句:{}'.format(sql))
                verify_code = open_url[1].fetch_one_dict(sql)['Fverify_code']
                logger.info('验证码:{}'.format(verify_code))
                setattr(context.Context, "verify_code", str(verify_code))


            if data["title"]=='注册成功':
                sql=eval(data["check_sql"])['sql2']
                sql=context.replace(sql,"username",str(user_name))
                logger.info('执行的sql{}'.format(sql))

                sql_res=open_url[1].fetch_all(sql)
                len_res=len(sql_res)
                logger.info('sql执行结果:{}'.format(sql_res))
                assert len_res == 1

            assert data["expected"] ==resp
            result = 'Pass'
        except AssertionError as e:
            result = 'False'
            logger.error("报错了，{0}".format(e))
            raise e
        finally:
           logger.info('响应结果是：{}'.format(result))
           self.excel.write(int(data["case_id"]) + 1, str(resp), result)
           logger.info('结束测试：{0}'.format(data["title"]))

