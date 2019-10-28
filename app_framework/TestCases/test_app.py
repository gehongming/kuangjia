from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from  selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import time

# 0703 - app元素定位-元素操作 - 作业 - 同步上课的操作，完成app常见操作
# 截至：07月07日  23:59 下载讨论内容展示词云
# 如题。。
# 自己完成app的各类操作，可以使用公司的app。
# 1、滑屏操作
# 2、触屏操作
# 3、toast获取
# 4、列表滑动
#
# 提交内容：1、代码；2、代码运行结果截图/,
# #启动参数
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["noReset"] = True  #不清除app数据

# apk信息
# desired_caps["appPackage"] = "com.lemon.lemonban"
# desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"

desired_caps["appPackage"] = "com.ss.android.article.news"
desired_caps["appActivity"] = "com.ss.android.article.news.activity.SplashBadgeActivity"
#
driver=webdriver.Remote("http://127.0.0.1:4724/wd/hub",desired_caps)

#UiAutomator定位
uiselector_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.android.settings:id/keyPad")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(uiselector_loc))

ele=driver.find_element(*uiselector_loc)
#元素大小
ele_size=ele.size
#起始坐标点
start=ele.location
#步长
step=ele_size["height"]/8

#坐标点
point1=(start["x"] + step,start["y"] + 3*step)
point2=(start["x"] + 3*step,start["y"] + 3*step )
point3=(start["x"] + 5*step,start["y"] + 3*step)
point4=(start["x"] + 5*step,start["y"] + 5*step )
point5=(start["x"] + 3*step,start["y"] + 5*step )
point6=(start["x"] + step,start["y"] + 5*step)

tc=TouchAction(driver)

tc.press(x=point1[0],y=point1[1]).\
    wait(200).move_to(x=point2[0],y=point2[1]).\
    wait(200).move_to(x=point3[0],y=point3[1]).\
    wait(200).move_to(x=point4[0],y=point4[1]).\
    wait(200).move_to(x=point5[0],y=point5[1]).\
    wait(200).move_to(x=point6[0],y=point6[1]).release().perform()


time.sleep(0.5)

uiselector_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("推荐")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(uiselector_loc))
size=driver.get_window_size()

driver.swipe(size["width"]*0.9,size["height"]*0.5,size["width"]*0.1,size["height"]*0.5)
time.sleep(2)
#打开柠檬班
desired_caps["appPackage"] = "com.lemon.lemonban"
desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"
driver.start_activity(desired_caps["appPackage"],desired_caps["appActivity"])
#点击我的柠檬
uiselector_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("我的柠檬")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(uiselector_loc))
driver.find_element(*uiselector_loc).click()
#点击去登陆
uiselector_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(uiselector_loc))
driver.find_element(*uiselector_loc).click()
#登录
uiselector_phone_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("手机号码")')
uiselector_pwd_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("密码")')
uiselector_login_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("登录")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(uiselector_phone_loc))
driver.find_element(*uiselector_phone_loc).send_keys('17625188013')
driver.find_element(*uiselector_pwd_loc).send_keys('')
driver.find_element(*uiselector_login_loc).click()
toast_loc='//*[contains(*text,"手机号码或密码")]'
try:
    WebDriverWait(driver,10,0.01).until(EC.presence_of_all_elements_located((MobileBy.XPATH,toast_loc)))
    print(driver.find_element_by_xpath(toast_loc).text)
except:
    print("没有获取 到toast信息！")
time.sleep(1.5)
driver.find_element(*uiselector_pwd_loc).send_keys('188013')
driver.find_element(*uiselector_login_loc).click()

uiselector_loc=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("题库")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(uiselector_loc))

driver.find_element(*uiselector_loc).click()

old=driver.page_source
new_src=""
size=driver.get_window_size()
while old != new_src:
    #重新给old赋值。因为new马就要更新了。
    old = new_src
    #滑动一次
    driver.swipe(size["width"]*0.5,size["height"]*0.9,size["width"]*0.5,size["height"]*0.2,200)
    time.sleep(2)
    #获取滑动之后的页面内容
    new_src = driver.page_source
    #其它的需求：滑一次找一次的内容
    if new_src.find("逻辑思维题") != -1:
        print("找到了了了！！")
        break
