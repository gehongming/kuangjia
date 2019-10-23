import os
#h获取当前目录



base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
#框架项目顶层目录
# base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

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



testdatas_dir =  os.path.join(base_dir,"TestDatas")
testcases_dir =  os.path.join(base_dir,"TestCases")




#测试报告html
reports_html=os.path.join(base_dir,'OutPuts//reports')
# print(reports_html)
#日志目录
log_dir=os.path.join(base_dir,'OutPuts//log')
# print(log_dir)
#截图
screenshot_dir = os.path.join(base_dir,"Outputs//screenshots")
# print(screenshot_dir)




