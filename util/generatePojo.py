import mysql.connector
import string
from string import Template
import time,os
import pojoTemplate.java as java

def resetMethond(column):
    methonds = {}
    column = column.lower()
    methonds["column"] = column
    if "_" not in column:
        methond = column.capitalize()
    else:
        columns = column.split("_",1)
        methond = columns[0].lower().capitalize()+ "_" +columns[-1].lower()
    methonds["methond"] = methond
    return methonds

def saveFile(dirPath, filename, buf):
    filePath = "" + dirPath + "/" + filename
    dirPath = "" + dirPath
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)
    else:
        if os.path.exists(filename):
            os.remove(filename)
        f = open(filePath,'w')
        f.write(buf)
        f.close()

def generate(Class, user, password, host, db):
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    connect = mysql.connector.connect(user=user,password=password,host=host,database=db)
    cursor = connect.cursor()
    query = "select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT from \
     information_schema.columns where table_name='{}'".format(Class)
    cursor.execute(query)
    columns = cursor.fetchall()
    pro,mth = '',''
    for column in columns:
        comment = column[2]
        attribute = java.dbmap[column[1]]
        methonds = resetMethond(column[0])
        if not len(comment)==0:
            comment = "// {}".format(comment)
        pro += java.propertyTemplate.substitute(comment = comment, 
            attribute = attribute , column = methonds["column"])
        mth += java.methodTemplate.substitute(methond = methonds["methond"], 
            attribute = attribute, column = methonds["column"])
        propty = pro + mth
        pojo = java.pojoTemplate.substitute(Class = Class, Property = propty, Datetime = date)
        saveFile(db + date, "{}.java".format(Class), pojo)
    pass
