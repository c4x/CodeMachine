import tornado.web
import mysql.connector
import json

class DatabaseHandler(tornado.web.RequestHandler):
    # select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT from information_schema.columns where table_name='user';
    def get(self):
        user = self.get_argument('user')
        password = self.get_argument('password')
        host = self.get_argument('host')
        db = self.get_argument('db')
        connector = mysql.connector.connect(user=user, password=password, host=host, database=db)
        cursor = connector.cursor();
        try:
            cursor.execute("show tables")
            databases = cursor.fetchall()
            for table_name in databases:
                # print(table_name[0])
                self.tableProcess(cursor,table_name[0])
            self.write(json.dumps(databases))
        except mysql.connector.Error as e:
            raise e
        finally:
            cursor.close()
            connector.close()

    def tableProcess(self,cursor,table_name):
        cursor.execute("select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT from"
         " information_schema.columns where table_name= %s",table_name)
        columns = cursor.fetchall()
        print(columns)
        pass
