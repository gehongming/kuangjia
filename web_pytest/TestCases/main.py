import pytest
import os
# pytest.main(["-v","-m","login"])

pytest.main(["-v","-m","demo","--alluredir=../OutPuts/allure-results"])
os.system(r"allure generate --clean ../OutPuts/allure-results -o ../allure-report ")



