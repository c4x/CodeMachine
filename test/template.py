# column 首字母小写
# methond 首字母大写
# Class 为tablename，首字母大写
propertyTemplate = Template("""
$comment
private $attribute $column
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

xmlTemplate = Template("""
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="$methond">
    <typeAlias alias="$methond" type="" />
    <select id="get$methond" resultType="$methond">
    </select>
</mapper>
""")
