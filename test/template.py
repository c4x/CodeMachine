# column 首字母小写
# mcolumn 首字母大写
# classname 为tablename，首字母大写
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
    "year":"Date"
}

propertyTemplate = Template("""
$comment    
private $type $column
""")

methodTemplate = Template("""
public void set$mcolumn($type $column) {
    this.$column = $column;
}

public $type get$mcolumn {
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
public class $ClassName
{ 
    $Property
}
""")

xmlTemplate = Template("""
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" 
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="$classname">
    <typeAlias alias="$classname" type="" /> 
    <select id="get$classname" resultType="$classname">
    </select>
</mapper>
""")