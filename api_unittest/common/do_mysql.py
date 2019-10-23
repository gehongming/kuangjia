import pymysql

from api_unittest.common.config import config


class DoMysql:

    def __init__(self):
        #建立连接
        host = config.get('mysql','host')
        user = config.get('mysql','user')
        password = config.get('mysql','password')
        port = config.get('mysql','port')
        self.mysql=pymysql.connect(host=host,user=user,password=password,port=int(port))
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor) #创建字典格式游标,返回的是字典格式

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return  self.cursor.fetchone() #返回一条数据，元组格式
    def fetch_all(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()  # 返回多条数据的时候，元组里面套元组

    def close(self):
        self.cursor.close() #关闭游标
        self.mysql.close()   #关闭连接

if __name__ == '__main__':
    mysql=DoMysql()
    result1=mysql.fetch_one('select * from future.member where mobilephone ="18861342700"')
    print(result1)
    # result2=mysql.fetch_all('select max(mobilephone) from future.member')
    # print(result2)
    # mysql.close()