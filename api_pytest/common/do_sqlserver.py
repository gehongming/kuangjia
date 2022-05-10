import pymysql

from common.do_config import *
config = ReadConfig()


class DoSqlServer:

    def __init__(self, host, user, password, port, database):
        # 建立连接
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.sql = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database,
            charset='utf8')
        self.cursor = self.sql.cursor()

    def fetch_one_dict(self, sql):
        self.cursor = self.sql.cursor(as_dict=True)  # 创建一个字典类型的游标,返回字典
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        self.sql.commit()
        return result

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchone()  # 返回一条数据，元组格式
        self.sql.commit()
        return result

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()  # 返回多条数据的时候，元组里面套元组
        self.sql.commit()
        return result

    def close(self):
        self.cursor.close()  # 关闭游标
        self.sql.close()  # 关闭连接


if __name__ == '__main__':
    sql = DoSqlServer(
        host='192.168.0.101',
        user='sigob2c',
        password='SigoP@ssw0rd123',
        port='1433',
        database='SigoCn')
    # result1=mysql.fetch_one('SELECT * FROM sms_db_13.t_mvcode_info_0 WHERE Fmobile_no="17625188013"')
    # print(result1)
    result2 = sql.fetch_one_dict(
        "SELECT TOP 1 * FROM SigoCN.dbo.Sigocn_UserSMSVF WHERE VFUName='17625188013' ORDER BY AddTime desc;")
    print(result2['VFCode'])
    sql.close()
