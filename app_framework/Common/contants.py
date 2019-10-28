import os

#框架项目顶层目录
# base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(base_dir)

# 获取当前顶层目录
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

#测试数据
testdatas_dir =  os.path.join(base_dir,"TestDatas")

#测试用例
testcases_dir =  os.path.join(base_dir,"TestCases")

#html报告
htmlreport_dir =  os.path.join(base_dir,"Outputs\\reports")

#日志目录
log_dir =  os.path.join(base_dir,"OutPuts\log")
# print(log_dir)

#配置文件层
config_dir =  os.path.join(base_dir,"Config")
# print(config_dir)

#截图目录
screenshot_dir = os.path.join(base_dir,"Outputs\screenshots")
# print(screenshot_dir)

#环境开关
global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)

#线上环境配置
online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)

#测试环境配置
test_file = os.path.join(base_dir, 'config', 'test.conf')

#allure报告
allure_dir=os.path.join(base_dir, 'OutPuts\\allure')
# print(allure_dir)
caps_dir=os.path.join(base_dir,'Desired_Caps','caps.yaml')
# print(caps_dir)