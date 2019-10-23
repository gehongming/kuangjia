#__author__="G"
#date: 2019/6/15
from selenium.webdriver.common.by import By

class UserPageLocator:
    # 用户金额
    user_money=(By.XPATH,'//li[@class="color_sub"]')
    #抢投标
    qtoubiao=(By.XPATH,'//div[@class="rate_info"]/following-sibling::a[@href="/loan/loan_detail/Id/14630.html"]')
    #投标
    toubiao=(By.XPATH,'//button[text()="投标"]')
    #输入金额/获取金额
    input_money=(By.XPATH,'//input[@data-url="/Invest/invest"]')
    #查看并激活
    jihuo=(By.XPATH,'//div[text()="投标成功！"]/following-sibling::div[@class="capital_btn"]/button[text()="查看并激活"]')
    #查看剩余金额
    # less_money=(By.XPATH,'//li[@class="color_sub"]')
    #投标弹框提示
    invest_tools=(By.XPATH,'//div[@class="text-center"]')
    #投标按钮提示
    invest_button=(By.XPATH,'//button[@class="btn btn-special height_style"]')
    #投标提示弹框确定按钮
    invent_tool_ok=('//a[text()="确认"]')