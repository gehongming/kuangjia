import HTMLTestRunnerNew
import unittest
from api_unittest.testcases import test3_recharge #调用模块
from api_unittest.common import contants

suite=unittest.TestSuite()#创建一个对象
loader=unittest.TestLoader()   #用力的加载器
suite.addTest(loader.loadTestsFromModule(test3_recharge)) #执行用例
with open(contants.reports_html, 'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='20190411py15测试报告',
        description='借口测试报告',
        tester='冥鴻')
    runner.run(suite)
# 执行用例--unittest版本
# with open('test3.txt','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
#     runner.run(suite)