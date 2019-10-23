

import pytest

from web_pytest.TestDatas import work_datas as ld
from web_pytest.TestDatas import common_datas as cd
from web_pytest.PageObjects.ketangpai_login_page import LoginPage as lp
from web_pytest.PageObjects.ketangpai_homework_page import HomeworkPage as hp
from web_pytest.PageObjects.ketangpai_letter_page import LetterPage as le
from web_pytest.PageObjects.ketangpai_main_page import MainPage as mp

import  time


@pytest.mark.usefixtures("open_url")
@pytest.mark.usefixtures("refresh")
  # 使用函数名称为open_url的fixture
class TestWork:

    #加班退班
    @pytest.mark.demo
    # @pytest.mark.parametrize("data",ld.test_1_data)

    def test_1(self,open_url):
        mp(open_url).join_class(ld.test_1_data["code"])
        assert ld.test_1_data["check_success"] == mp(open_url).get_success_join_message()
        mp(open_url).level_class((ld.test_1_data["pwd"]))
        assert ld.test_1_data["check_quit"] ==mp(open_url).get_success_quit_message()

    @pytest.mark.demo
    def test_2(self,open_url):
        mp(open_url).into_letter()
        assert open_url.current_url == ld.test_2_data["check_url"]
        le(open_url).search_man(ld.test_2_data["man"],ld.test_2_data["mesage"])

    @pytest.mark.demo
    def test_3(self, open_url):
        time.sleep(0.5)
        mp(open_url).into_class()
        time.sleep(0.5)
        assert open_url.current_url == ld.test_3_data["check_url"]
        hp(open_url).input_work(ld.test_3_data["file"],ld.test_3_data["message"])








