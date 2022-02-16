English | [简体中文](./README_ZH.md)

# Genshin Dailynote Helper


<div align="center"> 

[![](https://img.shields.io/badge/Author-Xm798-blueviolet?style=flat-square)](https://github.com/Xm798/)
[![](https://img.shields.io/badge/Github-blue?style=flat-square&logo=Github&logoColor=181717&labelColor=eeeeee&color=181717)](https://github.com/Xm798/Genshin-Dailynote-Helper)
[![](https://img.shields.io/badge/Gitee-blue?style=flat-square&logo=Gitee&logoColor=C71D23&labelColor=eeeeee&color=C71D23)](https://gitee.com/Xm798/Genshin-Dailynote-Helper)
[![](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&color=3776AB)](https://github.com/Xm798/)
[![](https://img.shields.io/github/license/Xm798/Genshin-Dailynote-Helper?style=flat-square)](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/master/LICENSE)
[![](https://img.shields.io/github/contributors/Xm798/Genshin-Dailynote-Helper?style=flat-square)](https://github.com/Xm798/Genshin-Dailynote-Helper/graphs/contributors)
[![](https://img.shields.io/docker/pulls/xm798/genshin-dailynote-helper?style=flat-square)](https://hub.docker.com/r/xm798/genshin-dailynote-helper)
[![](https://img.shields.io/github/v/release/xm798/Genshin-Dailynote-Helper?color=success&style=flat-square)](https://github.com/Xm798/Genshin-Dailynote-Helper/releases)

</div>


## Introduction

Check and push the status of the Genshin Impact resin, commissions, expeditions and homecoin.

**Features**
  - Support running on cloud functions, docker and local machine
  - Support multi-account and multi-role
  - Support push to multiple channels
  - Support CN server (official and channel server) and oversea server
  - Support for skipping certain roles (when multiple roles are bound under the same Mihoyo / Hoyolab account)

**Supports sending a notification when**
  - Resin is about to overflow
  - Today's commission is not completed
  - Overflow of home coin
  - Expeditions completed
  - Resin will overflow during the no-disturb time period

## Content
- [Introduction](#introduction)
- [Content](#content)
- [Examples](#examples)
- [How to use](#how-to-use)
  - [1. Serverless](#1-serverless)
  - [2. Docker](#2-docker)
  - [3. Local](#3-local)
- [Configuration file parameters description](#configuration-file-parameters-description)
  - [Some basic information](#some-basic-information)
  - [Configuration file example](#configuration-file-example)
- [Push method configuration](#push-method-configuration)
- [💬Feedback](#feedback)
- [Changelog](#changelog)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Examples

**Push Example**

<img src="https://s2.loli.net/2022/02/10/fop8SNLW1bqejEQ.png" width="300px" />
<img src="https://s2.loli.net/2022/02/10/TJH8Kly4n7pwazg.png" width="300px" />


**Display of each push channel**

<details>

**Notification Center Preview**

<img src="https://s2.loli.net/2022/02/10/orsvg2lk794aIKZ.png" width="300px" />

**WeChat**

<img src="https://s2.loli.net/2022/02/10/D1n58XafpIWUYZ9.png" width="300px" />

**Bark**

<img src="https://s2.loli.net/2022/02/10/WCyNp9mEUziFt2d.png" width="300px" />

**Server Sauce**

<img src="https://s2.loli.net/2022/02/10/uwpErkDjth4voM7.png" width="300px" />

**Telegram Bot**

<img src="https://s2.loli.net/2022/02/10/l3aN2JWfOtKwn9L.png" width="300px" />

**Pushdeer**

<img src="https://s2.loli.net/2022/02/10/RZb1s6GD8V5Kpt9.png" width="300px" />

**PUSH PLUS**

<img src="https://s2.loli.net/2022/02/10/dnuyhcSqfeR28As.png" width="300px" />

**Pinning group bot**

<img src="https://s2.loli.net/2022/02/10/duZLQUelNRMT5Cc.png" width="300px" />

**Discord**

<img src="https://s2.loli.net/2022/02/10/HdwcDSgqLe8m6kK.png" width="300px" />

**QQ**

<img src="https://s2.loli.net/2022/02/10/UArdhlvXQjomJgM.png" width="300px" />

</details>

## How to use

- Please make sure that dailynote permission is turned on in hoyolab.
- Configure the push method, see section [Push method configuration](#push-method-configuration)
- Fill in the configuration file or configure environment variables, see [Configuration file parameters description](#configuration-file-parameters-description)section for details

### 1. Serverless

**Tencent SCF**

<details>

1. Download the latest code packages from [Release page](https://github.com/Xm798/Genshin-Dailynote-Helper/releases) and domestically from [Gitee mirror](https://gitee.com/Xm798/Genshin-Dailynote-Helper/releases).
   
2. Open [Tencent Cloud SCF](https://console.cloud.tencent.com/scf), log in to your account, and click on "Function Services" - "New".

3. Select "Start from scratch" and enter a function name. If you want to detect international services or push Telegram or Discord, you must select a region other than mainland China, such as Hong Kong. The runtime environment is Python 3.7.

   ![ image-20220209183102030 ](https://s2.loli.net/2022/02/09/BVQ1sZnSfRj2UhF.png)

4. In the function code section, select "Upload zip package locally", select the downloaded package and upload it.

   ![ image-20220209183304497 ](https://s2.loli.net/2022/02/09/HM275iAPhzxRyBn.png)

5. Expand "Advanced Configuration", **change the execution timeout to 90 seconds or longer**, **add environment variable**key to `TZ`and value to `Asia/Shanghai`. If you are in another time zone, please change it to the corresponding time zone, you can check the time zone list at [这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518)(**very important**, otherwise the time will be incorrect).

   ![ image-20220209183900117 ](https://s2.loli.net/2022/02/12/Lw2Hn48jKSGBPJF.png)

6. Expand Trigger Configuration, select Custom Trigger Period and fill in the cron expression. For example, to check every 15 minutes, fill in `0 * /15 * * * * *`, to check every 30 minutes, fill in `0 * /30 * * * * *`, and to trigger every hour exactly, fill in `0 0 * * * * *`. Please note that this interval is consistent with `CHECK_INTERVAL` in the configuration file to run the bedtime check function.

   ![image.png](https://s2.loli.net/2022/02/14/KQGvlWOq5EiARY8.png)

7. Jump to the **Function Management - Function Code** page, find `dailynotehelper/config/config.example.yaml` in the directory, right-click and rename it to `config.yaml`, **and fill in your configuration**(environment variables are not supported).

    ![ image-20220209184555981 ](https://s2.loli.net/2022/02/09/vxkaqoOfVw6hBgW.png)

8. Click **Deploy and Test** below to see if the log test is working properly.

</details>

### 2. Docker

i. **Using Docker Image**

  1. Click [here](https://raw.githubusercontent.com/Xm798/Genshin-Dailynote-Helper/master/dailynotehelper/config/config.example.yaml) or get the sample configuration file from this project path `dailynotehelper/config/config.example.yaml` and fill it out, renaming it to `config.yaml`.

  2. Run, `/PATH-to-YOUR-CONFIG/config.yaml` is the path to your local configuration file, you need to fill it according to the actual situation. The environment variable `TZ` is the time zone of your location (**very important**, otherwise the time will be incorrect), you can check the list of time zones at [here](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518).


     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --env TZ=Asia/Shanghai
     --restart=always \
     --name=genshin-dailynote-helper \
     xm798/genshin-dailynote-helper:latest
     ```
     If you are running on a chinese mainland machine, you can use the image on Tencent Cloud.

     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --env TZ=Asia/Shanghai
     --restart=always \
     --name=genshin-dailynote-helper \
     ccr.ccs.tencentyun.com/xm798/genshin-dailynote-helper:latest
     ```

ii. **Using docker-compose**

  Clone the project, fill in the configuration file and build it to run. The environment variable TZ is the time zone of your location, you can check the list of time zones at [here](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518).


  ```sh
  git clone https://github.com/Xm798/Genshin-Dailynote-Helper.git
  cd Genshin-Dailynote-Helper
  cp ./dailynotehelper/config/config.example.yaml ./dailynotehelper/config/config.yaml
  docker-compose up -d
  ```

### 3. Local

1. Install [python3](https://www.python.org) environment, version >= 3.7.

2. Download the project and install the dependencies.


   ```shell
   git clone https://github.com/Xm798/Genshin-Dailynote-Helper.git
   cd Genshin-Dailynote-Helper
   pip3 install -r requirements.txt
   ```

3. Modify configuration

   Copy `./dailynotehelper/config/config.example.yaml` and save it as `config.yaml`and fill in the configuration information.


   ```shell
   cp ./dailynotehelper/config/config.example.yaml ./dailynotehelper/config/config.yaml
   vim ./dailynotehelper/config/config.yaml
   ```

4. Running Projects

   ```shell
   python3 index.py
   ```

## Configuration file parameters description

### Some basic information

1. RUN_ENV, only for CN server

    Specify the runtime environment, use `cloud` for running on domestic cloud service providers, otherwise use `local`, only effective for national service. This option is designed to provide compatibility options for users running on domestic cloud servers. `cloud` is an old version of the API, which was once unusable and is now restored. However, since MiYosha has been fully replaced with the new API, the default is to run with the `local` environment, which is the new API. For more information, please refer to [米游社可能已经禁止国内特定VPS服务商的IP或ASN](https://github.com/Arondight/Adachi-BOT/issues/522).
    
2. **COOKIE**:
      1. Open [Mihoyo bbs](https://bbs.mihoyo.com/ys)and login for cn server, open [Hoyolab](https://www.hoyolab.com/)and login for oversea server.
      2. Press F12 to open Developer Tools.
      3. Switching the developer tools to the Console tab.
      4. Copy the code below and paste it in the console, press enter and the result is pasted into the configuration file.

    ```javascript
    javascript:(()=>{_=(n)=>{for(i in(r=document.cookie.split(';'))){var a=r[i].split('=');if(a[0].trim()==n)return a[1]}};c=_('account_id')||alert('Invalid Cookie,please relogin!');c&&confirm('Copy cookies to clipboard?')&&copy(document.cookie)})();
    ```

3. **EXCLUDE_UID**
   
   If you have multiple characters bound to your MiYosha/Hoyolab account, but don't want to receive alerts for some of them, you can write their UIDs here, one per line.

### Configuration file example


```yaml
# PROJECT: Genshin DailyNote Notice Helper Config File
# Author: Xm798
# Github: https://github.com/Xm798/Genshin-Dailynote-Helper

# Caution: Don't forget to use quotes if the string contains special characters.

base:
  # Language, support zh_CN or en_US.
  LANGUAGE: zh_CN
  RUN_ENV: local
  # Account information, replace COOKIEx below with your COOKIE. Fill in a new line for multiple accounts, remove the #, and start with - .
  # CN COOKIE
  COOKIE: 
    - 'COOKIE1'
    #- 'COOKIE2'
  # OVERSEA COOKIE
  COOKIE_HOYOLAB:
    #- 'COOKIE1'
    #- 'COOKIE2'
  # Exclude UIDs, UIDs in this list will not be detected
  EXCLUDE_UID:
    #- 100000001
    #- 500000001
  # Whether to display the UID with the middle three digits hidden in the message, true or false
  DISPLAY_UID: true

# Display information settings, true or false
receive_info: 
  # Original Resin
  RESIN_INFO: true
  # Commission requests
  COMMISSION_INFO: true
  # Expeditions
  EXPEDITION_INFO: true
  # Resin discount of trounce
  TROUNCE_INFO: true
  # Home coin
  HOMECOIN_INFO: true

# Receive reminder settings
receive_notice:
  # The original resin reminder threshold, fill in 0 to close the reminder
  RESIN_THRESHOLD: 140
  #  Reminder time when the commissions is not completed, if not filled, the reminder will be closed
  COMMISSION_NOTICE_TIME: '21:00'
  # Expeditions completion reminder, true or false
  EXPEDITION_NOTICE: true
  # Whether to wait until all expeditions are completed before sending reminders，true or false
  WAIT_ALL_EXPEDITION: false
  # Hom ecoin overflow reminder，true or false
  HOMECOIN_NOTICE: true

time:
  # Check interval (minutes), please make sure it is consistent with the trigger setting when using serverless, so that the bedtime check can be performed
  CHECK_INTERVAL: 30
  # Do Not Disturb Time
  SLEEP_TIME: '23:00-07:00'

# Push channel settings
notifier:

# WeChat Work
  # Company ID
  WW_ID: ''
  # Agent ID of WeChat Work
  WW_APP_AGENTID: 
  # App SECRET of WeChat Work
  WW_APP_SECRET: ''
  # User ID for receiving push, multiple recipients are separated by '|', all users fill in @all
  WW_APP_USERID: '@all'

# 企业微信机器人
  WW_BOT_KEY: ''

# BARK
  # BARK's full push address, such as 'https://api.day.app/YourKey'
  BARK_URL: ''
  # Customize the Bark group, if not filled, the default group will be used.
  BARK_GROUP: 
  # Customize the Bark notification icon, if not filled, the custom icon will not be used.
  BARK_ICON: 'https://i2.hdslb.com/bfs/face/d2a95376140fb1e5efbcbed70ef62891a3e5284f.jpg@240w_240h_1c_1s.png'
  # Whether save in Bark, 1 is to save, 0 is not to save, leave blank to use the default rule
  BARK_ARCHIVE: 
  # BARK Time-sensitive notification settings, active / timeSensitive / passive, leave blank to use default rules
  BARK_LEVEL: 

# Telegram bot
  # Telegram API Address
  TG_BOT_API: api.telegram.org
  # Telegram Bot Token
  TG_BOT_TOKEN: ''
  # User id to receive push
  TG_USER_ID: 

# Pushdeer
  PUSHDEER_KEY: 

# CQHTTP
  # API address of CQHTTP, format: protocol header://IP-or-domain-name:port-number
  CQHTTP_URL: 'http://1.2.3.4:5700'
  # QQ number/group number to receive messages
  CQHTTP_SEND_ID: 
  # Message sending method, 'private' is for private chat, 'group' is for group chat
  CQHTTP_MESSAGE_TYPE: private
  # Authentication TOKEN of CQHTTP, no need to fill in if not set
  CQHTTP_TOKEN: ''

# DingTalk group robot
  # Access_token of DingTalk robot
  DD_BOT_TOKEN: ''
  # DingTalk robot signing key, no need to fill in if not set
  DD_BOT_SECRET: ''

# Server chan
  SCTKEY: 

# Push plus
  # Token of PushPlus
  PUSH_PLUS_TOKEN: 
  # PushPlus One-to-many push group id, leave blank for one-to-one push
  PUSH_PLUS_USER: 

# Coolpush
  # SKEY of Coolpush
  COOL_PUSH_SKEY: 
  # Cool push push mode，send / psend / group / pgroup
  COOL_PUSH_MODE: psend
  # Coolpush designated recipient QQ number/group number
  COOL_PUSH_SENDID: 

# QMSG
  QMSG_KEY: 

# Discord Webhook
  # Discord Webhook url
  DISCORD_WEBHOOK: ''
  # Robot name, leave it blank and use the default
  DISCORD_USERNAME: 
  # The avatar of the robot, which must be a web image, the default is used if not filled
  DISCORD_AVATAR: ''
  # Convert hex color to decimal
  DISCORD_COLOR: 15553898

# IGOT
  IGOT_KEY: 

# MAIL
  # mail smtp server
  MAIL_HOST: ''
  # smtp port
  MAIL_PORT: 465
  # Whether to enable STARTTLS，true or false
  MAIL_STARTTLS: false
  # Sender's email account
  MAIL_USERNAME: ''
  # Sender's email password (or authorization code)
  MAIL_PASSWORD: ''
  # recipient email address
  MAIL_TO: ''
```


## Push method configuration

**Details of the supported push channels currently are listed below**, recommended:

- **WeChat Push**: Using WeChat Work.
- **System notification push**: Bark or Pushdeer for iOS users, Pushdeer for MIUI users.
- **Full Platform Push**: Use Telegram.
- **QQ Push**: Use go-cqhttp.

|                 Push Channels                 | Support Situation |              Push Channel              |                  Remark                  |
| :-------------------------------------------: | :---------------: | :------------------------------------: | :--------------------------------------: |
|         [WeChat Work](#1-wechat-work)         |    ✅ Supported    |         WeChat (All Platforms)         |               Recommend ⭐             |
|    [WeChat Work group bot](#1-wechat-work)    |    ✅ Supported    |         WeChat (All Platforms)         |                                         |
|                [Bark](#2-bark)                |    ✅ Supported    |          APP（only for iOS）           |               Recommend ⭐              |
|        [Telegram Bot](#3-telegram-bot)        |    ✅ Supported    |       Telegram（All platforms）        |               Recommend ⭐              |
|            [Pushdeer](#4-pushdeer)            |    ✅ Supported    | Light APP(iOS)/APP(Android)/APP(MacOS) |  Recommended for iOS and Xiaomi devices  |
|           [go-cqhttp](#5-go-cqhttp)           |    ✅ Supported    |                   QQ                   |       Need to deploy by yourself         |
| [DingTalk group bot](#6-dingtalk-group-robot) |    ✅ Supported    |             DingTalk group             |                                          |
|        [Server Sauce](#7-server-chan)         |    ✅ Supported    |       Multi-channel aggregation        | The free version is limited to 5 per day |
|           [pushplus](#8-push-plus)            |    ✅ Supported    |       Multi-channel aggregation        |                                          |
|     [Discord Webhook](#9-discord-webhook)     |    ✅ Supported    |                Discord                 |                                          |
|              [Email](#10-email)               |    ✅ Supported    |                                        |                                          |
|           [Cool Push](#11-coolpush)           |    ✅ Supported    |                   QQ                   |                                          |
|            [Qmsg Sauce](#12-qmsg)             |    ✅ Supported    |                   QQ                   |                                          |
|                     IGOT                      |   🛠️ Not tested    |                                        |                                          |

### 1. Wechat Work

i. WeChat Work self-built application

Push to WeChat Work/WeChat through self-built application is recommended.

<details>

> Thanks to Server Sauce for this part of the tutorial.

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

   1. Go to "My Business" → " [微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)", pull to the bottom and check "Allow members to receive and reply to chat messages in WeChat plugin" ![img](https://s2.loli.net/2022/02/06/sF8MS3ZBUCueN7I.jpg)
   2. Turn off the restriction of "Receive messages only in Enterprise Wechat" in "Me" → "Settings" → "New Message Notification" in Enterprise Wechat client ![img](https://s2.loli.net/2022/02/06/OdyJslVKtekTIAX.jpg)

</details>

ii. WeChat Work group robot

<details>

After adding a bot to a group in the terminal, the creator can look at the bot-specific webhookurl on the bot details page and fill in the contents after `key=` in the configuration file `WW_BOT_KEY`, for example `693a91f6-7xxx-4bc4-97a0-0ec2sifa5aaa`.

</details>

### 2. Bark

<details>

1. Download and open the [Bark](https://github.com/Finb/Bark) App from the AppStore and fill in the full push link (e.g. `https://api.day.app/xxxxxxx`) into `BARK_URL` to do so.
2. Support some optional configurations, such as custom message grouping `BARK_GROUP`, custom notification icon `BARK_ICON`, custom message saving `BARK_ARCHIVE`, time-sensitive notification `BARK_LEVEL`.
     - BARK_GROUP: Specify the push message group, you can view the push by group in the history.
     - BARK_ICON: Specify the push message icon, only supported by iOS15 or above, e.g.: `http://day.app/assets/images/avatar.jpg`.
     - BARK_ARCHIVE: Specify whether the push message should be saved to the history, 1 is to save, other values are not to save. If this parameter is not specified, the push information will be saved or not according to the setting in APP.
     - BARK_LEVEL: Sets the time-sensitive notification.
         - `active`: The default value when not set, the system will light up the screen to display the notification immediately.
         - `timeSensitive`: time-sensitive notifications that can be displayed in the focused state.
         - `passive`: Only notifications are added to the notification list, and no screen will be lit up for alerts.

</details>

### 3. Telegram Bot

<details>

1. To create a bot: Open [@BotFather](https://t.me/botfather), enter `/newbot` to create a new bot. Follow the prompts and enter: Bot name, Bot account (needs to end with bot), copy the obtained Token and fill in the configuration file `TG_BOT _TOKEN`. ![ image-20220206143711051 ](https://s2.loli.net/2022/02/06/MBX7EmTJZDtzq93.png)
2. Click on the link `t.me/你的botid `in the message box to jump to your bot and click `START` to associate your bot.
3. Open [@userinfobot](https://t.me/userinfobot), send `/start`, get your ID and fill in the profile `TG_USER_ID`.
4. To use Telegram bot push, you need to configure a proxy or fill in the configuration file `TG_BOT_API` after setting up the inverse proxy server. Here is a copy of my CF Workers based anti-generation API `tgbotapi.xm.mk` for use.

</details>

### 4. Pushdeer

<details>

[PushDeer](https://github.com/easychen/pushdeer)is a self-set up APP-free push service. iOS side is based on Light APP, no need to install APP; Android future will be based on Fast App (under development), currently using APP (has access to MI PUSH, so Xiaomi users can get notifications without opening APP).

1. Apple phones (iOS 14+) can pull up the light app by scanning the code below with the system camera. You can also search for "PushDeer" in the Apple Store to install it (do not install PushDeer self-shelf version). Android Quick App is still under development, you can download and install the Android Beta APP ( [GitHub](https://github.com/easychen/pushdeer/releases/tag/android1.0alpha)| [Gitee](https://gitee.com/easychen/pushdeer/releases/android1.0alpha)). ![img](https://github.com/easychen/pushdeer/raw/main/doc/image/clipcode.png)
2. Sign in with your apple account (or WeChat account - Android only).
3. Switch to the "Devices" tab and click the plus sign in the upper right corner to register the current device.
4. Switch to the `Key` tab, click the plus sign in the upper right corner to create a Key, and fill the Key into the configuration file `PUSHDEER_KEY`.

</details>

### 5. GO-CQHTTP

<details>

1. Deploy [GO-CQHTTP](https://github.com/Mrs4s/go-cqhttp), see the documentation at [快速开始](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B), or use other frameworks or SDKs that are compatible with the [OneBot-v11](https://github.com/botuniverse/onebot-11) specification.
2. Fill CQHTTP's server `protocol header://IP or domain:port number` with `CQHTTP_URL`, which needs to include the protocol header, e.g. `http://1.2.3.4:5700/` or `https://example.com/`.
3. Configure the sending mode `CQHTTP_MESSAGE_TYPE`, `private` for private chat sending, `group` for group chat sending.
4. Configure the QQ number/group number of the message recipient by filling in `CQHTTP_SEND_ID`to match the sending pattern.
5. If `Access Token` is configured, you need to fill in `CQHTTP_TOKEN`.

</details>

### 6. DingTalk group robot

<details>

1. Create a pinned group and add a custom bot, see [钉钉开放平台·自定义机器人接入](https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.7f875e594zPr9w#topic-2026027).
2. Fill in `DD_BOT_TOKEN`with the generated Webhook address of `access_token`.
3. Fill `DD_BOT_SECRET` with the key of `add signature` in the creation process.
</details>

### 7. Server Chan

<details>

1. Go to [Server Chan](https://sct.ftqq.com/) official website to register and bundle with WeChat.
2. Just fill the obtained `send key` into `config.json -> SCKEY`.

Note: The free version of Server Jam has a maximum number of 5 calls per day.

</details>

### 8. Push Plus

<details>

1. Log in to [pushplus website](http://www.pushplus.plus/) and copy the token to fill in `PUSH_PLUS_TOKEN`.
2. For one-to-many tweets, you need to create a group and enter the group number into `PUSH_PLUS_USER`. One-to-one tweets do not need to be filled in.

</details>

### 9. Discord Webhook

<details>

1. Go to Server Settings - Integrations, click Create Webhook, click Copy Webhook URL and fill in the configuration file `DISCORD_WEBHOOK`.
2. You can set the bot display name `DISCORD_USERNAME`, bot avatar `DISCORD_AVATAR` (needs to be a web image address) and message card color `DISCORD_COLOR` as needed, read [ Discord Webhooks Guide ](https://birdie0.github.io/discord-webhooks-guide/structure/embeds.html)for details.

</details>

### 10. Email

<details>

Enter the help page of mail service provider to get SMTP server server and port information, some mailboxes also need to get client authorization code, and fill in the configuration into MAIL part. The default port is 465 (without STARTTLS) or 587 (with STARTTLS).

</details>

### 11. CoolPush Cool Push

<details>

Note: Cool Push public service is now unavailable and may need to be privatized for deployment.

1. Login to [CoolPush](https://cp.xuthus.cc/), bind QQ number/QQ group and private deployment address, and get `call code Skey`.
2. Fill Skey with `COOL_PUSH_SKEY`, `COOL_PUSH_MODE` supports QQ private chat push/QQ group message push/QQ private private chat push/QQ private group chat push, not support one-to-many push.
3. If you need to dynamically assign a push message to a specific QQ number or group, put the QQ number/group number into `COOL_PUSH_SENDID` and you're done.

</details>

### 12. Qmsg

<details>

Log in to [Qmsg website](https://qmsg.zendee.cn/)and get the KEY by filling in `QMSG_KEY`.

Note: Qmsg sauce is easily determined to be in violation =\_= and cannot be pushed in group chats (audit does not pass).

</details>


## 💬Feedback

[![](https://img.shields.io/badge/%20-QQ%20Group-blue?style=for-the-badge&logo=Tencent%20QQ&logoColor=EB1923&labelColor=eeeeee&color=EB1923)](https://jq.qq.com/?_wv=1027&k=CnNxc9hp)
[![](https://img.shields.io/badge/%20-Telegram%20Group-blue?style=for-the-badge&logo=Telegram&logoColor=26A5E4&labelColor=eeeeee&color=26A5E4)](https://t.me/+QtSxha7rXsc2ZTg1)



## Changelog

### v2.1.2（2022-02-14）

New Features:

- Add multilingual internationalization support and add English version. (But need someone to proofread the English translation.)

### v2.1.1 (2022-02-13)

New Features:

- Support setting whether to wait for all exploration dispatch to be completed before reminding, and adding the field `WAIT_ALL_EXPEDITION` to the configuration file
  
Bug Fixes:

- Fix the problem that the switch of whether to receive information of Dongtianbao money does not work

### v2.1.0 (2022-02-12)

New Features:

- New international service support
- New function of blocking some roles

Bug Fixes:

- Fix the problem of abnormal exit when API request fails

### v2.0.1 (2022-02-10)

New Features:

- Support email push via custom SMTP server

Bug Fixes:

- Fix the problem that some push configurations are abnormal when they are empty

### v2.0.0 (2022-02-09)

BREAKING CHANGE:

- Change the configuration file to yaml format

New Features:

- Support multi-account and multi-role
- Support for cloud function deployment
- Discord push support

Removed.

- Remove QQ active query module

Others:

- Adding a domestic docker image
- Optimize push experience
- Refactoring of some modules

<details>

### v1.3.3 (2022-02-06)

New Features:

- New Pushdeer push channel
- Remove old Serverchan push channel
- Optimize push content

Bug Fixes:

- Adjust the cqhttp parameter to merge `CQHTTP_IP` and `CQHTTP_PORT` into `CQHTTP_URL`
- Adjust the rendering style of some channels

### v1.3.2 (2022-01-12)

Bug Fixes

### v1.3.1 (2022-01-10)

New Features:

- Support for custom BARK push servers

Bug Fixes:

- Fix the problem of BARK push status detection error

### v1.3.0 (2022-01-10)

New Year

New Features:

- Add Caveman treasure money information, support setting Caveman treasure money overflow alert, new `RECEIVE_HOMECOIN_ALERT` field in configuration file
- Add a bedtime check, if the resin overflows during sleep will send an alert before sleep
- Add API switching options to support specifying older APIs when running on cloud servers
- Optimize message layout

Bug Fixes:

- Fix the problem of invalid resin overflow prompt
- Update the information of exploring and sending new characters
- Fix Noelle character information error
- Optimize hibernation logic

### v1.2.5 (2021-12-24)

Bug Fixes.

- Synchronize the MiTAC API changes with the new API.

### v1.2.4 (2021-11-24)

Bug Fixes.

- Fix an abnormal exit when a cookie error occurs

### v1.2.3 (2021-11-23)

New Features:

- CQHTTP push IP field support protocol header to support HTTPS

### v1.2.2 (2021-11-10)

New Features:

- Optimize the logic of daily commission reminder time judgment
- Add the judgment of daily commission rewards collection, so you will no longer be mistaken for not completing the commission after going to other worlds to collect rewards.

### v1.2.1 (2021-11-01)

Bug Fixes.

- Fix CQ-HTTP push authentication error, please note **profile field change**for users using CQ-HTTP.

New Features:

- Add support for group push mode
- Add custom port support

### v1.2.0 (2021-11-01)

New Features:

- Support night hibernation, no more late night non-stop disturbance
- Logs add per-round check resin value display

Bug Fixes.
- Fix cqhttp push error prompt
- Some fields of the configuration file are changed to optional configuration

### v1.1.2 (2021-10-29)

New Features:

- Add cqhttp push

Others:
- Update documentation

### v1.1.1 (2021-10-28)

New Features:

- Add a reminder of the completion of exploration dispatch
- Optimize alert titles

### v1.1.0 (2021-10-28)

New Features:
- Optimize alert logic
- Add account information display

Bug Fixes:
- Fix the problem of incorrect hibernation time

</details>

## Acknowledgements

|                                                   Project                                                   |                     Author                     |                                                License                                                |             Comment             |
| :---------------------------------------------------------------------------------------------------------: | :--------------------------------------------: | :---------------------------------------------------------------------------------------------------: | :-----------------------------: |
| [ genshin_task-resin-expedition_alert ](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert) | [yaomeng0722](https://gitlab.com/yaomeng0722/) | [MIT LICENSE](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert/blob/master/LICENSE) | Initial version of this project |
|                                [onepush](https://github.com/y1ndan/onepush)                                 |      [y1ndan](https://gitlab.com/y1ndan/)      |                  [MIT LICENSE](https://github.com/y1ndan/onepush/blob/main/LICENSE)                   |      message push channel       |
|                [ genshin-checkin-helper ](https://gitlab.com/y1ndan/genshin-checkin-helper)                 |      [y1ndan](https://gitlab.com/y1ndan/)      |         [GPLv3 LICENSE](https://gitlab.com/y1ndan/genshin-checkin-helper/-/blob/main/LICENSE)         |         API call method         |
|                                                      -                                                      |      [yllhwa](https://github.com/yllhwa)       |                                                   -                                                   | DS encryption algorithm reverse |



## License

[GNU GPLv3](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/master/LICENSE)


> Translated by DeepL and Google from Simplified Chinese.