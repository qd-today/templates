### api
api|地址|参数|参数是否必须|说明|用例
:-: | :-: | :-: |:-:|:-:|:-:|
时间戳|http://localhost/util/timestamp|ts<br>|否|默认返回当前时间戳和时间<br>如果参数带时间戳，返回所对应北京时间|http://localhost/util/timestamp <br>http://localhost/util/timestamp?ts=1586921249
Unicode转中文|http://localhost/util/unicode|content|是|要转码的内容|http://localhost/util/unicode?content=今日签到：1\u5929\u5ef6\u4fdd
Url转中文|http://localhost/util/urldecode|content|是|要转码的内容|http://localhost/util/urldecode?content=签到成功！每日签到获得%2C
正则表达式|http://localhost/util/regex|data,p|是|data：原始数据<br>p：正则表达式|http://localhost/util/regex?data=%7b"code"%3a0%2c"msg"%3a"成功"%2c"data"%3a%7b"users"%3a%5b%7b"name"%3a"张三"%2c"gender"%3a"male"%2c"age"%3a12%7d%2c%7b"name"%3a"李四"%2c"gender"%3a"female"%2c"age"%3a15%7d%2c%7b"name"%3a"王五"%2c"gender"%3a"male"%2c"age"%3a22%7d%2c%7b"name"%3a"赵六"%2c"gender"%3a"male"%2c"age"%3a24%7d%5d%2c"goods"%3a%5b%7b"name"%3a"apple"%2c"price"%3a15%2c"num"%3a200%7d%2c%7b"name"%3a"pear"%2c"price"%3a18%2c"num"%3a100%7d%2c%7b"name"%3a"banana"%2c"price"%3a16%2c"num"%3a210%7d%5d%7d%7d&p=name"%3a"(.%2b%3f)"
字符串替换|http://localhost/util/string/replace|p,s,t|是|p：正则表达式<br>s:要替换的字符串<br>t:要替换的内容|http://localhost/util/string/replace?p=%E4%BA%BA&t=%E5%AD%97%E7%AC%A6%E4%B8%B2&s={%22text%22:%22%E6%88%91%E6%98%AF%E4%BA%BA%22}