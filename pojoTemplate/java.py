from string import Template

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