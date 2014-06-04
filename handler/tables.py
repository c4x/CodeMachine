import tornado.web
import mysql.connector
import json
import random


class TablesHandler(tornado.web.RequestHandler):
    def get(self):
        co = {}
        co["user"] = self.get_argument('user')
        co["password"] = self.get_argument('password')
        co["host"] = self.get_argument('host')
        co["db"] = self.get_argument('db')
        connector = mysql.connector.connect(user=co["user"], 
            password=co["password"], host=co["host"], database=co["db"])
        cursor = connector.cursor()
        try:
            cursor.execute("show tables")
            tables = cursor.fetchall()
            uuid = self.GenCRSF()
            self.render("tables.html", co = co, tables = tables, uuid = uuid)
        except mysql.connector.Error as e:
            self.render("tables.html", co = co, message = "get tables error")
            # raise e
        finally:
            cursor.close()
            connector.close()

    #使用时间戳生成，得到唯一
    def GenCRSF(length = 5):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join(random.sample(chars, 4))
