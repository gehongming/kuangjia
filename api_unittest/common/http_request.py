#__author__="G"
#date: 2019/4/11
import requests

from api_unittest.common.config import config


class HttpCookies:
    def http_request(self,url,data,method,cookies=None,json=None,headers=None,verify=None):
        '''
        :param url: 地址
        :param data: 数据
        :param method: 请求方式
        :param cookies:
        :param json: 为json格式的时候为True
        :param headers: 请求头字典格式
        :param verify: https格式时为False
        :return:
            url = 'https://api.yjq.com/account/anyms/send-vfcode'
            main = {"phone":"17625188013"}
            heardes={"Content-Type": "application/json","sign":"1234"}
            b=HttpsCookies().https_request(url,main,method='post',json=True,headers=heardes)
            print(b)
        '''
        url=config.get('api','pre_url')+url #url拼接
        if method.lower()=='get':
            resp=requests.get(url=url,params=data,cookies=cookies,headers=headers,verify=verify)
        elif method.lower()=='post':
            if json:
               resp=requests.post(url=url,json=data,cookies=cookies,headers=headers,verify=verify)
            else:
               resp=requests.post(url=url,data=data,cookies=cookies,headers=headers,verify=verify)
        # print ('''响应报文:{}
        # 响应头:{}
        # 状态码:{}
        # 响应cookie:{}
        # 请求cookies:{}'''
        # .format(resp.text
        #         ,resp.headers,resp.status_code,resp.cookies,resp.request._cookies))
        return (resp.text)


class HttpSessions:
    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def http_request(self, method, url, data=None, json=None,headers=None,verify=None):
        url = config.get('api', 'pre_url') + url
        if method.lower() == 'get':
            resp = self.session.request(method=method, url=url, params=data,headers=headers,verify=verify)
        elif method.lower() == 'post':
            if json:
                resp = self.session.request(method=method, url=url, json=data,headers=headers,verify=verify)
            else:
                resp = self.session.request(method=method, url=url, data=data,hheaders=headers,verify=verify)
        else:
            print('UN-support method')
        return (resp.text)
        # print('''响应报文:{}
        # 响应头:{
        # 状态码:{}
        # 响应cookie:{}
        # 请求cookies:{}'''
        #       .format(resp.text
        #               , resp.headers, resp.status_code, resp.cookies, resp.request._cookies))
    def close(self):
        self.session.close()

if __name__=='__main__':
#注册
  # url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
  # main = {'mobilephone': '17625188012', 'pwd': '1234561234561234561'}
  # G=HttpCookies()
  # G.http_request(url,main,'GET')
  # print(G)
  # # 登录
  # url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
  # main = {'mobilephone': '', 'pwd': ''}
  # # G=HttpCookies()
  # b=HttpCookies().http_request(url,main,'post')
  # print(b)
  #
  # #充值
  # main = {"mobilephone": "18861342700", "amount": "1000"}
  # url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
  # G=HttpCookies()
  # c=G.http_request(url,main,'post',b)
  # print(c)
  # #提现
  # main = {"mobilephone": "18861342700", "amount": "1000"}
  # url='http://test.lemonban.com/futureloan/mvc/api/member/withdraw'
  # G=HttpCookies()
  # d=G.http_request(url,main,'post')
  # print(d)
    url = 'http://120.78.128.25:8766/futureloan/member/login'
    main = {"mobile_phone": "13998889999", "pwd": "12345688"}
    header = {"Content-Type":"application/json","X-Lemonban-Media-Type":"lemonban.v1"}
    b = HttpCookies().http_request(url, main, 'post',headers=header)
    print(b)