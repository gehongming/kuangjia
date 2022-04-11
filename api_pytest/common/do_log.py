#__author__="G"
#date: 2019/4/24
import logging
from common import contants
from common.config import config
from common.contants import log_dir
import time


class HandleLogger:
    """处理日志相关的模块"""

    @staticmethod
    def create_logger():
        """
        创建日志收集器
        :return: 日志收集器
        """
        # 第一步：创建一个日志收集器
        log = logging.getLogger("ghm")

        # 第二步：设置收集器收集的等级
        log.setLevel(config.get("log", "level"))

        # 第三步：设置输出渠道以及输出渠道的等级
        curTime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        fh = logging.FileHandler(log_dir + f"/openapi_{curTime}.log", encoding="utf8")
        fh.setLevel(config.get("log", "fh_level"))
        log.addHandler(fh)

        sh = logging.StreamHandler()
        sh.setLevel(config.get("log", "sh_level"))
        log.addHandler(sh)
        # 创建一个输出格式对象
        formats = '%(asctime)s -- [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        form = logging.Formatter(formats)
        # 将输出格式添加到输出渠道
        fh.setFormatter(form)
        sh.setFormatter(form)

        return log


log = HandleLogger.create_logger()