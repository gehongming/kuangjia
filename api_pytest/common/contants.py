import os

# 获取当前顶层目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)


# 测试excel
case_file = os.path.join(base_dir, 'data', 'testcase.xlsx')
demo_file = os.path.join(base_dir, 'data', 'testcase_demo.xlsx')
# print(case_file)
# 测试目录
case_dir = os.path.join(base_dir, 'testcases')


# 配置文件目录
config_dir = os.path.join(base_dir, 'config')
# 环境控制器
global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)
# 线上环境配置文件
online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)
# 测试环境配置文件
test_file = os.path.join(base_dir, 'config', 'test.conf')
# print(test_file)


# allure报告
allure_dir = os.path.join(base_dir, 'OutPuts\\allure')
# html报告
htmlreport_dir = os.path.join(base_dir, "Outputs\\reports")
# 日志报告
log_dir = os.path.join(base_dir, 'OutPuts\\log')
