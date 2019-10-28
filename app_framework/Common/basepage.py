#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: basepage
# Author: 简
# Time: 2019/6/18

from app_framework.Common import log

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime
import time

from app_framework.Common.contants import screenshot_dir
logger=log.get_logger(__name__)

class BasePage:

    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图

    def __init__(self,driver):
        self.driver = driver

    def wait_eleVisible(self,loc,img_doc="",timeout=30,frequency=0.5):
        logger.info("等待元素 {} 可见。".format(loc))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
            # 结束等待的时间
            end = datetime.datetime.now()
            logger.info("开始等待时间点：{}，结束等待时间点：{}，等待时长为：{}".
                format(start,end,end-start))
        except:
            # 日志
            logger.exception("等待元素可见失败：")
            # 截图 - 哪一个页面哪一个操作导致的失败。+ 当前时间
            self.save_web_screenshot(img_doc)
            raise
    #获取toast等待用
    def wait_elePresence(self,loc,img_doc="",timeout=30,frequency=0.5):
        logger.info("等待元素 {} 可见。".format(loc))
        try:
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,frequency).until(EC.presence_of_element_located(loc))
            # 结束等待的时间
            end = datetime.datetime.now()
            logger.info("开始等待时间点：{}，结束等待时间点：{}，等待时长为：{}".
                format(start,end,end-start))
        except:
            # 日志
            logger.exception("等待元素可见失败：")
            # 截图 - 哪一个页面哪一个操作导致的失败。+ 当前时间
            self.save_web_screenshot(img_doc)
            raise

    # 查找一个元素
    def get_element(self,loc,img_doc=""):
        """
        :param loc: 元素定位。以元组的形式。(定位类型、定位时间)
        :param img_doc: 截图的说明。例如：登陆页面_输入用户名
        :return: WebElement对象。
        """
        logger.info("查找 {} 中的元素 {} ".format(img_doc,loc))
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            # 日志
            logger.exception("查找元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    def click_element(self,loc,img_doc,timeout=30,frequency=0.5):
        """
        实现了，等待元素可见，找元素，然后再去点击元素。
        :param loc:
        :param img_doc:
        :return:
        """
        # 1、等待元素可见
        self.wait_eleVisible(loc,img_doc,timeout,frequency)
        # 2、找元素
        ele = self.get_element(loc,img_doc)
        # 3、再操作
        logger.info(" 点击元素 {}".format(loc))
        try:
            ele.click()
        except:
            # 日志
            logger.exception("点击元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 文本输入
    def input_text(self,loc,img_doc,*args):
        # 1、等待元素可见
        self.wait_eleVisible(loc,img_doc)
        # 2、找元素
        ele = self.get_element(loc,img_doc)
        # 3、再操作
        logger.info(" 给元素 {} 输入文本内容:{}".format(loc,args))
        try:
            ele.send_keys(*args)
        except:
            # 日志
            logger.exception("元素输入操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的属性值
    def get_element_attribute(self,loc,attr_name,img_doc,timeout=30,frequency=0.5):
        # 等待元素存在 、sleep(1)
        self.wait_elePresence(loc,img_doc,timeout,frequency)
        # time.sleep(0.1)
        # 获取元素
        ele = self.get_element(loc,img_doc)
        # 获取属性
        try:
            attr_value =  ele.get_attribute(attr_name)
            logger.info("获取元素 {} 的属性 {} 值为:{}".format(loc, attr_name,attr_value))
            return attr_value
        except:
            # 日志
            logger.exception("获取元素属性失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的文本值。
    def get_element_text(self,loc,img_doc,timeout=30,frequency=0.5):
        # 等待元素存在 、sleep(1)
        self.wait_elePresence(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        # 获取属性
        try:
            text = ele.text
            logger.info("获取元素 {} 的文件值为:{}".format(loc, text))
            return text
        except:
            # 日志
            logger.exception("获取元素文本值失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise


    # 实现网页截图操作
    def save_web_screenshot(self,img_doc):
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_doc,now)
        try:
            self.driver.save_screenshot(screenshot_dir +"/" + filepath)
            logger.info("网页截图成功。图片存储在：{}".format(screenshot_dir +"/" + filepath))
        except:
            logger.exception("网页截屏失败！")
    #切换app
    def check_app(self,appPackage=None,appActivity=None):
        self.driver.start_activity(appPackage,appActivity)

# 获取窗口的大小
    def get_window(self):
        size = self.driver.get_window_size()
        logger.info("获取窗口大小成功")
        return size

# 上下左右滑动 - up  down  left right
    def swipe(self,fangxiang=None,):
        size=self.get_window()
        self.fangxiang=fangxiang
        if fangxiang =='up': #从下往上
            self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.1)
            logger.info('往上滑动')
        elif fangxiang =='down':#从上往下
            self.driver.swipe(size["width"] * 0.9, size["height"] * 0.1, size["width"] * 0.1, size["height"] * 0.5)
            logger.info('往下滑动')
        elif fangxiang =='left':#从右往左
            logger.info('往左滑动')
            self.driver.swipe(size["width"]*0.9,size["height"]*0.5,size["width"]*0.1,size["height"]*0.5)
        else:#从左往右
            logger.info('往右滑动')
            self.driver.swipe(size["width"]*0.1,size["height"]*0.5,size["width"]*0.9,size["height"]*0.5)
    # toast获取
    def get_toast(self,loc,img_doc,timeout=30,frequency=0.5):
        try:
            self.wait_elePresence(loc,img_doc,timeout,frequency)
            logger.info('toast提示是,{}'.format(self.driver.find_element_by_xpath(loc).text))
            return self.driver.find_element_by_xpath(loc).text
        except:
                logger.exception("没有获取 到toast信息！")
                self.save_web_screenshot(img_doc)

# 切换到webview - context
# 获取当前的contexts

# 获取元素的大小和位置

if __name__ == '__main__':
    BasePage(driver=1).swipe(fangxiang='up')