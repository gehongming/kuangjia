#__author__="G"
#date: 2019/11/14

from common import contants
import os
import allure
from common.file import *

Filelist = get_filelist(contants.reports_screen)
with open(Filelist[0], "rb") as f:
                    context = f.read()
                    allure.attach(context, "错误图片", attachment_type=allure.attachment_type.PNG)