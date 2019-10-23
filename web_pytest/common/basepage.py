
from web_unittest.common import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time
import win32gui
import win32con
from web_unittest.common.contants import screenshot_dir
from selenium.webdriver.support.select import Select
logger=log.get_logger(__name__)

class BasePage:

    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图

    def __init__(self,driver):
        self.driver = driver
    #等待元素可见
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
    #点击元素
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
    def get_element_attribute(self,loc,attr_name,img_doc):
        self.wait_eleVisible(loc, img_doc)
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
    def get_element_text(self,loc,img_doc):
        self.wait_eleVisible(loc,img_doc)
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


    # windows切换
    def check_window(self,loc,img_doc):
        '''
        点击会出现新窗口的操作，并切换到新窗口
        :param loc: 操作后会出新新窗口的操作
        :param img_loc: 记录动作
        :return:
        '''
        logger.info("点击{}元素，出现{}弹框".format(loc,img_doc))
        logger.info("获取窗口数。")
        self.click_element(loc,img_doc)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        time.sleep(0.5)
    # iframe切换
    def check_iframe(self,loc,webelement,img_doc):
        """
                       实现了，操作。等待ifram弹框出现。进入下拉框
                       :param loc:操作后会出现弹框的动作
                       :param webelement：ifram对象
                       :return:
                      """
        logger.info("点击{}元素，出现{}弹框".format(loc,img_doc))
        # self.wait_eleVisible(loc)
        self.click_element(loc,img_doc)
        #等待下拉框出现
        try:
            WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(webelement))
        except:
            logger.exception("弹框未出现")
            raise

    # select下拉列表
    def select(self,loc,value,img_doc):
        """
               实现了，等待下拉框可见，找下拉框值，然后再去点击值。
               :param loc:
               :param value: value属性值
               :return:
               """
        logger.info("下拉列表{}点击选项{}".format(img_doc,value))
        self.wait_eleVisible(loc)
        self.click_element(loc)
        try:
            s = Select(self.get_element(loc))
        except:
            logger.exception("下拉框未出现")
            raise
        time.sleep(2)
        s.select_by_value(value)
    # 上传操作 -
    def upload(self,filePath,img_doc,browser_type="chrome"):
        try:
            logger.info("上传文件路径".format(filePath))
            if browser_type == "chrome":
                title = "打开"
            else:
                title = ""
            # 找元素
            # 一级窗口"#32770","打开"
            dialog = win32gui.FindWindow("#32770", title)
            #
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
            comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
            # 编辑按钮
            edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
            # 打开按钮
            button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 四级

            # 往编辑当中，输入文件路径 。
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
        except:
            logger.exception("上传文件失败")
            self.save_web_screenshot(img_doc)
            raise