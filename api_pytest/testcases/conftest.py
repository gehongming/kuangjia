import pytest
import os
import warnings

from api_pytst.common import do_mysql
from api_pytst.common import openexcel
from api_pytst.common.webservice_request import WebService
from api_pytst.common.context import Context
from api_pytst.common import contants
from api_pytst.common import log

logger = log.get_logger(__name__)
from api_pytst.common import contants



# 删除指定目录下的文件
def remove_files_in_dir(dir):
    files = os.listdir(dir)
    for item in files:
        c_path = os.path.join(dir,item)
        if os.path.isdir(c_path):
            remove_files_in_dir(c_path)
        else:
            os.remove(c_path)

# session级别的
@pytest.fixture(scope="session",autouse=True)
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    # 清除allure测试报告
    remove_files_in_dir(contants.allure_dir)
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")

@pytest.fixture(scope="class")
def open_url():
    # 前置
    http_request = WebService()
    mysql = do_mysql.DoMysql()
    context = Context()
    warnings.simplefilter("ignore", ResourceWarning)
    yield  (http_request,mysql,context) # yield之前代码是前置，之后的代码就是后置。
    # 后置
    mysql.close()









