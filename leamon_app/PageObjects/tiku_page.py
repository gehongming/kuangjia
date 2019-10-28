#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2019/3/18 17:28

from Common.basepage import BasePage
from PageLocators.tikuPage_locator import TikuPageLocator as loc
import time
import random

class TikuPage(BasePage):

    tiku_types_list = []

    #获取所有的题库类型
    def get_all_tiku_type_names(self):
        #等待题库元素可见
        self.wait_ele_visible(loc.titu_type_loc,"题库列表页面_等待题库列表可见")
        time.sleep(1)
        #获取两屏的内容，然后相同的类型要去重。
        #滚动之前，获取一次pagesource.
        old_page_source = ""
        new_page_source = self.driver.page_source
        #向上滑动，50% 。再获取一次新的pagesource。如果新旧不相等。
        # 继续向上滑动。重复操作，直到新旧的pagesource一模一样。
        while(old_page_source != new_page_source):
            self.__get_curPage_tiku_types() # 获取当前页面，所有题库类型
            self.swipe_by_direction("up") # 向上滑动
            old_page_source = new_page_source
            new_page_source = self.driver.page_source  # 更新当前页面源码
        print(self.tiku_types_list)


    #选择题库类型
    def select_tiku_type_by_name(self,tiku_type_name):
        """
        :param tiku_type_name: 题库类型名称。app页面上的题库名称
        :return:
        """
        #元素定位替换
        tiku_title_loc = (loc.tiku_title_loc[0],loc.tiku_title_loc[1].format(tiku_type_name))
        #点击对应的题库，进入题库。若题库类型不在当前页面，需要滚动操作。
        self.click_element(tiku_title_loc,"题库列表页面_点击题库类型进入题目难度页面")

    #选择题目难度等级
    def select_topic_level(self,level_name):
        """
        :param level_name:初级、中级、高级
        :return:None
        """
        self.wait_ele_visible(loc.firstLevel_loc,"题目难度页面_等待难度级别出现")
        if level_name == "初级":
            self.click_element(loc.firstLevel_loc,"题目难度页面_选择初级难度")
        elif level_name == "中级":
            self.click_element(loc.secondLevel_loc,"题目难度页面_选择中级难度")
        elif level_name == "高级":
            self.click_element(loc.thirdLevel_loc,"题目难度页面_选择高级难度")

    #随机选择套题
    def select_topic_suite_by_random(self):
        self.wait_ele_visible(loc.suite_title_loc,"套题页面_等待套题元素出现")
        time.sleep(0.5)
        # 获取当前所有的套题数
        suites = self.get_element(loc.suite_title_loc,"套题页面_获取当前页面所有套题",find_all=True)
        index = random.randint(0,len(suites)-1)
        #随便选择一套并点击
        suites[index].click()

    #收藏开关操作
    def switch_favirate(self,action=True):
        pass

    #答案开关操作
    def switch_answer(self,action=True):
        pass

    #拖拽
    def drag_answer(self,x=None,y=None):
        pass


    #获取当前页面的题库类型
    def __get_curPage_tiku_types(self):
        # 根据id得到所有元素
        self.wait_ele_visible(loc.titu_type_loc,"题库列表页面_等待题库列表可见")
        time.sleep(0.5)
        type_eles = self.get_element(loc.titu_type_loc,"题库列表页面_获取当前页面所有题库类型",find_all=True)
        # 根据元素得到它的text值
        # 将所有的text放在列表当中，再返回。(去重)
        for ele in type_eles:
            if ele.text not in self.tiku_types_list:
                self.tiku_types_list.append(ele.text)


