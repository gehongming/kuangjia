import sys

sys.path.append('./')  #获取project 根目录,jenkits执行需要
# print(sys.path)
import HTMLTestRunnerNew
import unittest
from api_unittest.common import contants
import time

discover = unittest.defaultTestLoader.discover(contants.case_dir, pattern='test*.py')
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
with open(contants.reports_html+'/api_{}.html'.format(curTime), 'wb+') as files:
            runner = HTMLTestRunnerNew.HTMLTestRunner(
                stream=files,
                verbosity=1,
                title='20190411py15测试报告',
                description='借口测试报告',
                tester='冥鴻')
            runner.run(discover)




















