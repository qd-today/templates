| 参数/过滤器                                        | 说明                                                         | 用例                                        | 参考值                           |
| -------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------- | -------------------------------- |
| {{md5(a)}}                                         | 计算 a 的 md5 值                                             | {{md5("123")}}                              | 202cb962ac59075b964b07152d234b70 |
| {{unicode(a)}}                                     | 将 a 由 Unicode 转为中文（和上面 API 相同）                  | {{unicode(u"\u4f60\u597d")}}                | 你好                             |
| {{random(min,max,unit)}}                           | 随机生成从 min 到 max 的 unit 位小数                         | {{random(0,10,4)}}                          | 0.8696                           |
| {{timestamp()}}                                    | 调用 python 里的 time.time() 函数                            | {{timestamp()}}                             | 1599990277.46                    |
| {{date_time(date,time,diff)}}                      | date：01表示是否显示日期（默认为 1）；time：01表示是否显示时分秒（默认为 1）；diff：时间差（默认为 0） | {{date_time(0,1,10)}}（在 18:06 测试）      | 04:06:21                         |
| {{quote_chinese(a)}}                               | 将 a 中所有 ord() >=128 的用 urlencode 表示（注意和 urlencoe 有区别） | {{quote_chinese("123中文QAQ&/:")}}          | 123%E4%B8%AD%E6%96%87QAQ&/:      |
| {% for i in urls %}                                | 开始一个 for 循环                                            | \                                           | \                                |
| {% endfor %}                                       | 结束一个 for 循环                                            | \                                           | \                                |
| {{loop.index}}                                     | 当前迭代的索引，从1开始算                                    | \                                           | \                                |
| safe                                               | 关闭 html 自动转义                                           | {{ '<em>name</em>' \| safe }}               | <em>name</em>                    |
| length                                             | 长度                                                         | {{"abc" \| length }}                        | 3                                |
| wordcount                                          | 计算字符串中单词的个数                                       | {{"abc def" \| wordcount}}                  | 2                                |
| striptags                                          | 删除字符串中所有的html标签，如果出现多个空格，将替换成一个空格 | {{"<a>123</a>    <p>456</p>" \| striptags}} | 123 456                          |
| replace(s,t)                                       | 将字符串中的 s 替换为 t                                      | {{"123"\|replace("1","a")}}                 | a23                              |
| truncate(length=255, killwords=False, end='...') | killwords=True 时在第 length 处截断，最后补上一个 end        | {{ "abcd"\|truncate(2, True,'q') }}         | aq                               |

