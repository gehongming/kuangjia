import  pytest



from web_pytest.PageObjects.ketangpai_login_page import LoginPage as lp
from web_pytest.TestDatas import work_datas as wd



@pytest.mark.usefixtures("open_url1")

class TestLogin:
    @pytest.mark.smoke
    @pytest.mark.usefixtures("refresh")
    @pytest.mark.parametrize("data", wd.login_data1)
    def test_login(self,open_url1,data):
        lp(open_url1[0]).login(data["phone"],data["pwd"])
