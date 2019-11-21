#__author__="G"
#date: 2019/10/31
from selenium.webdriver.common.by import  By


class ProductPageLocator:
    #隐形商品sku 花色 度数
    yx_huase=(By.XPATH,'//span[text()="星空紫"]')
    yx_dushu=(By.XPATH,'//tr[@skuid="6508964602909294595"]/td/span/button[@class="skuAdd skuRA"]')

    #选择护理用品数量
    hl_count=(By.XPATH,'//input[@class="detailsCglNum"]')

    #定制片sku （左右眼 定制球镜  定制柱镜  轴位  数量 ）
    dz_zyy=(By.XPATH,'//td[@attributename="左右眼"]/input')
    dz_dzqj=(By.XPATH,'//td[@attributename="定制球镜"]/input')
    dz_dzzj = (By.XPATH, '//td[@attributename="定制柱镜"]/input')
    dz_zw = (By.XPATH, '//td[@attributename="轴位"]/input')
    dz_count = (By.XPATH, '//input[@class="skuNum"]')

    #多彩伴侣盒sku
    blh_count = (By.XPATH, '//tr[@skuid="1544772850182546207"]/td/span/input[@class="skuNum"]')

    #镜片sku
    jp_count=(By.XPATH, '//tr[@skuid="6460400882461704195"]/td/span/input[@class="skuNum"]')

##########################
    # 加入购物车（通用）
    join_gwc=(By.XPATH,'//button[@class="add-car"]')
    #购物车同时加入成功提示(通用)
    success_gwc=(By.XPATH,'//div[text()="已成功加入购物车"]')
###########################