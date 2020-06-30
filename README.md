# 整理qiandao.today可用的har

## 鸣谢
[gxitm](https://github.com/gxitm)

[AragonSnow](https://github.com/AragonSnow)

[FellBan](https://github.com/FellBan)

[Devil](https://github.com/q123458384)

[github-h](https://github.com/github-h)

[liuqitech](https://github.com/liuqitoday)

呆贼

## 网站

Tips:
1. 链接里最好使用raw.githubusercontent.com的模板地址，其他的链接没有测试过
2. 修改日期格式 四位年-两位月-两位日 24小时:两位分:两位秒 ，例子：2020-05-15 07:03:47

网站|作者|链接|修改日期|备注/日志
:-: | :-: | :-: | :-: |:-:
联想签到延保|[gxitm](https://github.com/gxitm)|[联想签到延保(jointask).har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E8%81%94%E6%83%B3%E7%AD%BE%E5%88%B0%E5%BB%B6%E4%BF%9D(jointask).har)|2020-05-15 04:37:17|account：账号，password：密码<br>参加连续10天签到任务
natfrp|[gxitm](https://github.com/gxitm)|[natfrp.har](https://raw.githubusercontent.com/qiandao-today/templates/master/natfrp.har)|2020-05-15 07:03:47|登录请求cookies：acw_tc，登录请求cookies：wordpress<br>url：https://openid.oxygen.moe/oauth/authorize/?response_type=code&client_id=ezEb7xY9ZHGwXMTtaUzdHcnKAGRnxUwphfMcIj9l
189天翼云盘|[gxitm](https://github.com/gxitm)|[189天翼云盘.har](https://raw.githubusercontent.com/qiandao-today/templates/master/189%E5%A4%A9%E7%BF%BC%E4%BA%91%E7%9B%98.har)|2020-06-08 14:35:16|手机抓包，accessToken在链接里<br>url：http://api.cloud.189.cn/loginByOpen189AccessToken.action?accessToken=
国航APP|[AragonSnow](https://github.com/AragonSnow)|[airchina.har](https://raw.githubusercontent.com/qiandao-today/templates/master/airchina.har)|2020-06-17 02:40:10|抓包，app杀台后不用输密码登录就行，这两个链接里有这个参数<br>前两个在<br>https://m.airchina.com.cn:9061/worklight/apps/services/api/AirChina/iphone/init<br>param在<br>https://m.airchina.com.cn:9061/worklight/apps/services/api/AirChina/iphone/query<br>paramters=到&结束<br>20200617更新：替换公共API地址，改用内置，需要配合aragonsonw/qiandao最新版使用
轻之国度|[AragonSnow](https://github.com/AragonSnow)|[lightnovel 轻之国度.har](https://raw.githubusercontent.com/qiandao-today/templates/master/lightnovel%20%E8%BD%BB%E4%B9%8B%E5%9B%BD%E5%BA%A6.har)|2020-05-20 15:43:45|cks 网页cookie<br>https://www.lightnovel.us/
summer-plus(原south-plus)|[AragonSnow](https://github.com/AragonSnow)<br>[github-h](https://github.com/github-h)|[summer-plus(原south-plus).har](https://raw.githubusercontent.com/qiandao-today/templates/master/summer-plus(%E5%8E%9Fsouth-plus).har)|2020-06-25 19:21:15|pwd 密码<br> user 用户名<br>https://www.summer-plus.net/
精易论坛|[FellBan](https://github.com/FellBan)|[精易论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E7%B2%BE%E6%98%93%E8%AE%BA%E5%9D%9B.har)|2020-05-21 09:23:54|cookie<br>https://bbs.125.la
腾讯视频VIP|[devil](https://github.com/q123458384)|[腾讯视频VIP.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E8%85%BE%E8%AE%AF%E8%A7%86%E9%A2%91vip.har)|2020-05-25 14:11:06|cookie<br>腾讯视频手机APP抓包cookie
WPS签到送会员|[devil](https://github.com/q123458384)|[WPS.har](https://raw.githubusercontent.com/qiandao-today/templates/master/wps%E7%AD%BE%E5%88%B0%E9%80%81%E4%BC%9A%E5%91%98-6_13%E7%82%B9%E4%B8%80%E6%AC%A1.har)|2020-05-25 14:06:23|WPS会员小程序抓包【sid】 https://zt.wps.cn/
柠檬PT签到|[devil](https://github.com/q123458384)|[柠檬PT签到.har](https://raw.githubusercontent.com/qiandao-today/templates/master/leaguehd%E6%9F%A0%E6%AA%ACPT.har)|2020-05-25 14:06:23|cookie<br>https://leaguehd.com/attendance.php
ZodGame论坛|[github-h](https://github.com/github-h)|[ZodGame论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/ZodGame%E8%AE%BA%E5%9D%9B.har)|2020-06-25 19:20:44|cookie<br>https://zodgame.xyz
星空论坛seikuu|[github-h](https://github.com/github-h)|[星空论坛seikuu.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E6%98%9F%E7%A9%BA%E8%AE%BA%E5%9D%9Bseikuu.har)|2020-06-25 17:51:54|cookie<br>https://bbs2.seikuu.com/
网易云音乐-电脑 AND 手机|[qiandao.today公共模板](https://qiandao.today/tpls/public)|[网易云音乐-电脑 AND 手机.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e7%bd%91%e6%98%93%e4%ba%91%e9%9f%b3%e4%b9%90-%e7%94%b5%e8%84%91+AND+%e6%89%8b%e6%9c%ba.har)|2020-06-25 21:12:03|cookie<br>https://music.163.com/
吾爱破解|[github-h](https://github.com/github-h)|[吾爱破解.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e5%90%be%e7%88%b1%e7%a0%b4%e8%a7%a3.har)|2020-06-09 10:59:44|cookie<br>https://www.52pojie.cn/
哥特动漫王国|[github-h](https://github.com/github-h)|[哥特动漫王国.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e5%93%a5%e7%89%b9%e5%8a%a8%e6%bc%ab%e7%8e%8b%e5%9b%bd.har)|2020-06-25 19:20:16|cookie<br>https://www.gtloli.net/forum.php
萌出血动漫论坛|[github-h](https://github.com/github-h)|[萌出血动漫论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e8%90%8c%e5%87%ba%e8%a1%80%e5%8a%a8%e6%bc%ab%e8%ae%ba%e5%9d%9b.har)|2020-06-25 17:52:07|cookie<br>http://www.bbsmcx.com/forum.php
ArcTime字幕平台|[github-h](https://github.com/github-h)|[ArcTime字幕平台.har](https://raw.githubusercontent.com/qiandao-today/templates/master/ArcTime%e5%ad%97%e5%b9%95%e5%b9%b3%e5%8f%b0.har)|2020-06-25 19:24:49|用户名+密码<br>http://m.arctime.cn/
柚坛社区|[github-h](https://github.com/github-h)|[柚坛社区.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e6%9f%9a%e5%9d%9b%e7%a4%be%e5%8c%ba.har)|2020-06-25 19:26:42|cookie<br>http://www.miuibbs.cn/
keylol(原SteamCN蒸汽论坛)|[github-h](https://github.com/github-h)|[keylol(原SteamCN蒸汽论坛).har](https://raw.githubusercontent.com/qiandao-today/templates/master/keylol(%e5%8e%9fSteamCN%e8%92%b8%e6%b1%bd%e8%ae%ba%e5%9d%9b).har)|2020-06-25 19:28:10|cookie<br>https://keylol.com/
机锋论坛|[github-h](https://github.com/github-h)|[机锋论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e6%9c%ba%e9%94%8b%e8%ae%ba%e5%9d%9b.har)| 2020-06-25 19:27:50 |cookie<br>http://bbs.gfan.com/
HMOE俱乐部|[github-h](https://github.com/github-h)|[HMOE俱乐部.har](https://raw.githubusercontent.com/qiandao-today/templates/master/HMOE%e4%bf%b1%e4%b9%90%e9%83%a8.har)| 2020-06-25 19:23:21 |auth为请求头中Authorization，此为签到重要标识，不定期会过期，需要重新获取<br>https://club.hmoe.club/
3DMGAME论坛|[github-h](https://github.com/github-h)|[3DMGAME论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/3DMGAME%e8%ae%ba%e5%9d%9b.har)| 2020-06-25 20:58:13 |cookie<br>https://bbs.3dmgame.com/
花火学院|[github-h](https://github.com/github-h)|[花火学院.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e8%8a%b1%e7%81%ab%e5%ad%a6%e9%99%a2.har)|2020-06-25 19:19:35|cookie<br>https://www.say-huahuo.com/
QQNTR论坛|[github-h](https://github.com/github-h)|[QQNTR论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/QQNTR%e8%ae%ba%e5%9d%9b.har)|2020-06-25 19:28:02|cookie<br>https://iya.app/
CSDN-专业IT技术论坛|[github-h](https://github.com/github-h)|[CSDN-专业IT技术论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/CSDN-%e4%b8%93%e4%b8%9aIT%e6%8a%80%e6%9c%af%e8%ae%ba%e5%9d%9b.har)|2020-06-25 19:24:22|用户名+cookie<br>此为签到模块，记得定期抽奖<br>https://www.csdn.net/
漫画补档|[AragonSnow](https://github.com/AragonSnow)|[漫画补档.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E6%BC%AB%E7%94%BB%E8%A1%A5%E6%A1%A3.har)|2020-06-16 02:24:44|用户名+密码<br>此模板默认是没有设置安全问题，没测试过有安全问题的是否能登陆成功<br>[https://www.manhuabudang.com/](https://www.manhuabudang.com/)
华盟论坛|[github-h](https://github.com/github-h)|[华盟论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e5%8d%8e%e7%9b%9f%e8%ae%ba%e5%9d%9b.har)|2020-06-25 19:27:40|用户名+密码<br>https://bbs.77169.net/
什么值得买|[liuqitech](https://github.com/liuqitoday)<br>呆贼|[什么值得买.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E4%BB%80%E4%B9%88%E5%80%BC%E5%BE%97%E4%B9%B0.har)|2020-06-28 14:12:00|网页版 cookie<br>https://www.smzdm.com/