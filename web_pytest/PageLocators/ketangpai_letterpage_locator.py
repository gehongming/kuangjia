#__author__="G"
#date: 2019/6/27
from selenium.webdriver.common.by import By

class LetterLocator:
    #搜索私信人
    search_man=(By.XPATH,'//input[@type="text"]')
    #选择发送对象
    check_man=(By.XPATH,'//span[@title="丢丢暂无"]')
    # 输入发送语句
    input_message=(By.XPATH, '//textarea[@class]')
    #发送
    send_message=(By.XPATH,'//a[@class="btn btn-positive"]')