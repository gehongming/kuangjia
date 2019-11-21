#__author__="G"
#date: 2019/6/15

#encoding:utf-8
from Testdates.common_datas import base_url
#正常登录
login_data={"user":"17625188013","passwd":"sD2q"}

#正常登录购买隐形眼镜
success_data_yxyj = {"title":"NEO小黑环半年抛彩色隐形眼镜1片装",
                       "check_url":"https://www.yjq.com/search?keyword=NEO小黑环半年抛彩色隐形眼镜1片装",
                       "check_product_url":"https://www.yjq.com/product/1544773775205.html"}
#正常登录购买护理用品
success_data_huliye= {"title":"卫康新视多功能隐形眼镜护理液125ml",
                       "check_url":"https://www.yjq.com/search?keyword=卫康新视多功能隐形眼镜护理液125ml",
                       "check_product_url":"https://www.yjq.com/product/1805041333.html"}
#正常登录购买订制品
success_data_dzp = {"title":"【定制片】酷视远视散光隐形眼镜定制片半年抛1片装",
                "check_url":"https://www.yjq.com/search?keyword=【定制片】酷视远视散光隐形眼镜定制片半年抛1片装",
                "check_product_url":"https://www.yjq.com/product/1544773746114.html",
                "sku":["右眼（R）","+6.00","-0.25","170","1"]}
#正常登录购买伴侣盒
success_data_blh = {"title":"3N还原仪清洗仓",
                "check_url":"https://www.yjq.com/search?keyword=3N还原仪清洗仓",
                "check_product_url":"https://www.yjq.com/product/1544773749673.html",
                "count":"1"}
#正常登录购买镜片
success_data_jp = {"title":"万新博览1.56防蓝光非球面近视镜片",
                "check_url":"https://www.yjq.com/search?keyword=万新博览1.56防蓝光非球面近视镜片",
                "check_product_url":"https://www.yjq.com/product/1810231689.html",
                "count":"2"}

#生成订单
to_order={"message":"网管查房","check_url":"https://shop.yjq.com/shoppingCenter/shoppingList"}
