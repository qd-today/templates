# 公共模板库 <sub>For Qiandao 签到框架</sub>

![GitHub last commit](https://img.shields.io/github/last-commit/qiandao-today/templates.svg?style=popout-square)

## 简介

> 项目基于开源的签到框架站使用, 发布者在此发布模板仅供示范, 使用公共模板产生的任何问题需自行承担!

- [binux/qiandao](https://github.com/binux/qiandao) 最初版本框架，已停止维护。

- [qiandao-today/qiandao](https://github.com/qiandao-today/qiandao)  最新版框架，现持续更新中。

- 现模板基于 [最新版框架](https://github.com/qiandao-today/qiandao) 使用, 具体使用方式请自行学习。

> 极个别模板不兼容[旧版本](https://github.com/binux/qiandao)框架, 如有不兼容请使用 [最新版](https://github.com/qiandao-today/qiandao) 。

## 鸣谢

[gxitm](https://github.com/gxitm)
[AragonSnow](https://github.com/AragonSnow)
[FellBan](https://github.com/FellBan)
[Devil](https://github.com/q123458384)
[github-h](https://github.com/github-h)
[liuqitech](https://github.com/liuqitoday)
呆贼
[stay](https://gitee.com/qypw)
[acooler15](https://github.com/acooler15)
[wjf0214](https://github.com/wjf0214)
[a76yyyy](https://github.com/a76yyyy)

> 排名不分先后

QQ群: 642842749

## 如何注册第三方库

20211021版本已经开放注册第三方库的功能，默认提供 https://github.com/qiandao-today/templates 仓库，如果需要自建第三方库，请注意一下几点：
1. **仓库根目录必须要有 tpls_history.json 文件**, 需符合以下规范:
```
{
    "version":"版本号 yyyymmdd",
    "har": {
        "必填，和name保值一致，注意要在文件里保持唯一": {
            "name": "必填", 
            "author": "选题，作者", 
            "url": "选填，har链接", 
            "update": false, 
            "comments": "选填，har文件的注释，可用来解释har所需变量的说明", 
            "filename": "必填，content为空时通过此来读取har", 
            "content": "选填,不填则根据 filename 的值来读取对应的har文件,默认为base64编码", 
            "date": "必填， 日期",
			"version":"必填， 版本号 yyyymmdd，框架通过版本号来判断是否更新模板",
            "commenturl":"选填，模板对应的评论区，留空时不显示按钮"
        }
    }
}
```
2. 加速默认是jsdeliver 加速, 只支持Github的加速 
3. 模板更新规则: 上一次更新的24小时以后更新, 通过name判断是否存在, 如果不存在直接新增, 如果存在则通过version判断, 版本号大于当前缓存版本则更新

## FAQ

**部分模板订阅后使用网站cookie却提示未登录？**

*并不是模板问题而是网站可能对UA有验证，UA更换cookie会失效。请自行查看模板所使用的 User-Agent ,并使用所获得的UA去登录获取cookie。( Firefox 可使用 User-Agent Switcher and Manager 来设置特定的UA，其他浏览器同理。)*

**想学习模板制作流程？**

[签到宝典demo](https://www.bilibili.com/video/BV1ox411C7RT)

[模板书写规范](https://github.com/github-h/qiandao-templates/blob/self-bak/README.md)

## 网站

Tips:
1. 链接里最好使用raw.githubusercontent.com的模板地址，其他的链接没有测试过
2. 修改日期格式 四位年-两位月-两位日 24小时:两位分:两位秒 ，例子：2020-05-15 07:03:47

网站 | 作者 | 链接 | 修改日期 | 备注/日志
---  |  ---  |  ---  |  ---  |  --- 
natfrp|[gxitm](https://github.com/gxitm)|[natfrp.har](https://raw.githubusercontent.com/qiandao-today/templates/master/natfrp.har)|2020-05-15 07:03:47|登录请求cookies：acw_tc，登录请求cookies：wordpress<br>url：https://openid.oxygen.moe/oauth/authorize/?response_type=code&client_id=ezEb7xY9ZHGwXMTtaUzdHcnKAGRnxUwphfMcIj9l
189天翼云盘|[gxitm](https://github.com/gxitm)|[189天翼云盘.har](https://raw.githubusercontent.com/qiandao-today/templates/master/189%E5%A4%A9%E7%BF%BC%E4%BA%91%E7%9B%98.har)|2020-06-08 14:35:16|手机抓包，accessToken在链接里<br>url：https://api.cloud.189.cn/login4MergedClient.action
国航APP|[AragonSnow](https://github.com/AragonSnow)|[airchina.har](https://raw.githubusercontent.com/qiandao-today/templates/master/airchina.har)|2020-06-17 02:40:10|抓包，app杀台后不用输密码登录就行，这两个链接里有这个参数<br>前两个在<br>https://m.airchina.com.cn:9061/worklight/apps/services/api/AirChina/iphone/init<br>param在<br>https://m.airchina.com.cn:9061/worklight/apps/services/api/AirChina/iphone/query<br>paramters=到&结束<br>20200617更新：替换公共API地址，改用内置，需要配合aragonsonw/qiandao最新版使用
轻之国度|[AragonSnow](https://github.com/AragonSnow)|[lightnovel 轻之国度.har](https://raw.githubusercontent.com/qiandao-today/templates/master/lightnovel%20%E8%BD%BB%E4%B9%8B%E5%9B%BD%E5%BA%A6.har)|2020-05-20 15:43:45|cks 网页cookie<br>https://www.lightnovel.us/
精易论坛|[FellBan](https://github.com/FellBan)|[精易论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E7%B2%BE%E6%98%93%E8%AE%BA%E5%9D%9B.har)|2020-05-21 09:23:54|cookie<br>https://bbs.125.la
腾讯视频VIP|[devil](https://github.com/q123458384)|[腾讯视频VIP.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E8%85%BE%E8%AE%AF%E8%A7%86%E9%A2%91vip.har)|2020-05-25 14:11:06|cookie<br>腾讯视频手机APP抓包cookie
柠檬PT签到|[devil](https://github.com/q123458384)|[柠檬PT签到.har](https://raw.githubusercontent.com/qiandao-today/templates/master/leaguehd%E6%9F%A0%E6%AA%ACPT.har)|2020-05-25 14:06:23|cookie<br>https://leaguehd.com/attendance.php
网易云音乐-电脑 AND 手机|[qiandao.today公共模板](https://qiandao.today/tpls/public)|[网易云音乐-电脑 AND 手机.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90-%E7%94%B5%E8%84%91%20AND%20%E6%89%8B%E6%9C%BA.har)|2020-06-25 21:12:03|cookie<br>https://music.163.com/
summer-plus(原south-plus)|[AragonSnow](https://github.com/AragonSnow)<br>[github-h](https://github.com/github-h)|[summer-plus(原south-plus).har](https://raw.githubusercontent.com/qiandao-today/templates/master/summer-plus(%E5%8E%9Fsouth-plus).har)|2021-02-13 16:00:00|cookie<br>https://www.summer-plus.net/
ZodGame论坛|[github-h](https://github.com/github-h)|[ZodGame论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/ZodGame%E8%AE%BA%E5%9D%9B.har)|2021-02-13 16:00:00|cookie<br>若无法正常访问，国内vps请自行添加hosts文件<br>https://zodgame.xyz
星空论坛seikuu|[github-h](https://github.com/github-h)|[星空论坛seikuu.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E6%98%9F%E7%A9%BA%E8%AE%BA%E5%9D%9Bseikuu.har)|2021-02-13 16:00:00|cookie<br>https://bbs2.seikuu.com/
终点论坛|[github-h](https://github.com/github-h)|[终点论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e7%bb%88%e7%82%b9%e8%ae%ba%e5%9d%9b.har)|2021-02-13 16:00:00|cookie<br>https://bbs.zdfx.net/
~~哥特动漫王国~~|[github-h](https://github.com/github-h)|[哥特动漫王国.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e5%93%a5%e7%89%b9%e5%8a%a8%e6%bc%ab%e7%8e%8b%e5%9b%bd.har)|2021-03-10 16:00:00|cookie<br>~~CC盾验证对时间要求较高，为了减少因访问过慢而导致错误，请自行添加hosts文件~~<br>关站了，要是能活过来再修吧<br>https://www.gtloli.net/forum.php/
萌出血动漫论坛|[github-h](https://github.com/github-h)|[萌出血动漫论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e8%90%8c%e5%87%ba%e8%a1%80%e5%8a%a8%e6%bc%ab%e8%ae%ba%e5%9d%9b.har)|2021-02-13 16:00:00|cookie<br>https://www.bbsmcx.com/forum.php
好快的车车(原HMOE俱乐部)|[github-h](https://github.com/github-h)|[好快的车车.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e5%a5%bd%e5%bf%ab%e7%9a%84%e8%bd%a6%e8%bd%a6.har)|2021-07-12 16:00:00|用户名+密码<br>https://cheche.one/
花火学园| [wjf0214](https://github.com/wjf0214) | [花火学园.har](https://raw.githubusercontent.com/qiandao-today/templates/master/花火学园.har) | 2021-11-20 21:20:00 | username:账号<br>password:密码<br>https://www.sayhuahuo.com/
夏跡natsunokiseki|[github-h](https://github.com/github-h)|[夏跡natsunokiseki.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e5%a4%8f%e8%b7%a1natsunokiseki.har)|2021-02-13 16:00:00|用户名+密码<br>每日登录奖励<br>该论坛时不时会忘记续费主机导致任务失败<br>https://bbs.natsunokiseki.org/
萌幻之乡 | [wjf0214](https://github.com/wjf0214) |[萌幻之乡.har](https://raw.githubusercontent.com/qiandao-today/templates/master/萌幻之乡.har) | 2021-11-20 21:20:00 | 登录后首页cookie<br>https://www.hmoe11.net/
KDays论坛| [wjf0214](https://github.com/wjf0214) |[KDays论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/KDays论坛.har)|2021-11-20 21:20:00| username:账号<br>password:密码<br>https://bbs.kdays.net/
吾爱破解|[wjf0214](https://github.com/wjf0214)|[吾爱破解.har](https://raw.githubusercontent.com/qiandao-today/templates/master/吾爱破解.har)|2021-11-20 21:00:00|登录后首页cookie,f12的时候请选中复制,不要右键复制值。<br>国内vps供应商已经被加ACL黑名单，请使用家庭IP<br>https://www.52pojie.cn/
ArcTime字幕平台|[github-h](https://github.com/github-h)|[ArcTime字幕平台.har](https://raw.githubusercontent.com/qiandao-today/templates/master/ArcTime%e5%ad%97%e5%b9%95%e5%b9%b3%e5%8f%b0.har)|2021-02-13 16:00:00|用户名+密码<br>https://m.arctime.cn/
柚坛社区|[github-h](https://github.com/github-h)|[柚坛社区.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e6%9f%9a%e5%9d%9b%e7%a4%be%e5%8c%ba.har)|2021-02-13 16:00:00|cookie<br>每日登录奖励<br>https://uotan.cn/
keylol(原SteamCN蒸汽论坛)|[github-h](https://github.com/github-h)|[keylol(原SteamCN蒸汽论坛).har](https://raw.githubusercontent.com/qiandao-today/templates/master/keylol(%e5%8e%9fSteamCN%e8%92%b8%e6%b1%bd%e8%ae%ba%e5%9d%9b).har)|2021-02-13 16:00:00|cookie<br>https://keylol.com/
3DMGAME论坛|[github-h](https://github.com/github-h)|[3DMGAME论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/3DMGAME%e8%ae%ba%e5%9d%9b.har)|2021-02-13 16:00:00|cookie<br>部分日常任务会随等级发生更改，有能力的可以自行修改<br>https://bbs.3dmgame.com/
QQNTR论坛|[github-h](https://github.com/github-h)|[QQNTR论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/QQNTR%e8%ae%ba%e5%9d%9b.har)|2021-02-13 16:00:00|cookie<br>https://iya.app/
CSDN-专业IT技术论坛|[github-h](https://github.com/github-h)|[CSDN-专业IT技术论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/CSDN-%e4%b8%93%e4%b8%9aIT%e6%8a%80%e6%9c%af%e8%ae%ba%e5%9d%9b.har)|2021-02-13 16:00:00|用户名+cookie<br>此为签到模块，记得定期抽奖<br>https://www.csdn.net/
杉果游戏|[github-h](https://github.com/github-h)|[杉果游戏.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E6%9D%89%E6%9E%9C%E6%B8%B8%E6%88%8F.har)|2021-06-29 16:00:00|用户名+密码<br>用户名为邮箱<br>https://ww.sonkwo.com/
华盟论坛|[github-h](https://github.com/github-h)|[华盟论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e5%8d%8e%e7%9b%9f%e8%ae%ba%e5%9d%9b.har)|2021-02-13 16:00:00|用户名+密码<br>https://bbs.77169.net/
飞客茶馆|[github-h](https://github.com/github-h)|[飞客茶馆.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e9%a3%9e%e5%ae%a2%e8%8c%b6%e9%a6%86.har)|2021-02-13 16:00:00|cookie<br>https://www.flyertea.com/
V2EX|[github-h](https://github.com/github-h)|[V2EX.har](https://raw.githubusercontent.com/qiandao-today/templates/master/V2EX.har)|2021-02-13 16:00:00|cookie<br>若访问不稳定也建议添加hosts，目前应该只有 104.20.10.218 比较好用<br>https://www.v2ex.com/
花粉俱乐部|[github-h](https://github.com/github-h)|[花粉俱乐部.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e8%8a%b1%e7%b2%89%e4%bf%b1%e4%b9%90%e9%83%a8.har)|2021-02-13 16:00:00|cookie<br>https://club.huawei.com/
IT天空|[github-h](https://github.com/github-h)|[IT天空.har](https://raw.githubusercontent.com/qiandao-today/templates/master/IT%e5%a4%a9%e7%a9%ba.har)|2021-02-13 16:00:00|cookie<br>https://www.itsk.com/
恩山无线论坛|[github-h](https://github.com/github-h)|[恩山无线论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e6%81%a9%e5%b1%b1%e6%97%a0%e7%ba%bf%e8%ae%ba%e5%9d%9b.har)|2021-03-10 16:00:00|cookie<br>每日登录奖励<br>若签到不稳定也请自行添加hosts<br>https://www.right.com.cn/forum/forum.php
万能福利吧|[github-h](https://github.com/github-h)|[万能福利吧.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e4%b8%87%e8%83%bd%e7%a6%8f%e5%88%a9%e5%90%a7.har)|2021-06-29 16:00:00|cookie<br>https://www.wnflb2020.com/forum.php
高清MP4粉|[github-h](https://github.com/github-h)|[高清MP4粉.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e9%ab%98%e6%b8%85mp4%e7%b2%89.har)|2021-06-29 16:00:00|cookie<br>每日签到<br>https://mp4fan.org/
漫画补档(账号密码版) | [wjf0214](https://github.com/wjf0214) |[漫画补档(账号密码版).har](https://raw.githubusercontent.com/qiandao-today/templates/master/漫画补档(账号密码版).har)|2020-11-20 21:20:00| 账号如果是中文请先去 http://tool.chinaz.com/tools/urlencode.aspx  选择gb2312进行UrlEncode编码后填入。<br>user:账号<br>pwd:密码<br>https://www.manhuabudang.com
什么值得买|[liuqitech](https://github.com/liuqitoday)<br>呆贼|[什么值得买.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E4%BB%80%E4%B9%88%E5%80%BC%E5%BE%97%E4%B9%B0.har)|2020-06-28 14:12:00|网页版 cookie<br>https://www.smzdm.com/
联想智选app|[aragonsnow](https://github.com/aragonsnow)|[联想智选app.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E8%81%94%E6%83%B3%E6%99%BA%E9%80%89app.har)|2020-08-03 15:00:21|需要在联想智选APP 账号密码登录抓包 <br> account 和 password 是app登录的账号密码, loginType,邮箱是email,手机号是msisdn <br> IMEI 和 baseinfo 在 抓包的 https://api.club.lenovo.cn/users/getSessionID 的header里 <br> deviceId 在  抓包的 https://uss.lenovomm.com/authen/1.2/tgt/user/get 的post里
隔壁网|[stay](https://gitee.com/qypw)|[隔壁网签到.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%E9%9A%94%E5%A3%81%E7%BD%91%E7%AD%BE%E5%88%B0.har)|2020-11-14 15:00:21|username 和 password 是登录的账号密码
MIUI历史版本|[stay](https://gitee.com/qypw)|[MIUI历史版本.har](https://raw.githubusercontent.com/qiandao-today/templates/master/MIUI%E5%8E%86%E5%8F%B2%E7%89%88%E6%9C%AC.har)|2020-11-14 15:00:50|username 和 password 是登录的账号密码
E次元| [wjf0214](https://github.com/wjf0214) |[E次元.har](https://raw.githubusercontent.com/qiandao-today/templates/master/E次元.har)|2021-11-20 21:20:00 | homeaction和cks 打开首页即可获取 https://www.evacg.cc/wp-admin/admin-ajax.php?action=<br>https://www.evacg.cc/cc/wp-admin/admin-ajax.php?action 链接里
数码之家|[acooler15](https://github.com/acooler15)|[数码之家.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e6%95%b0%e7%a0%81%e4%b9%8b%e5%ae%b6.har)|2021-06-28 20:24:00|cookies
迅维网|[acooler15](https://github.com/acooler15)|[迅维网.har](https://raw.githubusercontent.com/qiandao-today/templates/master/%e8%bf%85%e7%bb%b4%e7%bd%91.har)|2021-06-28 20:24:00|cookies
远景论坛|[acooler15](https://github.com/acooler15)|[远景论坛.har](https://raw.githubusercontent.com/qiandao-today/templates/master//%e8%bf%9c%e6%99%af%e8%ae%ba%e5%9d%9b.har)|2021-06-28 20:24:00|cookies
91Wii核心玩家的集中营|[FellBan](https://github.com/FellBan)|[91Wii核心玩家的集中营.har](https://raw.githubusercontent.com/qiandao-today/templates/master/91Wii核心玩家的集中营.har)|2021-07-02 11:00:00|cookies
致美化| [wjf0214](https://github.com/wjf0214) |[致美化.har](https://raw.githubusercontent.com/qiandao-today/templates/master/致美化.har)|2021-11-20 21:20:00| user:账号<br>pass:密码<br>https://zhutix.com
hao4k| [wjf0214](https://github.com/wjf0214) |[hao4k.har](https://raw.githubusercontent.com/qiandao-today/templates/master/hao4k.har)|2021-11-20 21:20:00| 登录后首页cookie,f12的时候请选中复制,不要右键复制值。<br>https://www.hao4k.cn/
掘金|[acooler15](https://github.com/acooler15)|[掘金.har](https://raw.githubusercontent.com/qiandao-today/templates/master/掘金.har)|2021-09-16 19:00:00|cookies
有道云笔记|[acooler15](https://github.com/acooler15)|[有道云笔记.har](https://raw.githubusercontent.com/qiandao-today/templates/master/有道云笔记.har)|2021-09-16 19:00:00|cookies
爱奇艺|[a76yyyy](https://github.com/a76yyyy)|[爱奇艺.har](https://raw.githubusercontent.com/qiandao-today/templates/master/爱奇艺.har)|2021-11-20 21:00:00|网址: https://www.iqiyi.com/<br>首页登录后在cookie中提取变量P00001和P00003<br>仅爱奇艺会员可用
MZFastCloud|[wjf0214](https://github.com/wjf0214)|[MZFastCloud.har](https://raw.githubusercontent.com/qiandao-today/templates/master/MZFastCloud.har)|2021-11-20 21:00:00|username:账号<br>password:密码<br>https://www.mzfast.xyz/
HiFiNi | [wjf0214](https://github.com/wjf0214) | [HiFiNi.har](https://raw.githubusercontent.com/qiandao-today/templates/master/HiFiNi.har) | 2021-11-20 21:00:00 | 登录后首页cookie<br>https://www.hifini.com/
人人素材 | [wjf0214](https://github.com/wjf0214) | [人人素材.har](https://raw.githubusercontent.com/qiandao-today/templates/master/人人素材.har) | 2021-11-20 21:00:00 | username:账号,手机号<br>password:密码<br>https://www.rrcg.cn/
SolidWorks机械工程师网 | [wjf0214](https://github.com/wjf0214) | [SolidWorks机械工程师网.har](https://raw.githubusercontent.com/qiandao-today/templates/master/SolidWorks机械工程师网.har) | 2021-11-20 21:50:00 | 账号如果是中文请先去 http://tool.chinaz.com/tools/urlencode.aspx  选择gb2312进行UrlEncode编码后填入。<br>username:账号<br>password:密码<br>https://www.swbbsc.com/
