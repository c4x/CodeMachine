import mysql.connector
from string import Template
import template

try:
    connect = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='mysql')
    cursor = connect.cursor()
    # sql = "select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT from information_schema.columns where table_name='%s'"
    # executesql = 
    query = "select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT \
    from information_schema.columns where table_name='{}'".format("user")
    # print(query)
    cursor.execute(query)
    columns = cursor.fetchall()
    print(cursor._executed)
    for column in columns:
        comment = column[2]
        ctype = dbmap[column[1]]
        cnames = getName(column[0])
        if not len(comment==0):
            comment = "// {}".format(comment)
        pass
        propertyTemplate.substitute(comment=comment, type=ctype , column = )
    pass
except mysql.connector.Error as err:
    print(err)

def getName(name):
    cnames = ()
    if "_" not in name:
        column = name.lowercase()
        mcolumn = name.capitalize()
    else:
        
        pass
    pass