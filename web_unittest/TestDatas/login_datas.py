from web_unittest.TestDatas.common_datas import base_url

# 正常场景
success_data = {"user":"17625188013","passwd":"12345678qw",
                "check":"{}/Index/index".format(base_url)}


# 密码为空/用户名为空/用户名格式不正确
wrong_datas = [
    {"user":"17625188013","passwd":"","check":"请输入密码"},
    {"user":"","passwd":"12345678qw","check":"请输入手机号"},
    {"user":"1762","passwd":"12345678qw","check":"请输入正确的手机号"},
    {"user":"176251880133","passwd":"12345678qw","check":"请输入正确的手机号"}
]

# 用户名未注册 /密码错误
fail_datas = [
    {"user":"17777777713","passwd":"pthon","check":"此账号没有经过授权，请联系管理员!"},
    {"user":"17625188013","passwd":"pthon111","check":"帐号或密码错误!"}]