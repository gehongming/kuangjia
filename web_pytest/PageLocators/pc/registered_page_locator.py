#__author__="G"
#date: 2019/11/13


from selenium.webdriver.common.by import By


class RegisteredPageLocator:
    #同意按钮
    check_agree=(By.XPATH,'//button[@class="ant-btn ant-btn-primary"]')
    #注册手机号
    phone=(By.XPATH,'//input[@name="phone"]')
    #验证码
    phone_code=(By.XPATH,'//input[@name="phoneCode"]')
    #下一步
    go_on=(By.XPATH,'//p[text()="下一步"]')

    #店铺名称
    storename=(By.XPATH,'// input[ @ name = "storeName"]')
    #所在地
    location=(By.XPATH,'//span[@class="ant-cascader-picker-label"]')
    #省
    province=(By.XPATH,'//li[@title="新疆维吾尔自治区"]')
    #市
    city=(By.XPATH,'//li[@title="可克达拉市"]')
    #区
    area=(By.XPATH,'//li[@title="兵团六十七团"]')
    #详细地址
    address=(By.XPATH,'//input[@name="address"]')
    #联系人
    contact=(By.XPATH,'//input[@placeholder="请填写联系人姓名"]')
    #营业执照
    business_license=(By.XPATH,'//div[text()="营业执照"]/following-sibling::div/div/div/div/div/span/div[@class="ant-upload ant-upload-select ant-upload-select-picture-card"]')
    #选择医疗许可证
    choose_medicallicense=(By.XPATH,'//input[@type="checkbox"]')
    #医疗许可证
    medical_license =(By.XPATH,'//p[text()="上传医疗器械经营许可证："]/following-sibling::div/div/div/div/div/span/div[@class="ant-upload ant-upload-select ant-upload-select-picture-card"]')
    #下一步
    next=(By.XPATH,'//div[@class="btn__submit"]')





