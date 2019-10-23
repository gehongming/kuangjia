from web_pytest.TestDatas.common_datas import base_url

# 正常场景
login_data = {"phone":"17625188013","pwd":"woaini1314"},


test_1_data={"code":"UEPLPQ ","pwd":"woaini@1314","check_success":"加入课堂成功","check_quit":"课程退课成功"}

test_2_data={"check_url":"https://www.ketangpai.com/Letter/index.html","mesage":"测试demo","man":"丢丢"}

test_3_data={"check_url":"https://www.ketangpai.com/Course/Homework/courseid/MDAwMDAwMDAwMLOspd2Gz79r.html",
             "file":"D:\\timg","message":"测试取消"}

login_data1 = [{"phone":"17625188013","pwd":"woaini1314"},
{"phone":"17625188013","pwd":"woaini@1314"}]