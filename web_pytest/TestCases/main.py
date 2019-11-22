import pytest
import os
import sys
sys.path.append('./')  #获取project 根目录,jenkits执行需要
# pytest.main(["-v","-m","login"])
#
# pytest.main(["-v","-m","demo","--reruns","1","--alluredir=../OutPuts/allure-results"])
# os.system(r"allure generate --clean ../OutPuts/allure-results -o ../allure-report ")

pytest.main(["-v","-m","smoke","--alluredir=../OutPuts/allure-results"])
os.system(r"allure generate --clean ../OutPuts/allure-results -o ../allure-report ")

