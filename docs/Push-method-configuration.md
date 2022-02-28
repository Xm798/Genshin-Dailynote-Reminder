# Push method configuration

- [1. Wechat Work](#1-wechat-work)
  - [i. WeChat Work self-built application](#i-wechat-work-self-built-application)
  - [ii. WeChat Work group robot](#ii-wechat-work-group-robot)
- [2. Bark](#2-bark)
- [3. Telegram Bot](#3-telegram-bot)
- [4. Pushdeer](#4-pushdeer)
- [5. GO-CQHTTP](#5-go-cqhttp)
- [6. DingTalk group robot](#6-dingtalk-group-robot)
- [7. Server Chan](#7-server-chan)
- [8. Push Plus](#8-push-plus)
- [9. Discord Webhook](#9-discord-webhook)
- [10. Email](#10-email)
- [11. CoolPush Cool Push](#11-coolpush-cool-push)
- [12. Qmsg](#12-qmsg)
- [13. Custom Notifier](#13-custom-notifier)


## 1. Wechat Work

### i. WeChat Work self-built application

> Thanks to Server Chan for this part of the tutorial.

1. Register a business: Use your computer to open [official website](https://work.weixin.qq.com/)and register a business.

2. Create an application: After successful registration, tap "Manage Business" to enter the management interface, and select "Application Management" → "Create Your Own" → "Create Application".

   ![img](https://s2.loli.net/2022/02/06/j5EZvRV6YtDKr7B.png)

3. After the creation, enter the application details page, you can get the application ID ( `agentid` ), application secret ( `secret` ), copy and fill in the corresponding location of the configuration file (when you get the application secret, it may be pushed to the enterprise WeChat client. (You need to check it in the enterprise WeChat client).

![img](https://s2.loli.net/2022/02/06/1N3rnFVHBqQk2Wh.png)

4. Get enterprise ID: Go to " [我的企业](https://work.weixin.qq.com/wework_admin/frame#profile)" page, pull down to the bottom, you can see the enterprise ID, copy and fill in the configuration file.

5. Get the push user: Get the account of the person you want to receive information from in "Address Book" -> "Member Management" and fill in the profile `WW_APP_USERID`, and fill in `@all` for the full push. If the application is used by only one person, fill in `@all`.

   ![ image-20220206142035455 ](https://s2.loli.net/2022/02/06/XylJe4SAMFEjoYb.png)

6. Push message to WeChat: Go to "My Business" → " [微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)", pull down and scan the QR code, then you can receive the push message after following.

   ![img](https://s2.loli.net/2022/02/06/wOJ47LAVcX6Par8.png)

Note: In case of `interface request is normal, enterprise WeChat receives messages normally, personal WeChat cannot receive messages`.

1.  Go to "My Business" → " [微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)", pull to the bottom and check "Allow members to receive and reply to chat messages in WeChat plugin" ![img](https://s2.loli.net/2022/02/06/sF8MS3ZBUCueN7I.jpg)
2.  Turn off the restriction of "Receive messages only in Enterprise Wechat" in "Me" → "Settings" → "New Message Notification" in Enterprise Wechat client ![img](https://s2.loli.net/2022/02/06/OdyJslVKtekTIAX.jpg)

### ii. WeChat Work group robot

After adding a bot to a group in the terminal, the creator can look at the bot-specific webhookurl on the bot details page and fill in the contents after `key=` in the configuration file `WW_BOT_KEY`, for example `693a91f6-7xxx-4bc4-97a0-0ec2sifa5aaa`.

## 2. Bark

1. Download and open the [Bark](https://github.com/Finb/Bark) App from the AppStore and fill in the full push link (e.g. `https://api.day.app/xxxxxxx`) into `BARK_URL` to do so.
2. Support some optional configurations, such as custom message grouping `BARK_GROUP`, custom notification icon `BARK_ICON`, custom message saving `BARK_ARCHIVE`, time-sensitive notification `BARK_LEVEL`.
   - BARK_GROUP: Specify the push message group, you can view the push by group in the history.
   - BARK_ICON: Specify the push message icon, only supported by iOS15 or above, e.g.: `http://day.app/assets/images/avatar.jpg`.
   - BARK_ARCHIVE: Specify whether the push message should be saved to the history, 1 is to save, other values are not to save. If this parameter is not specified, the push information will be saved or not according to the setting in APP.
   - BARK_LEVEL: Sets the time-sensitive notification.
     - `active`: The default value when not set, the system will light up the screen to display the notification immediately.
     - `timeSensitive`: time-sensitive notifications that can be displayed in the focused state.
     - `passive`: Only notifications are added to the notification list, and no screen will be lit up for alerts.

## 3. Telegram Bot

1. To create a bot: Open [@BotFather](https://t.me/botfather), enter `/newbot` to create a new bot. Follow the prompts and enter: Bot name, Bot account (needs to end with bot), copy the obtained Token and fill in the configuration file `TG_BOT _TOKEN`. ![ image-20220206143711051 ](https://s2.loli.net/2022/02/06/MBX7EmTJZDtzq93.png)
2. Click on the link `t.me/你的botid `in the message box to jump to your bot and click `START` to associate your bot.
3. Open [@userinfobot](https://t.me/userinfobot), send `/start`, get your ID and fill in the profile `TG_USER_ID`.
4. To use Telegram bot push, you need to configure a proxy or fill in the configuration file `TG_BOT_API` after setting up the inverse proxy server.

## 4. Pushdeer

[PushDeer](https://github.com/easychen/pushdeer)is a self-set up APP-free push service. iOS side is based on Light APP, no need to install APP; Android future will be based on Fast App (under development), currently using APP (has access to MI PUSH, so Xiaomi users can get notifications without opening APP).

1. Apple phones (iOS 14+) can pull up the light app by scanning the code below with the system camera. You can also search for "PushDeer" in the Apple Store to install it (do not install PushDeer self-shelf version). Android Quick App is still under development, you can download and install the Android Beta APP ( [GitHub](https://github.com/easychen/pushdeer/releases/tag/android1.0alpha)| [Gitee](https://gitee.com/easychen/pushdeer/releases/android1.0alpha)). ![img](https://github.com/easychen/pushdeer/raw/main/doc/image/clipcode.png)
2. Sign in with your apple account (or WeChat account - Android only).
3. Switch to the "Devices" tab and click the plus sign in the upper right corner to register the current device.
4. Switch to the `Key` tab, click the plus sign in the upper right corner to create a Key, and fill the Key into the configuration file `PUSHDEER_KEY`.

## 5. GO-CQHTTP

1. Deploy [GO-CQHTTP](https://github.com/Mrs4s/go-cqhttp), see the documentation at [快速开始](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B), or use other frameworks or SDKs that are compatible with the [OneBot-v11](https://github.com/botuniverse/onebot-11) specification.
2. Fill CQHTTP's server `protocol header://IP or domain:port number` with `CQHTTP_URL`, which needs to include the protocol header, e.g. `http://1.2.3.4:5700/` or `https://example.com/`.
3. Configure the sending mode `CQHTTP_MESSAGE_TYPE`, `private` for private chat sending, `group` for group chat sending.
4. Configure the QQ number/group number of the message recipient by filling in `CQHTTP_SEND_ID`to match the sending pattern.
5. If `Access Token` is configured, you need to fill in `CQHTTP_TOKEN`.

## 6. DingTalk group robot

1. Create a pinned group and add a custom bot, see [钉钉开放平台·自定义机器人接入](https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.7f875e594zPr9w#topic-2026027).
2. Fill in `DD_BOT_TOKEN`with the generated Webhook address of `access_token`.
3. Fill `DD_BOT_SECRET` with the key of `add signature` in the creation process.

## 7. Server Chan

1. Go to [Server Chan](https://sct.ftqq.com/) official website to register and bundle with WeChat.
2. Just fill the obtained `send key` into `config.json -> SCKEY`.

Note: The free version of Server Jam has a maximum number of 5 calls per day.

## 8. Push Plus

1. Log in to [pushplus website](http://www.pushplus.plus/) and copy the token to fill in `PUSH_PLUS_TOKEN`.
2. For one-to-many tweets, you need to create a group and enter the group number into `PUSH_PLUS_USER`. One-to-one tweets do not need to be filled in.

## 9. Discord Webhook

1. Go to Server Settings - Integrations, click Create Webhook, click Copy Webhook URL and fill in the configuration file `DISCORD_WEBHOOK`.
2. You can set the bot display name `DISCORD_USERNAME`, bot avatar `DISCORD_AVATAR` (needs to be a web image address) and message card color `DISCORD_COLOR` as needed, read [ Discord Webhooks Guide ](https://birdie0.github.io/discord-webhooks-guide/structure/embeds.html)for details.

## 10. Email

Enter the help page of mail service provider to get SMTP server server and port information, some mailboxes also need to get client authorization code, and fill in the configuration into MAIL part. The default port is 465 (without STARTTLS) or 587 (with STARTTLS).

## 11. CoolPush Cool Push

Note: Cool Push public service is now unavailable and may need to be privatized for deployment.

1. Login to [CoolPush](https://cp.xuthus.cc/), bind QQ number/QQ group and private deployment address, and get `call code Skey`.
2. Fill Skey with `COOL_PUSH_SKEY`, `COOL_PUSH_MODE` supports QQ private chat push/QQ group message push/QQ private private chat push/QQ private group chat push, not support one-to-many push.
3. If you need to dynamically assign a push message to a specific QQ number or group, put the QQ number/group number into `COOL_PUSH_SENDID` and you're done.

## 12. Qmsg

Log in to [Qmsg website](https://qmsg.zendee.cn/)and get the KEY by filling in `QMSG_KEY`.

Note: Qmsg is easily determined to be in violation =\_= and cannot be pushed in group chats (audit does not pass).

## 13. Custom Notifier

```yaml
  CUSTOM_NOTIFIER:
   method:              Required，request method，GET/POST
   url: ''              Required, request URL
   data_type:           Required, the format of the sent data, data/json/params
   headers: {}          Optional, headers to be added
   data: {}             Optional, additional request content
   title_key:           Required, the key of the message title
   desp_key:            Optional, the key of the message details. If this item is empty, the message title and message details will be combined to 'title_key'.
   markdown:            Optional, whether to support markdown, true/false
   retcode_key:         Required, the key of the status code in the response body
   retcode_value:       Required, the status code when push was succeeded in the response body
```

### Examples

#### Send CQHTTP push with custom notifier

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

#### Send Telegram push with custom notifier

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
#### Send Pushplus push with custom notifier

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

#### Send Server chan push with custom notifier

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