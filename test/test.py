import mysql.connector
import string
from string import Template
import os
import time

# import template
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

# 1.column => column : column, methond : Methond
# 2.column_attr => column : column_attr, methond : Column_attr
def getName(name):
    methonds = {}
    column = name.lower()
    methonds["column"] = column
    if "_" not in name:
        methond = name.capitalize()
    else:
        names = name.split("_",1)
        methond = names[0].lower().capitalize()+ "_" +names[-1].lower()
    methonds["methond"] = methond
    return methonds

def saveFile(filePath, buf):
    filePath = os.getcwd() + "/" + filePath
    if os.path.exists(filePath):
        os.remove(filePath)
        # else:
        #     os.remove(filePath)
        #     print(filePath)
    f = open(filePath,'w')
    f.write(buf)
    f.close()

try:
    connect = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='mysql')
    cursor = connect.cursor()
    # sql = "select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT from information_schema.columns where table_name='%s'"
    query = "select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT \
    from information_schema.columns where table_name='{}'".format("user")
    cursor.execute(query)
    columns = cursor.fetchall()
    # print(cursor._executed)
    pro,mth = '',''
    for column in columns:
        comment = column[2]
        attribute = dbmap[column[1]]
        methond = getName(column[0])
        if not len(comment)==0:
            comment = "// {}".format(comment)
        pro += propertyTemplate.substitute(comment = comment, attribute = attribute , column = methond["column"])
        mth += methodTemplate.substitute(methond = methond["methond"], attribute = attribute, column = methond["column"])
    propty = pro + mth
    time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    pojo = pojoTemplate.substitute(Class = "Test", Property = propty, Datetime = time)
    saveFile("test.java",pojo)
except mysql.connector.Error as err:
    print(err)
