# 推送渠道配置文档

- [1. 企业微信](#1-企业微信)
  - [i. 企业微信自建应用](#i-企业微信自建应用)
  - [ii. 企业微信机器人](#ii-企业微信机器人)
- [2. Bark](#2-bark)
- [3. Telegram Bot](#3-telegram-bot)
- [4. Pushdeer](#4-pushdeer)
- [5. GO-CQHTTP](#5-go-cqhttp)
- [6. 钉钉群机器人](#6-钉钉群机器人)
- [7. Server 酱](#7-server-酱)
- [8. Push Plus](#8-push-plus)
- [9. Discord Webhook](#9-discord-webhook)
- [10. 邮件推送](#10-邮件推送)
- [11. CoolPush 酷推](#11-coolpush-酷推)
- [12. Qmsg 酱](#12-qmsg-酱)
- [13. 自定义推送](#13-自定义推送)

## 1. 企业微信

### i. 企业微信自建应用

通过自建应用推送到企业微信 / 微信，推荐使用。

> 本部分教程鸣谢 Server 酱。

1. 注册企业：用电脑打开 [企业微信官网](https://work.weixin.qq.com/)，注册一个企业。

2. 创建应用：注册成功后，点「管理企业」进入管理界面，选择「应用管理」→「自建」→「创建应用」。

    ![img](https://s2.loli.net/2022/02/06/j5EZvRV6YtDKr7B.png)

3. 创建完成后进入应用详情页，可以得到应用 ID( `agentid` )，应用 Secret( `secret` )，复制并填到配置文件对应位置（获取应用 Secret 时，可能会将其推送到企业微信客户端，需要在企业微信客户端查看）。

    ![img](https://s2.loli.net/2022/02/06/1N3rnFVHBqQk2Wh.png)

4. 获取企业 ID：进入「[我的企业](https://work.weixin.qq.com/wework_admin/frame#profile)」页面，拉到最下边，可以看到企业 ID，复制并填到配置文件中。

5. 获取推送用户：在 "通讯录" -> "成员管理" 中获取要收取信息的人员账号填入配置文件 `WW_APP_USERID`，全员推送填 `@all`。如果该应用只有一个人使用，填 `@all` 即可。

    ![image-20220206142035455](https://s2.loli.net/2022/02/06/XylJe4SAMFEjoYb.png)

6. 推送消息到微信：进入「我的企业」→「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到下边扫描二维码，关注以后即可收到推送的消息。

    ![img](https://s2.loli.net/2022/02/06/wOJ47LAVcX6Par8.png)

注：如果出现 ` 接口请求正常，企业微信接受消息正常，个人微信无法收到消息 ` 的情况：

1. 进入「我的企业」→「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到最下方，勾选 “允许成员在微信插件中接收和回复聊天消息”

    ![img](https://s2.loli.net/2022/02/06/sF8MS3ZBUCueN7I.jpg)

2. 在企业微信客户端「我」→「设置」→「新消息通知」中关闭 “仅在企业微信中接受消息” 限制条件

    ![img](https://s2.loli.net/2022/02/06/OdyJslVKtekTIAX.jpg)

### ii. 企业微信机器人

在终端某个群组添加机器人之后，创建者可以在机器人详情页看的该机器人特有的 webhookurl，将其中的 `key=` 后面的内容填写到配置文件 `WW_BOT_KEY` 中，例如 `693a91f6-7xxx-4bc4-97a0-0ec2sifa5aaa`。

## 2. Bark

1. 从 AppStore 下载并打开 [Bark](https://github.com/Finb/Bark) App，将完整推送链接（如 `https://api.day.app/xxxxxxx`）填入 `BARK_URL` 即可。
2. 支持部分可选配置，如自定义消息分组 `BARK_GROUP`，自定义通知图标 `BARK_ICON`，自定义消息保存 `BARK_ARCHIVE`，时效性通知 `BARK_LEVEL`。
   - BARK_GROUP: 指定推送消息分组，可在历史记录中按分组查看推送。
   - BARK_ICON：指定推送消息图标，仅 iOS15 或以上支持，如：`http://day.app/assets/images/avatar.jpg`。
   - BARK_ARCHIVE： 指定是否需要保存推送信息到历史记录，1 为保存，其他值为不保存。如果不指定这个参数，推送信息将按照 APP 内设置来决定是否保存。
   - BARK_LEVEL： 设置时效性通知：
     - `active`：不设置时的默认值，系统会立即亮屏显示通知。
     - `timeSensitive`：时效性通知，可在专注状态下显示通知。
     - `passive`：仅将通知添加到通知列表，不会亮屏提醒。

## 3. Telegram Bot

1. 创建机器人：打开 [@BotFather](https://t.me/botfather)，输入 `/newbot` 生成新一个的 bot。根据提示，依次输入：Bot 名字、Bot 账号（需要以 bot 结尾），复制获取到的 Token，填入配置文件 `TG_BOT_TOKEN`。
   ![image-20220206143711051](https://s2.loli.net/2022/02/06/MBX7EmTJZDtzq93.png)
2. 点击消息框中 `t.me / 你的 botid` 这个链接，跳转到你的 bot，点击 `START` 以关联你的 bot。
3. 打开 [@userinfobot](https://t.me/userinfobot)，发送 `/start`，获取你的 ID，填入配置文件 `TG_USER_ID`。
4. 使用 Telegram bot 推送需要配置代理，或搭建反代服务器后填入配置文件 `TG_BOT_API`。

## 4. Pushdeer

[PushDeer](https://github.com/easychen/pushdeer) 是一个可以自行架设的无 APP 推送服务，iOS 端基于轻 APP，无需安装 APP；Android 未来将基于快应用（正在开发），目前使用 APP（已接入 MI PUSH，因此小米用户可在不开启 APP 的情况下获取通知）。

1. 苹果手机（iOS 14+）用系统相机扫描下方码即可拉起轻应用。亦可在苹果商店搜索「PushDeer」安装（不要安装 PushDeer 自架版）。Android 快应用尚在开发，可下载并安装 Android 测试版 APP([GitHub](https://github.com/easychen/pushdeer/releases/tag/android1.0alpha)|[Gitee](https://gitee.com/easychen/pushdeer/releases/android1.0alpha))。
   ![img](https://github.com/easychen/pushdeer/raw/main/doc/image/clipcode.png)
2. 通过 apple 账号（或微信账号 · 仅 Android 版支持）登录。
3. 切换到「设备」标签页，点击右上角的加号，注册当前设备。
4. 切换到「Key」标签页，点击右上角的加号，创建一个 Key，将 Key 填入配置文件 `PUSHDEER_KEY` 中。

## 5. GO-CQHTTP

1. 部署 [GO-CQHTTP](https://github.com/Mrs4s/go-cqhttp)，参见文档 [快速开始](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B)，也可使用其他兼容 [OneBot-v11](https://github.com/botuniverse/onebot-11) 规范的框架或 SDK。
2. 将 CQHTTP 的服务器 ` 协议头://IP 或域名：端口号 ` 填入 `CQHTTP_URL`，需包含协议头，如：`http://1.2.3.4:5700/` 或 `https://example.com/`。
3. 配置发送模式 `CQHTTP_MESSAGE_TYPE`，`private` 为私聊发送，`group` 为群聊发送，`guild_id` 为频道发送。发送到频道需要先获取频道 ID 和子频道 ID，详见 CQHTTP 文档[频道 API](https://docs.go-cqhttp.org/api/guild.html)。
4. 配置消息接收方的 QQ 号 / 群号，填入 `CQHTTP_SEND_ID`，与发送模式匹配。
5. 若配置了 `Access Token`，需要填写 `CQHTTP_TOKEN`。

## 6. 钉钉群机器人

1. 创建钉钉群，并添加自定义机器人，参见 [钉钉开放平台 · 自定义机器人接入](https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.7f875e594zPr9w#topic-2026027)。
2. 将生成的 Webhook 地址中的 `access_token` 填入 `DD_BOT_TOKEN`。
3. 将创建过程中 ` 加签 ` 的密钥填入 `DD_BOT_SECRET`。

## 7. Server 酱

1. 前往 [Server 酱](https://sct.ftqq.com/) 官网注册并绑定微信。
2. 将获取到的 `send key` 填入 `config.json -> SCKEY` 中即可。

注：Server 酱免费版每天有 5 次的调用次数上限。

## 8. Push Plus

1. 登录 [pushplus 网站](http://www.pushplus.plus/) ，复制 token 填入 `PUSH_PLUS_TOKEN`。
2. 若要一对多推送，需要创建群组并将群组编号填入 `PUSH_PLUS_USER`，一对一推送无需填写。

## 9. Discord Webhook

1. 进入 Server Settings（服务器设定）- Integrations（整合），点击 Create Webhook，点击 Copy Webhook URL，填写到配置文件 `DISCORD_WEBHOOK` 中。
2. 可根据需要设置机器人显示的名字 `DISCORD_USERNAME`、机器人头像 `DISCORD_AVATAR`（需要是 web 图片地址）和消息卡片颜色 `DISCORD_COLOR`，详情可阅读 [Discord Webhooks Guide](https://birdie0.github.io/discord-webhooks-guide/structure/embeds.html)。

## 10. 邮件推送

进入邮件服务商帮助页面获取 SMTP 服务器服务器和端口信息，部分邮箱还需获取客户端授权码，将配置填入 MAIL 部分即可。
仅支持通过 SSL 发送，一般默认端口为 465（不开启 STARTTLS）或 587（开启 STARTTLS）。

## 11. CoolPush 酷推

注：现在酷推公共服务不可用，可能需要私有化部署。

1. 登录 [CoolPush](https://cp.xuthus.cc/)，绑定 QQ 号 / QQ 群及私有化部署地址，获取 `调用代码 Skey`。
2. 将 Skey 填入 `COOL_PUSH_SKEY` ，`COOL_PUSH_MODE` 支持 QQ 私聊推送 / QQ 群消息推送 / QQ 私有化私聊推送 / QQ 私有化群聊推送，不支持一对多推送。
3. 如果需要动态的指定推送消息给特定的 QQ 号或者群，将 QQ 号 / 群号填入 `COOL_PUSH_SENDID` 即可。

## 12. Qmsg 酱

登录 [Qmsg 酱](https://qmsg.zendee.cn/)，获取 KEY 填入 `QMSG_KEY` 即可。

注：Qmsg 酱容易被判定违规 =\_=，且无法进行群聊推送（审核不通过）。

## 13. 自定义推送

```yaml
  CUSTOM_NOTIFIER:
    method:             必填，请求方式，GET/POST
    url: ''             必填，请求 URL
    data_type:          必填，发送数据的格式，data/json/params
    headers: {}         选填，需要添加的 headers
    data: {}            选填，需要额外追加的请求内容
    title_key:          必填，消息标题的 key
    desp_key:           选填，消息详情的 key。若该项为空，则会将消息标题和消息详情合并推送。
    markdown:           选填，是否支持 markdown，true/false
    retcode_key:        必填，响应体中状态码的 key
    retcode_value:      必填，响应体中推送正常时的状态码
```

参考上表填写自定义推送配置。

### 示例

#### 使用自定义推送发送 CQHTTP 推送

```yaml
  CUSTOM_NOTIFIER:
    method: POST
    url: 'http://x.x.x.x:5700/send_private_msg'
    data_type: data
    headers: {"Authorization":"Bearer xxxxxxxx"}
    data: {"user_id": 123456789}
    title_key: message
    desp_key:
    markdown: false
    retcode_key: 'retcode'
    retcode_value: 0
```

#### 使用自定义推送发送 Telegram 推送

```yaml
  CUSTOM_NOTIFIER:
    method: POST
    url: 'https://tg-message.xm.mk/botxxxxxxxxxxxxxxxxxx/sendMessage'
    data_type: data
    headers: {}
    data: {"chat_id": 123456789, "parse_mode":"MarkdownV2"}
    title_key: text
    desp_key:
    markdown: true
    retcode_key: 'ok'
    retcode_value: True
```

#### 使用自定义推送发送 Pushplus 推送

```yaml
  CUSTOM_NOTIFIER:
    method: POST
    url: 'http://www.pushplus.plus/send'
    data_type: data
    headers: {}
    data: {"token":"xxxxxxxxxxxxxxxxx","template":"markdown"}
    title_key: title
    desp_key: content
    markdown: true
    retcode_key: 'code'
    retcode_value: 200
```

#### 使用自定义推送发送 Server 酱推送

```yaml
  CUSTOM_NOTIFIER:
    method: GET
    url: 'https://sctapi.ftqq.com/SCTxxxxxxxxxxxxxxxxx.send'
    data_type: params
    headers: {}
    data: {}
    title_key: title
    desp_key: desp
    markdown: true
    retcode_key: 'code'
    retcode_value: 0
```
