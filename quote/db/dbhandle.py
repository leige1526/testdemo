import pymysql


class DbHandle:
    def __init__(self, host, port, database, username, password, charset):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.charset = charset

    def get_connect(self):
        try:
            conn = pymysql.connect(host=self.host, port=self.port, database=self.database,
                                   user=self.username, password=self.password, charset=self.charset)
            return conn
        except Exception as e:
            print(e, "connect error")

    def sql_search(self, sql):
        res = None
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(sql)
            res = cursor.fetchall()
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e, "sql operation error")
        finally:
            cursor.close()
            conn.close()
        return res

    def sql_modify(self,sql,para):
        try:
            conn = self.get_connect()
            cursor = conn.cursor()
            cursor.execute(sql,para)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e,"sql operation error")
        finally:
            cursor.close()
            conn.close()


# db = DbHandle('localhost', 3306, 'quote', 'root', '123456', 'utf8')
# db.sql_modify("delete from tb_customer where customerNO = %s",['09999'])
# db = DbHandle('localhost', 3306, 'quote', 'root', '123456', 'utf8')
#
# print(db.sql_search('select * from tb_user'))