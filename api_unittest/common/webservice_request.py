from suds.client import Client
from api_unittest.common import openexcel
from api_unittest.common.config import config
import suds


class WebService:
    def webservice(self,url,data,method):
    #要访问的Webservice地址
        url=config.get('api_web','pre_url')+url #url拼接
    #创建Webservice Client对象
        client = Client(url)
        # print(client)#可以打印出Client对象所有的方法
        # data={"client_ip":"192.168.0.105","tmpl_id":"1","mobile":"18762725696"}#用字典的方式传值
        try:
            resp = eval("client.service.{0}({1})".format(method, data))
            msg = resp.retInfo
            # print("返回码", resp.retCode)
            # print("返回信息", resp.retInfo)
        except suds.WebFault as e:
            # print(e.fault.faultstring)
            msg = e.fault.faultstring

        return msg


if __name__ == '__main__':






    url = "finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
    data={'verify_code': '616511', 'user_id': '程桂香', 'channel_id': '3', 'pwd': '123456', 'ip': '192.31.197.10', 'mobile': '15129371321'}
    data={"verify_code":'616511',"user_id":"庄勇","channel_id":"1","pwd":"123456","ip": "192.52.189.13", "mobile":'13170390562'}
    a=WebService()
    result=a.webservice(url,data,'userRegister')
    print(result)


