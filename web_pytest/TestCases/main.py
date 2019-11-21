import pytest
import os
# pytest.main(["-v","-m","login"])
#
# pytest.main(["-v","-m","demo","--reruns","1","--alluredir=../OutPuts/allure-results"])
# os.system(r"allure generate --clean ../OutPuts/allure-results -o ../allure-report ")

pytest.main(["-v","-m","smoke","--alluredir=../OutPuts/allure-results"])
os.system(r"allure generate --clean ../OutPuts/allure-results -o ../allure-report ")

