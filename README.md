# 整理qiandao.today可用的har
## 鸣谢
[gxitm](https://github.com/gxitm)

[AragonSnow](https://github.com/AragonSnow)

[FellBan](https://github.com/FellBan)
## 网站
Tips:链接里最好使用raw.githubusercontent.com的模板地址，其他的链接没有测试过
网站|作者|链接|变量说明|备注/日志
:-: | :-: | :-: | :-: |:-:
联想签到延保|[gxitm](https://github.com/gxitm)|[联想签到延保(jointask).har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E8%81%94%E6%83%B3%E7%AD%BE%E5%88%B0%E5%BB%B6%E4%BF%9D(jointask).har)|account：账号，password：密码|参加连续10天签到任务
natfrp|[gxitm](https://github.com/gxitm)|[natfrp.har](https://raw.githubusercontent.com/qiandao-today/templates/master/natfrp.har)|登录请求cookies：acw_tc，登录请求cookies：wordpress|url：https://openid.oxygen.moe/oauth/authorize/?response_type=code&client_id=ezEb7xY9ZHGwXMTtaUzdHcnKAGRnxUwphfMcIj9l
189天翼云盘|[gxitm](https://github.com/gxitm)|[189天翼云盘.har](https://raw.githubusercontent.com/qiandao-today/templates/master/189%E5%A4%A9%E7%BF%BC%E4%BA%91%E7%9B%98.har)|accessToken|url：http://api.cloud.189.cn/loginByOpen189AccessToken.action?accessToken=
国航APP|[AragonSnow](https://github.com/AragonSnow)|[airchina.har](https://raw.githubusercontent.com/qiandao-today/templates/master/airchina.har)|id<br>authenticityRealm<br>param|抓包，app杀台后不用输密码登录就行，这两个链接里有这个参数<br>前两个在<br>https://m.airchina.com.cn:9061/worklight/apps/services/api/AirChina/iphone/init<br>param在<br>https://m.airchina.com.cn:9061/worklight/apps/services/api/AirChina/iphone/query<br>paramters=到&结束<br>
轻之国度|[AragonSnow](https://github.com/AragonSnow)|[lightnovel 轻之国度.har](https://raw.githubusercontent.com/qiandao-today/templates/master/lightnovel%20%E8%BD%BB%E4%B9%8B%E5%9B%BD%E5%BA%A6.har)|cks 网页cookie|https://www.lightnovel.us/
south-plus论坛|[AragonSnow](https://github.com/AragonSnow)|[south-plus.har](https://raw.githubusercontent.com/qiandao-today/templates/master/south-plus.har)|pwd 密码<br> user 用户名|https://www.south-plus.net/
精易论坛|[FellBan](https://github.com/FellBan)|[精易论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E7%B2%BE%E6%98%93%E8%AE%BA%E5%9D%9B.har)|cookie|https://bbs.125.la
腾讯视频VIP|[devil](https://github.com/q123458384)|[腾讯视频VIP.har](https://github.com/qiandao-today/templates/blob/master/%E8%85%BE%E8%AE%AF%E8%A7%86%E9%A2%91vip.har)|cookie|腾讯视频手机APP抓包cookie
