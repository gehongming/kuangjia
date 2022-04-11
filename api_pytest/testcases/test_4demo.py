from base_utils import *


@pytest.mark.usefixtures("open_url")
class TestRegister:
    excel = openexcel.DoExcel(do_contants.case_file, 'testcase_demo')
    cases = excel.read()

    @pytest.mark.parametrize("data", cases)
    @pytest.mark.demo
    def test_sendMCode(self,open_url,data):
        # data["url"], data["data"], data["method"], data["expected"], data["case_id"], data["title"], data["result"], data["check_sql"]
        self.resp = open_url[3].http_request(case=data,re_cls=TestRegister)

        status_code = self.resp.status_code

        open_url[3].assert_res(self, data['expected'], status_code, data, self.resp, self.excel, data['case_id']+1, data['actual'])

