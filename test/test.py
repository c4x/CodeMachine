

# 1.column => column : column, methond : Methond
# 2.column_attr => column : column_attr, methond : Column_attr


try:
    database = 'mysql'
    connect = mysql.connector.connect(user='root',password='',host='127.0.0.1',database=database)
    cursor = connect.cursor()
    query = "show tables"
    cursor.execute(query)
    tables = cursor.fetchall()
    time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    for table in tables:
        Class = table[0]
        print("this is table:{}".format(Class))
        query = "select COLUMN_NAME,DATA_TYPE,COLUMN_COMMENT from information_schema.columns where table_name='{}'".format(Class)
        cursor.execute(query)
        columns = cursor.fetchall()
        pro,mth = '',''
        for column in columns:
            comment = column[2]
            attribute = dbmap[column[1]]
            methonds = resetMethond(column[0])
            if not len(comment)==0:
                comment = "// {}".format(comment)
            pro += propertyTemplate.substitute(comment = comment, attribute = attribute , column = methonds["column"])
            mth += methodTemplate.substitute(methond = methonds["methond"], attribute = attribute, column = methonds["column"])
            propty = pro + mth
        pojo = pojoTemplate.substitute(Class = Class, Property = propty, Datetime = time)
        saveFile(database+time, "{}.java".format(Class), pojo)
except mysql.connector.Error as err:
    print(err)
