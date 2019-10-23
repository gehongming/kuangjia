#__author__="G"
#date: 2019/6/15
from web_unittest.TestDatas.common_datas import base_url

# 正常充值
success_data = {"user":"17625188013","passwd":"12345678qw",
                "money":"100","check":"投标成功！"}


# 充值格式错误-无弹框提示
wrong_datas ={"user":"17625188013","passwd":"12345678qw","money":"12","check":"请输入10的整数倍"}


# 充值金额为空/格式错误-有弹框提示
fail_datas = [
    {"user":"","passwd":"12345678qw", "money":"120","check":"投标金额必须为100的倍数"},
    {"user":"17625188013","passwd":"12345678qw", "money":"10","check":"投标金额必须为100的倍数"},
    {"user":"17625188013","passwd":"12345678qw", "money":"","check":"投标金额必须为100的倍数"}
]