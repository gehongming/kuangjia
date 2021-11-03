import pymysql


class OpenMysql:

    def __int__(self, data_conf):
        self.mysql = pymysql.connect(**data_conf)
        self.cursor = self.mysql.cursor()

    def __enter__(self):
        return self.cursor   # 返回的是可操作对象

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()  # 关闭游标
        self.mysql.close()  # 关闭连接


if __name__ == '__main__':
    DATABASES_CONG = dict(
        host='localhost',
        user='root',
        password='mysql',
        database='test',
        port=3306,
        charset='utf8')

    with OpenMysql(DATABASES_CONG) as cur:
            cur.excute('sql语句')
    print(cur.fetchone())
