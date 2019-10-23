#__author__="G"
#date: 2019/6/27
#__author__="G"
#date: 2019/6/27
from selenium.webdriver.common.by import By

class HomeworkLocator:

    #上传作业
    input_file=(By.XPATH,'//a[@class="sc-btn"]')
    # 点击上传文件
    file =(By.XPATH, '//a[@class="sc-btn webuploader-container"]')
    #选择留言
    check_message=(By.XPATH,'//span[@class="s2"]')
    #输入留言
    input_message=(By.ID,'comment')
    #保存留言
    save_message=(By.XPATH,'//textarea[@id="comment"]/following-sibling::a[@class="sure active"]')
    # 提交
    tijiao = (By.XPATH, '//a[@class="tj-btn active"]')
    #作业提交成功
    success_tijiao=(By.XPATH,'//div[@class="weui_dialog_bd"]')
    #知道了
    get=(By.XPATH,'//a[@class="weui_btn_dialog primary"]')