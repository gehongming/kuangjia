#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/7/14 17:05
# @Author : ASUS
# @File : XIAOMING.py
# @Software: PyCharm Community Edition



class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 'weight'

    def talk(self):
        print("person is talking....")


class Chinese(Person):
    def __init__(self, name, age, language):
        Person.__init__(self, name, age)
        self.language = language
        print(self.name, self.age, self.weight, self.language)

    def talk(self):  # 子类 重构方法
        print('%s is speaking chinese' % self.name)

    def walk(self):
        print('is walking...')


c = Chinese('bigberg', 22, 'Chinese')
c.talk()