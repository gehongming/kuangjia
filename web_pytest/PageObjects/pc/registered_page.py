#__author__="G"
#date: 2019/11/13


from common.basepage import BasePage
from PageLocators.pc.registered_page_locator import RegisteredPageLocator as rpl
import time

class RegisteredPage(BasePage):

    def aggre(self):
        self.click_element(rpl.check_agree,'同意协议')

    def check_phone(self,phone,code):
        self.input_text(rpl.phone,'输入手机号',phone)
        self.input_text(rpl.phone_code,'输入验证码',code)
        self.click_element(rpl.go_on,'去填信息')

    def register(self,storename,address,contact):
        self.input_text(rpl.storename,'输入店铺名称',storename)
        self.click_element(rpl.location,'点击所在地')
        time.sleep(0.2)
        self.click_element(rpl.province, '省')
        time.sleep(0.2)
        self.click_element(rpl.city, '市')
        time.sleep(0.2)
        self.click_element(rpl.area, '区')
        time.sleep(0.1)
        self.input_text(rpl.address, '输入详细地址', address)
        self.input_text(rpl.contact, '输入联系人', contact)
    # 上传营业执照
    def update_business(self,b_address):
        self.click_element(rpl.business_license,'请求上传营业执照')
        time.sleep(1)
        self.upload(b_address, '上传营业执照')
    #上传医疗许可证
    def update_medical(self,m_address):
        self.click_element2(rpl.choose_medicallicense,'选择医疗许可证')
        self.click_element(rpl.medical_license, '请求上传医疗许可证')
        time.sleep(1)
        self.upload(m_address, '上传医疗许可证执照')
        time.sleep(10)
    #提交
    def tijiao(self):
        self.click_element(rpl.next,'下一步')


