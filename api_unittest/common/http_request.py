#__author__="G"
#date: 2019/4/11
import requests

from api_unittest.common.config import config


class HttpCookies:
    def http_request(self,url,data,method,cookies=None,json=None):
        url=config.get('api','pre_url')+url #url拼接
        if method.lower()=='get':
            resp=requests.get(url=url,params=data,cookies=cookies)
        elif method.lower()=='post':
            if json:
               resp=requests.post(url=url,json=data,cookies=cookies)
            else:
               resp=requests.post(url=url,data=data,cookies=cookies)
        # print ('''响应报文:{}
        # 响应头:{}
        # 状态码:{}
        # 响应cookie:{}
        # 请求cookies:{}'''
        # .format(resp.text
        #         ,resp.headers,resp.status_code,resp.cookies,resp.request._cookies))
        return (resp.text)
class HttpsCookies:
    def https_request(self,url,data,method,cookies=None,json=None):
        url=config.get('api','pre_url')+url #url拼接
        if method.lower()=='get':
            resp=requests.get(url=url,params=data,cookies=cookies,verify=False)
        elif method.lower()=='post':
            if json:
               resp=requests.post(url=url,json=data,cookies=cookies,verify=False)
            else:
               resp=requests.post(url=url,data=data,cookies=cookies,verify=False)
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

    def http_request(self, method, url, data=None, json=None):
        url = config.get('api', 'pre_url') + url
        if method.lower() == 'get':
            resp = self.session.request(method=method, url=url, params=data)
        elif method.lower() == 'post':
            if json:
                resp = self.session.request(method=method, url=url, json=data)
            else:
                resp = self.session.request(method=method, url=url, data=data)

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
class HttpsSessions:
    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def https_request(self, method, url, data=None, json=None):
        url = config.get('api', 'pre_url') + url
        if method.lower() == 'get':
            resp = self.session.request(method=method, url=url, params=data,verify=False)
        elif method.lower() == 'post':
            if json:
                resp = self.session.request(method=method, url=url, json=data,verify=False)
            else:
                resp = self.session.request(method=method, url=url, data=data,verify=False)

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
if __name__=='__main__':
#注册
  # url = 'http://test.lemonban.com/futureloan/mvc/api/member/register'
  # main = {'mobilephone': '17625188012', 'pwd': '1234561234561234561'}
  # G=HttpCookies()
  # G.http_request(url,main,'GET')
  # print(G)
  # # 登录
  url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
  main = {'mobilephone': '', 'pwd': ''}
  # G=HttpCookies()
  b=HttpCookies().http_request(url,main,'post')
  print(b)
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
  # d=G.http_request(url,main,'post',b)
  # print(d)