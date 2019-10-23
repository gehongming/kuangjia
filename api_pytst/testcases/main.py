import pytest

pytest.main(["-v","-s","-m","smoke","--alluredir=../OutPuts/allure"])


#allure serve 报告绝对路径
# eval("allure serve F:\\框架\\api_pytst\\allure-report")