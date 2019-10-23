import os

#h获取当前目录
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)


#配置文件目录
config_dir = os.path.join(base_dir,'config')
#环境控制器
global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)
#线上环境配置文件
online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)
#测试环境配置文件
test_file = os.path.join(base_dir, 'config', 'test.conf')
# print(test_file)


#测试excel
case_file=os.path.join(base_dir,'data','testcase.xlsx')
# print(case_file)
#测试目录
case_dir=os.path.join(base_dir,'testcases')
# print(case_dir)


#测试报告txt
reports_text=os.path.join(base_dir,'reports','text3.txt')
# print(reports_text)
#测试报告html
reports_html=os.path.join(base_dir,'reports')
# print(reports_html)
#日志目录
log_dir=os.path.join(base_dir,'log')
# print(log_dir)

