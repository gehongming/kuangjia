#__author__="G"
#date: 2019/4/24
import logging
from common import contants
from common.config import config
import time

    # 新建一个日志收集器：getLogger() 新建一个收集器
def get_logger(name):
    logger=logging.getLogger(name)  # 名为case_log的日志收集器
    logger.setLevel(config.get('log_info','collect_level'))  # 设定收集的级别
    #指定格式
    formatter = logging.Formatter(config.get('log_info','log_famtter'))
    # 新建指定的输出渠道：
    # 指定输出渠道 handler
    console_handler = logging.StreamHandler()  # 指定输出到console控制台
    console_handler.setLevel(config.get('log_info','output_level'))  # 设定输出信息的级别
    console_handler.setFormatter(formatter)
    # 指定输出文本渠道 handler
    curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
    file_handler = logging.FileHandler(contants.log_dir+"/Web_Autotest_{0}.log".format(curTime),encoding='utf-8')
    file_handler.setLevel(config.get('log_info','output_level')) # 设定输出信息的级别
    file_handler.setFormatter(formatter)
    # 配合关系
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # 收集日志
    return logger
if __name__ == '__main__':

    logger = get_logger(__name__)
    logger.info('测试开始啦')
    logger.error('测试报错')
    logger.debug('测试数据')
    logger.info('测试结束')
