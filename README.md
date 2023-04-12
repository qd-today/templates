# 公共模板库 <sub>For Qiandao 签到框架</sub>

![GitHub last commit](https://img.shields.io/github/last-commit/qiandao-today/templates.svg?style=popout-square)

## 🏠简介

> 项目基于开源的签到框架站使用, 发布者在此发布模板仅供示范, 使用公共模板产生的任何问题需自行承担!

- [binux/qiandao](https://github.com/binux/qiandao) 最初版本框架，已停止维护。

- [qiandao-today/qiandao](https://github.com/qiandao-today/qiandao)  最新版框架，现持续更新中。

- 现模板基于 [最新版框架](https://github.com/qiandao-today/qiandao) 使用, 具体使用方式请自行学习。

> 极个别模板不兼容 [旧版本](https://github.com/binux/qiandao) 框架, 如有不兼容请使用 [最新版](https://github.com/qiandao-today/qiandao) 。
>
> 仅20211228及之后版本签到框架支持`api://`请求, 其他版本使用模板时请自行升级签到框架 或 将`api://`更换为`http://localhost/`

## 💭交流反馈

> QQ群: [642842749](https://jq.qq.com/?_wv=1027&k=PXZcLlO1) | **仅用于模板交流及BUG提交反馈**

## 🏁网站

Tips:

1. 链接里最好使用 `raw.githubusercontent.com` 的模板地址，其他的链接没有测试过
2. 修改日期格式 `四位年-两位月-两位日 24小时:两位分:两位秒` ，例子：`2020-05-15 07:03:47`

## 📄如何注册第三方库

20211021版本已经开放注册第三方库的功能，默认提供 <https://github.com/qiandao-today/templates> 仓库，如果需要自建第三方库，请注意一下几点：

1. **仓库根目录必须要有 `tpls_history.json` 文件**, 需符合以下规范:

    ```json
    {
        "version":"版本号 yyyymmdd",
        "har": {
            "必填，和name保持一致，注意要在文件里保持唯一": {
                "name": "必填", 
                "author": "选填，作者", 
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

2. 加速默认是 `jsdeliver` 加速, 只支持 `Github` 的加速
3. 模板更新规则: 上一次更新的24小时以后更新, 通过 `name` 判断是否存在, 如果不存在直接新增, 如果存在则通过 `version` 判断, 版本号大于当前缓存版本则更新

## 💬FAQ

**部分模板订阅后使用网站cookie却提示未登录？**

并不是模板问题而是网站可能对UA有验证，UA更换cookie会失效。请自行查看模板所使用的 User-Agent ,并使用所获得的UA去登录获取cookie。( Firefox 可使用 User-Agent Switcher and Manager 来设置特定的UA，其他浏览器同理。)

**想学习模板制作流程？**

[签到宝典demo](https://www.bilibili.com/video/BV1ox411C7RT)

[模板书写规范](https://github.com/github-h/qiandao-templates/blob/self-bak/README.md)

## 💝鸣谢

- [gxitm](https://github.com/gxitm)
- [AragonSnow](https://github.com/AragonSnow)
- [FellBan](https://github.com/FellBan)
- [Devil](https://github.com/q123458384)
- [github-h](https://github.com/github-h)
- [liuqitech](https://github.com/liuqitoday)
- 呆贼
- [stay](https://gitee.com/qypw)
- [acooler15](https://github.com/acooler15)
- [wjf0214](https://github.com/wjf0214)
- [a76yyyy](https://github.com/a76yyyy)
