# 公共模板库 <sub>For QD 框架</sub>

![GitHub last commit](https://img.shields.io/github/last-commit/qd-today/templates.svg?style=popout-square)

## 🏠简介

项目基于开源的 QD 框架, 用于指导用户学习如何使用 QD 框架. 项目中的模板均为开源模板, 仅供学习参考使用, 请勿用于商业用途.

### QD 框架介绍

- [binux/qiandao](https://github.com/binux/qiandao) 最初版本框架，已停止维护。

- [qd-today/qd](https://github.com/qd-today/qd)  最新版框架，现持续更新中。

- 现模板基于 [最新版框架](https://github.com/qd-today/qd) 使用, 具体使用方式请自行学习。

> 极个别模板不兼容 [旧版本](https://github.com/binux/qiandao) 框架, 如有不兼容请使用 [最新版](https://github.com/qd-today/qd) 。
>
> 仅20211228及之后版本 QD 框架支持`api://`请求, 其他版本使用模板时请自行升级 QD 框架 或 将`api://`更换为`http://localhost/`

## 📢项目声明

- 使用公共模板产生的任何问题需自行承担!

- 发布者在此发布模板仅供示范, 请勿用于任何形式的商业用途.

- 如果您认为模板中的内容侵犯了您的合法权益, 请通过邮件或 [Discussions](https://github.com/qd-today/templates/discussions) 联系并 @仓库管理员或模板发布者 进行**删除**处理.

- 本项目及其内容仅用于学习和交流, 不承担任何责任!

## 💭交流反馈

> QQ群: [642842749](https://jq.qq.com/?_wv=1027&k=PXZcLlO1) | **仅用于模板交流及BUG提交反馈**

## 😀使用 Issue 发布模板

不再建议自行通过 Push 或 PR 的方式发布或更新模板, **请通过 Issue 的方式发布或更新模板**, 以便于模板审核及自动化管理.

### 发布模板流程

1. 进入 Issue 界面
2. 点击右上角 `New issue` 按钮, 选择 `HAR 模板发布` 对应的 `Get Started` 按钮
3. 标题填写 "模板名称 评论区",内容按照要求的格式进行填写
4. 点击 `Submit new issue` 按钮
5. 等待 Github Actions 运行完成, 会自动进行 PR
6. 等待模板审核通过, 仓库拥有者会进行合并
7. 合并完成后, 即完成模板的发布

> Tips:
>
> 1. 请勿在 Issue 里发布其他内容, 否则会被关闭.
> 2. 自动化 **更新** 模板:  直接在 Issue 里编辑内容, 不要重新发布 Issue.
>
>    > **PS:**
>    >
>    > Issue 内容须符合下述模板格式, 请确保 Issue 包含 `har` 标签;
>    >
>    > 非 Issue 作者更新, 请在评论区提交 har 模板内容并 @Issue作者或仓库管理员.
>
> 3. 自动化 **删除** 无效模板: 直接将对应的 Issue 标签标记为 `invalid` 即可.
>
>    > PS: Issue 内容须符合下述模板格式.
>
> 4. 仓库管理员对 PR 进行 Merge 时推荐使用 `Squash Merge` 方式.

### Q&A: 旧的 HAR 模板如何更新?

1. 复制以下格式内容至 HAR 模板所对应的 Issue 评论区内主楼部分, 编辑并修改其中的内容:

    ~~~markdown
    ### HAR 模板名称

    请将此行替换为**模板名称** ( HAR 文件的命名, 空格请用下划线代替, 允许中文, 请勿使用括号等特殊字符)

    ### 作者信息

    请将此行替换为**作者信息** ( HAR 文件的作者名或昵称, 用英文逗号 `,` 分隔多个作者, 请勿使用括号等特殊字符)

    ### 模板备注及说明

    请在此输入模板备注及说明 ( HAR 文件的备注及说明, 直接换行即可, 无需<br>)

    ### HAR 文件名

    请将此行替换为 **HAR 文件名** ( HAR 文件的文件名, 含 `.har` 后缀, 允许中文, 请勿使用括号等特殊字符)

    ### 其他信息

    请在此输入Issue的其他信息, 选填, 如无请填暂无 ( 例如: 对于 Issue 的其他说明 )

    ### HAR 模板内容

    ```JSON
    请将此行替换为 **HAR 模板内容** (请粘贴 HAR 文件内容, 允许使用 json 格式化工具进行格式化后再粘贴)
    ```

    ~~~

2. 修改完成后, 请为 Issue 添加 `har` 标签, 并点击 `Submit changes` 按钮进行提交

## 📄如何注册第三方库

20211021版本已经开放注册第三方库的功能，默认提供 <https://github.com/qd-today/templates> 仓库，如果需要自建第三方库，请注意一下几点：

1. **仓库根目录必须要有 `tpls_history.json` 文件**, 需符合以下规范:

    ```JSON
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

2. 加速默认是 `jsdelivr` 加速, 可通过 config 或环境变量配置修改为 `ghproxy` 或 `fastgit` 加速, 只支持 `Github` 仓库的加速
3. 模板更新规则: 上一次更新的24小时以后更新, 通过 `name` 判断是否存在, 如果不存在直接新增, 如果存在则通过 `version` 判断, 版本号大于当前缓存版本则更新

> 项目不对任何第三方库的内容负责, 请自行判断是否可信

## 💬FAQ

- **部分模板订阅后, 使用网站 Cookie 却提示未登录?**

    并不是模板问题, 而是网站可能对 UA 有验证, UA 更换Cookie 会失效。请自行查看模板所使用的 User-Agent, 并使用所获得的 UA 去登录获取 Cookie。(Firefox 可使用 `User-Agent Switcher and Manager` 来设置特定的UA, 其他浏览器同理)

- **想学习 HAR 模板制作流程?**

    [框架宝典demo](https://www.bilibili.com/video/BV1ox411C7RT)

    [模板书写规范](https://github.com/github-h/qiandao-templates/blob/self-bak/README.md)

## 💝鸣谢

排名不分先后:

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
- [MyFaith](https://github.com/MyFaith)
- [chen8945](https://github.com/chen8945)
- [ddd-zero](https://github.com/ddd-zero)
- [IITII](https://github.com/IITII)
- [AlisaCat-S](https://github.com/AlisaCat-S)
- ...
