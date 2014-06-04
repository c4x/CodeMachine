import mysql.connector
import string
from string import Template
import os
import time

dbmap = {
    "varchar":"String",
    "char":"String",
    "blob":"byte[]",
    "text":"String",
    "integer":"Long",
    "tinyint":"Integer",
    "smallint":"Integer",
    "mediumint":"Integer",
    "bit":"Boolean",
    "bigint":"BigInteger",
    "float":"Float",
    "double":"Double",
    "decimal":"BigDecimal",
    "boolean":"Integer",
    "id":"Long",
    "date":"Date",
    "time":"Time",
    "datetime":"Timestamp",
    "timestamp":"Timestamp",
    "year":"Date",
    "enum":"String",
    "int":"Long",
    "set":"String",
    "longblob":"byte[]",
    "mediumtext":"String"
}

propertyTemplate = Template("""
$comment
private $attribute $column;
""")

methodTemplate = Template("""
public void set$methond($attribute $column) {
    this.$column = $column;
}

public $attribute get$methond {
    return $column;
}
""")

pojoTemplate = Template("""
import java.lang.*;

/*
*
*   Author:
*
*   Created by CodeBuilder@$Datetime
*/
public class $Class
{
    $Property
}
""")

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
    filePath = "/Users/cfour/workspace/codespace/CodeMachine/" + dirPath + "/" + filename
    dirPath = "/Users/cfour/workspace/codespace/CodeMachine/" + dirPath
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
        attribute = dbmap[column[1]]
        methonds = resetMethond(column[0])
        if not len(comment)==0:
            comment = "// {}".format(comment)
        pro += propertyTemplate.substitute(comment = comment, 
            attribute = attribute , column = methonds["column"])
        mth += methodTemplate.substitute(methond = methonds["methond"], 
            attribute = attribute, column = methonds["column"])
        propty = pro + mth
        pojo = pojoTemplate.substitute(Class = Class, Property = propty, Datetime = date)
        saveFile(db + date, "{}.java".format(Class), pojo)
    pass
