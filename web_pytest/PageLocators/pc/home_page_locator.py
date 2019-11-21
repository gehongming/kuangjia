#__author__="G"
#date: 2019/6/15

from selenium.webdriver.common.by import  By


class HomePageLocator:
    #搜索框
    search=(By.XPATH,'//input[@class="s-input"]')
    #隐形商品链接
    yx=(By.XPATH,'//a[@href="https://www.yjq.com/product/1544773775205.html"]')
    # 护理用品链接
    hl=(By.XPATH,'//a[@href="https://www.yjq.com/product/1805041333.html"]')
    #定制片链接
    dz = (By.XPATH,'//a[@href="https://www.yjq.com/product/1544773746114.html"]')
    #多彩伴侣盒链接
    blh=(By.XPATH,'//a[@href="https://www.yjq.com/product/1544773749673.html"]')
    # 镜片链接
    jp = (By.XPATH,'//a[@href="https://www.yjq.com/product/1810231689.html"]')
    ###############
    #老项目进入购物车
    go_cart=(By.XPATH,'//a[@href="https://cart.yjq.com/shoppingCart"]')

    # 新项目进入购物车
    go_cart_new = (By.XPATH, '//span[@class="pl20 pr20"]')

    #进入采购单
    go_purchase_order=(By.XPATH,'//a[@href="https://shop.yjq.com/shoppingCenter/shoppingList"]')



