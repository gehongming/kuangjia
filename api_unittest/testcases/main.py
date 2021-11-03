import unittest
from unittestreport import TestRunner

from common.config import *
from common.chose_case import ChoseCase
from common.handle_path import CASE_DIR, REPORT_DIR
from common.send_email import send_email
import sys
sys.path.append('/')

input = sys.argv[-1]
DIR = ChoseCase().chosedir(input)

# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件
loader = unittest.TestLoader()
# suite.addTest(loader.discover(CASE_DIR))
suite.addTest(loader.discover(DIR))

runner = TestRunner(suite,
                    filename=f"clink2_{input}.html",
                    report_dir=REPORT_DIR,
                    title=f'clink2_{input}测试报告',
                    tester='demo',
                    desc=f"clink2_{input}接口测试报告",
                    templates=1)
runner.run()

# 发送钉钉通知
runner.dingtalk_notice(url=config.get('dingding','url'),
                       key=config.get('dingding','key'),
                       secret=config.get('dingding','secret'))

runner.send_email(
    host=config.get('email', 'host'),
    port=465,
    user=config.get('email', 'user'),
    password=config.get('email', 'password'),
    to_addrs=["gehm@ti-net.com.cn"])



# 多线程
# runner.run(thread_count=5)
# 执行测试用例，失败重运行设置为3次，间隔时间为2秒
# runner.rerun_run(count=3, interval=2)





















