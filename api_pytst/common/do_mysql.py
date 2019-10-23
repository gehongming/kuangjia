import pymysql

from api_pytst.common.config import config


class DoMysql:

    def __init__(self):
        #建立连接
        host = config.get('mysql','host')
        user = config.get('mysql','user')
        password = config.get('mysql','password')
        port = config.get('mysql','port')
        self.mysql=pymysql.connect(host=host,user=user,password=password,port=int(port))
        self.cursor = self.mysql.cursor()

    def fetch_one_dict(self,sql):
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 创建一个字典类型的游标,返回字典
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()
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
    # result1=mysql.fetch_one('SELECT * FROM sms_db_13.t_mvcode_info_0 WHERE Fmobile_no="17625188013"')
    # print(result1)
    result2=mysql.fetch_one("SELECT * FROM sms_db_13.t_mvcode_info_0 WHERE Fmobile_no='17625188013'")
    print(result2[2])
    mysql.close()