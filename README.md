# 原神实时便笺提醒小助手 | Genshin Dailynote Helper


检查并推送原神内树脂、委托、周本、探索派遣和洞天宝钱情况。

支持多账号，支持多渠道同时推送，目前只支持国服。

支持当如下情况时发送提醒：
  - 树脂即将溢出
  - 今日委托未完成
  - 洞天宝钱溢出
  - 探索派遣已完成



## 目录
- [示例](#示例)
- [使用方法](#使用方法)
  - [1. 云函数运行](#1-云函数运行)
  - [2. Docker 运行](#2docker-运行)
  - [3. 本地运行](#3本地运行)
- [配置文件参数说明](#配置文件参数说明)
  - [一些基础信息](#一些基础信息)
  - [配置文件示例](#配置文件示例)
- [推送方式配置](#推送方式配置)
- [更新日志](#更新日志)
- [致谢](#致谢)
- [License](#license)

## 示例

**推送示例**

<img src="https://s2.loli.net/2022/02/10/fop8SNLW1bqejEQ.png" width="300px" />
<img src="https://s2.loli.net/2022/02/10/TJH8Kly4n7pwazg.png" width="300px" />


**各推送渠道展示**

<details>

**通知中心预览**

<img src="https://s2.loli.net/2022/02/10/orsvg2lk794aIKZ.png" width="300px" />

**微信**

<img src="https://s2.loli.net/2022/02/10/D1n58XafpIWUYZ9.png" width="300px" />

**Bark**

<img src="https://s2.loli.net/2022/02/10/WCyNp9mEUziFt2d.png" width="300px" />

**Server 酱**

<img src="https://s2.loli.net/2022/02/10/uwpErkDjth4voM7.png" width="300px" />

**Telegram Bot**

<img src="https://s2.loli.net/2022/02/10/l3aN2JWfOtKwn9L.png" width="300px" />

**Pushdeer**

<img src="https://s2.loli.net/2022/02/10/RZb1s6GD8V5Kpt9.png" width="300px" />

**PUSH PLUS**

<img src="https://s2.loli.net/2022/02/10/dnuyhcSqfeR28As.png" width="300px" />

**钉钉群机器人**

<img src="https://s2.loli.net/2022/02/10/duZLQUelNRMT5Cc.png" width="300px" />

**Discord**

<img src="https://s2.loli.net/2022/02/10/HdwcDSgqLe8m6kK.png" width="300px" />

**QQ**

<img src="https://s2.loli.net/2022/02/10/UArdhlvXQjomJgM.png" width="300px" />

</details>

## 使用方法

- 请确保米游社的实时便笺权限已经打开
- 配置推送方式，参见[推送方式配置](#%E6%8E%A8%E9%80%81%E6%96%B9%E5%BC%8F%E9%85%8D%E7%BD%AE)部分
- 填写配置文件或配置环境变量，详情参见[配置文件参数说明](#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E)部分

### 1. 云函数运行

1. 从 [Release 页面](https://github.com/Xm798/Genshin-Dailynote-Helper/releases) 下载最新代码包，国内可从 [Gitee镜像](https://gitee.com/Xm798/Genshin-Dailynote-Helper/releases) 下载。
   
2. 打开[腾讯云云函数控制台](https://console.cloud.tencent.com/scf)，登录账号，点击“函数服务”-“新建”。

3. 选择“从头开始”，输入一个函数名，地域在国内随便选择（如需推送 Telegram 或 Discord，选中国香港地区），运行环境为 Python3.7。

   ![image-20220209183102030](https://s2.loli.net/2022/02/09/BVQ1sZnSfRj2UhF.png)

4. 函数代码部分，选择“本地上传 zip 包”，选择下载的程序包并上传。

   ![image-20220209183304497](https://s2.loli.net/2022/02/09/HM275iAPhzxRyBn.png)

5. 展开“高级配置”，**修改执行超时时间为 120 秒或更长**，**添加环境变量** key 为 `TZ`，value 为 `Asia/Shanghai`（**十分重要**，否则时间不正确）。

   ![image-20220209183900117](https://s2.loli.net/2022/02/09/N4ubS2oFEGdhBVr.png)

6. 展开触发器配置，选择自定义触发周期，填写 cron 表达式。例如：每15分钟检查一次，填写`* */15 * * * * *`，每30分钟检查一次，填写`* */30 * * * * *`，每小时整点触发，填写`0 0 * * * * *`。该间隔请注意与配置文件中`CHECK_INTERVAL`一致，以便运行睡前检查功能。

   ![image-20220209184423821](https://s2.loli.net/2022/02/09/OYZsChGzdVW6oqx.png)

7. 跳转到 **函数管理 - 函数代码**页面，在目录中找到`dailynotehelper/config/config.example.yaml`，右键重命名为`config.yaml`，**并填写你的配置**（不支持环境变量）。

    ![image-20220209184555981](https://s2.loli.net/2022/02/09/vxkaqoOfVw6hBgW.png)

8. 点击下方“**部署并测试**”，查看日志测试是否运行正常。

### 2. Docker 运行

i. **使用镜像**

  1. 点击 [链接](https://raw.githubusercontent.com/Xm798/Genshin-Dailynote-Helper/master/dailynotehelper/config/config.example.yaml) 或从本项目路径`dailynotehelper/config/config.example.yaml`提取示例配置文件并填写，重命名为`config.yaml`。

  2. 运行，`/PATH-to-YOUR-CONFIG/config.yaml`是你本地配置文件的路径，需要根据实际情况填写。

     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --restart=always \
     --name=genshin-dailynote-helper \
     xm798/genshin-dailynote-helper:latest
     ```
     若在国内机器运行，可使用在腾讯云的镜像。
     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --restart=always \
     --name=genshin-dailynote-helper \
     ccr.ccs.tencentyun.com/xm798/genshin-dailynote-helper:latest
     ```

ii. **使用 docker-compose**

  克隆项目，填写配置文件后构建运行。

  ```sh
  git clone https://github.com/Xm798/Genshin-Dailynote-Helper.git
  cd Genshin-Dailynote-Helper
  cp ./dailynotehelper/config/config.example.yaml/ dailynotehelper/config/config.yaml
  docker-compose up -d
  ```

### 3. 本地运行

1. 安装 [python3](https://www.python.org) 环境，版本>=3.7。

2. 下载项目并安装依赖，

   ```shell
   # 国内可考虑使用 Gitee 镜像: https://gitee.com/Xm798/Genshin-Dailynote-Helper
   git clone https://github.com/Xm798/Genshin-Dailynote-Helper.git
   cd Genshin-Dailynote-Helper
   pip3 install -r requirements.txt
   ```

3. 修改配置

   复制 `./dailynotehelper/config/config.example.yaml` 并另存为 `config.yaml`，填入配置信息。

   ```shell
   cp ./dailynotehelper/config/config.example.yaml ./dailynotehelper/config/config.yaml
   vim ./dailynotehelper/config/config.yaml
   ```

4. 运行项目
   ```shell
   python3 index.py
   ```

## 配置文件参数说明

### 一些基础信息

1. RUN_ENV：

    指定运行环境，国内云服务商运行使用`cloud`，否则使用`local`。该选项旨在为在国内云服务器运行的用户提供兼容性选项，`cloud`为旧版 API，曾经无法使用，现在又恢复了。但由于米游社已全面更换为新的 API，因此默认使用`local`环境即新 API 运行。详情参考：[米游社可能已经禁止国内特定 VPS 服务商的 IP 或 ASN](https://github.com/Arondight/Adachi-BOT/issues/522)。

2. **COOKIE**: 
   
      1. 打开[米游社社区](https://bbs.mihoyo.com/ys)并登录； 
      2. 按 F12 打开开发者工具； 
      3. 将开发者工具切换至控制台(Console)页签； 
      4. 复制下方的代码，并将其粘贴在控制台中，按下回车，结果粘贴到配置文件中。 
    ```javascript
    javascript:(()=>{_=(n)=>{for(i in(r=document.cookie.split(';'))){var a=r[i].split('=');if(a[0].trim()==n)return a[1]}};c=_('account_id')||alert('无效的Cookie,请重新登录!');c&&confirm('将Cookie复制到剪贴板?')&&copy(document.cookie)})();
    ```

### 配置文件示例

```yaml
base:
  # 运行环境，若云服务商环境下运行出错，请尝试修改为 cloud 。
  RUN_ENV: local
  # 账号信息，将下面的 COOKIEx 替换为你的 COOKIE。多账号换行填写，去掉 #，以 - 开头。
  COOKIE: 
    - 'COOKIE1'
    #- 'COOKIE2'
    #- 'COOKIE3'
  # 消息中是否显示隐去中间三位数字的 UID，true or false
  DISPLAY_UID: true

# 展示信息设置，true or false
receive_info: 
  # 原粹树脂
  RESIN_INFO: true
  # 委托任务
  COMMISSION_INFO: true
  # 探索派遣
  EXPEDITION_INFO: true
  # 征讨领域（周本）树脂减半信息
  TROUNCE_INFO: true
  # 洞天宝钱
  HOMECOIN_INFO: true

# 接收提醒设置
receive_notice:
  # 原粹树脂提醒阈值，填 0 则关闭提醒
  RESIN_THRESHOLD: 140
  #  委托未完成的提醒时间，不填则关闭提醒
  COMMISSION_NOTICE_TIME: '21:00'
  # 探索派遣完成提醒，true or false
  EXPEDITION_NOTICE: true
  # 洞天宝钱溢出提醒，true or false
  HOMECOIN_NOTICE: true

time:
  # 检查间隔（分钟），云函数运行时请确保与触发器设置一致，以便执行睡前检查
  CHECK_INTERVAL: 30
  # 免打扰时间
  SLEEP_TIME: '23:00-07:00'

# 推送通道设置
notifier:

# 企业微信
  # 企业ID
  WW_ID: ''
  # 企业微信应用 ID
  WW_APP_AGENTID: 
  # 企业微信应用 SECRET
  WW_APP_SECRET: ''
  # 接收推送的用户ID，多个接收者用‘|’分隔，全部用户填写 @all
  WW_APP_USERID: '@all'

# 企业微信机器人
  WW_BOT_KEY: ''

# BARK
  # BARK 完整推送地址，如'https://api.day.app/YourKey'
  BARK_URL: ''
  # 自定义 Bark 分组，不填则使用默认分组
  BARK_GROUP: 
  # 自定义 Bark 通知图标，不填则不使用自定义图标
  BARK_ICON: 'https://i2.hdslb.com/bfs/face/d2a95376140fb1e5efbcbed70ef62891a3e5284f.jpg@240w_240h_1c_1s.png'
  # 自定义 Bark 保存，1 为保存，0 为不保存，不填使用默认规则
  BARK_ARCHIVE: 
  # BARK 时效性通知设置，active / timeSensitive / passive，不填使用默认规则
  BARK_LEVEL: 

# Telegram bot
  # Telegram API 地址
  TG_BOT_API: api.telegram.org
  # Telegram Bot Token
  TG_BOT_TOKEN: ''
  # 接收推送的用户 id
  TG_USER_ID: 

# Pushdeer
  PUSHDEER_KEY: 

# CQHTTP
  # CQHTTP 的 API 地址，格式：协议头://IP 或域名:端口号
  CQHTTP_URL: 'http://1.2.3.4:5700'
  # 接收消息的 QQ 号码/群号码
  CQHTTP_SEND_ID: 
  # 消息发送方式，private为私聊，group为群聊
  CQHTTP_MESSAGE_TYPE: private
  # CQHTTP 的鉴权 TOKEN，未设置不需要填写
  CQHTTP_TOKEN: ''

# 钉钉群机器人
  # 钉钉机器人的 access_token
  DD_BOT_TOKEN: ''
  # 钉钉机器人加签密钥，未设置不需要填写
  DD_BOT_SECRET: ''

# Server chan
  SCTKEY: 

# Push plus 推送加
  # PushPlus 推送 token
  PUSH_PLUS_TOKEN: 
  # PushPlus 一对多推送群组 id，一对一推送不填
  PUSH_PLUS_USER: 

# 酷推
  # 酷推 SKEY
  COOL_PUSH_SKEY: 
  # 酷推推送模式，send / psend / group / pgroup
  COOL_PUSH_MODE: psend
  # 酷推指定接收方 QQ 号/群号
  COOL_PUSH_SENDID: 

# QMSG 酱
  QMSG_KEY: 

# Discord Webhook
  # Discord Webhook 地址
  DISCORD_WEBHOOK: ''
  # 机器人名字，不填使用默认
  DISCORD_USERNAME: 
  # 机器人头像，须为 web 图片，不填使用默认
  DISCORD_AVATAR: ''
  # 将颜色16进制转为十进制
  DISCORD_COLOR: 15553898

# IGOT
  IGOT_KEY: 
```


## 推送方式配置

**目前支持的推送渠道详情如下表**，建议：

- **微信推送**：使用企业微信；
- **系统通知推送**：iOS 用户使用 Bark 或 Pushdeer，MIUI 用户使用 Pushdeer；
- **全平台推送**：使用 Telegram 或企业微信；
- **QQ 推送**：自行部署 go-cqhttp 并使用。

|               推送渠道                | 支持情况 |             推送通道             |          备注           |
| :-----------------------------------: | :------: | :------------------------------: | :---------------------: |
|        [企业微信](#1-企业微信)        |  ✅ 支持  |          微信（全平台）          |         推荐 ⭐          |
|     [企业微信机器人](#1-企业微信)     |  ✅ 支持  |          微信（全平台）          |                         |
|            [Bark](#2-bark)            |  ✅ 支持  |         APP（仅限 iOS）          |         推荐 ⭐          |
|    [Telegram Bot](#3-telegram-bot)    |  ✅ 支持  |        Telegram（全平台）        |   推荐 ⭐，需科学上网    |
|        [Pushdeer](#4-pushdeer)        |  ✅ 支持  | 轻 APP(iOS)/APP(安卓)/APP(MacOS) | 推荐 iOS 和小米设备使用 |
|       [go-cqhttp](#5-go-cqhttp)       |  ✅ 支持  |                QQ                |  需自行部署 go-cqhttp   |
|    [钉钉群机器人](#6-钉钉群机器人)    |  ✅ 支持  |              钉钉群              |                         |
|       [Server 酱](#7-server-酱)       |  ✅ 支持  |        多渠道推送(微信等)        |    免费版每天限 5 条    |
|       [pushplus](#8-push-plus)        |  ✅ 支持  |     多渠道推送(微信/邮件等)      |                         |
| [Discord Webhook](#9-discord-webhook) |  ✅ 支持  |             Discord              |       需科学上网        |
|    [Cool Push](#10-coolpush-酷推)     |  ✅ 支持  |                QQ                |                         |
|        [Qmsg 酱](#11-qmsg-酱)         |  ✅ 支持  |                QQ                |                         |
|                 IGOT                  | 🛠️ 未测试 |                                  |                         |

### 1. 企业微信

i. 企业微信自建应用

通过自建应用推送到企业微信/微信，推荐使用。

<details>

> 本部分教程鸣谢 Server 酱。

1. 注册企业：用电脑打开[企业微信官网](https://work.weixin.qq.com/)，注册一个企业。

2. 创建应用：注册成功后，点「管理企业」进入管理界面，选择「应用管理」 → 「自建」 → 「创建应用」。

   ![img](https://s2.loli.net/2022/02/06/j5EZvRV6YtDKr7B.png)

3. 创建完成后进入应用详情页，可以得到应用 ID( `agentid` )，应用 Secret( `secret` )，复制并填到配置文件对应位置（获取应用 Secret 时，可能会将其推送到企业微信客户端，需要在企业微信客户端查看）。

![img](https://s2.loli.net/2022/02/06/1N3rnFVHBqQk2Wh.png)

4. 获取企业 ID：进入「[我的企业](https://work.weixin.qq.com/wework_admin/frame#profile)」页面，拉到最下边，可以看到企业 ID，复制并填到配置文件中。

5. 获取推送用户：在"通讯录" -> "成员管理" 中获取要收取信息的人员账号填入配置文件`WW_APP_USERID`，全员推送填`@all`。如果该应用只有一个人使用，填`@all`即可。

   ![image-20220206142035455](https://s2.loli.net/2022/02/06/XylJe4SAMFEjoYb.png)

6. 推送消息到微信：进入「我的企业」 → 「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到下边扫描二维码，关注以后即可收到推送的消息。

   ![img](https://s2.loli.net/2022/02/06/wOJ47LAVcX6Par8.png)

注：如果出现`接口请求正常，企业微信接受消息正常，个人微信无法收到消息`的情况：

   1. 进入「我的企业」 → 「[微信插件](https://work.weixin.qq.com/wework_admin/frame#profile/wxPlugin)」，拉到最下方，勾选 “允许成员在微信插件中接收和回复聊天消息” ![img](https://s2.loli.net/2022/02/06/sF8MS3ZBUCueN7I.jpg)
   2. 在企业微信客户端 「我」 → 「设置」 → 「新消息通知」中关闭 “仅在企业微信中接受消息” 限制条件 ![img](https://s2.loli.net/2022/02/06/OdyJslVKtekTIAX.jpg)

</details>

ii. 企业微信机器人

<details>

在终端某个群组添加机器人之后，创建者可以在机器人详情页看的该机器人特有的 webhookurl，将其中的`key=`后面的内容填写到配置文件`WW_BOT_KEY`中，例如`693a91f6-7xxx-4bc4-97a0-0ec2sifa5aaa`。

</details>

### 2. Bark

<details>

1. 从 AppStore 下载并打开 [Bark](https://github.com/Finb/Bark) App，将 App 内提供的 KEY 填入 `BARK_KEY` 即可。
2. 支持部分可选配置，如自定义消息分组 `BARK_GROUP`，自定义通知图标 `BARK_ICON`，自定义消息保存 `BARK_ARCHIVE`，时效性通知`BARK_LEVEL`。
     - BARK_GROUP: 指定推送消息分组，可在历史记录中按分组查看推送。
     - BARK_ICON：指定推送消息图标，仅 iOS15 或以上支持，如：`http://day.app/assets/images/avatar.jpg`。
     - BARK_ARCHIVE： 指定是否需要保存推送信息到历史记录，1 为保存，其他值为不保存。如果不指定这个参数，推送信息将按照APP内设置来决定是否保存。
     - BARK_LEVEL： 设置时效性通知。
         - `active`：不设置时的默认值，系统会立即亮屏显示通知。
         - `timeSensitive`：时效性通知，可在专注状态下显示通知。
         - `passive`：仅将通知添加到通知列表，不会亮屏提醒。
3. 自建服务器需修改`BARK_URL`。

</details>

### 3. Telegram Bot

<details>

1. 创建机器人：打开 [@BotFather](https://t.me/botfather)，输入 `/newbot` 生成新一个的 bot。根据提示，依次输入：Bot 名字、Bot 账号（需要以 bot 结尾），复制获取到的 Token，填入配置文件`TG_BOT_TOKEN`。
   ![image-20220206143711051](https://s2.loli.net/2022/02/06/MBX7EmTJZDtzq93.png)
2. 点击消息框中 `t.me/你的botid `这个链接，跳转到你的 bot，点击`START`以关联你的 bot。
3. 打开 [@userinfobot](https://t.me/userinfobot)，发送`/start`，获取你的 ID，填入配置文件`TG_USER_ID`。
4. 使用 Telegram bot 推送需要配置代理，或搭建反代服务器后填入配置文件`TG_BOT_API`。此处提供一个我基于 CF Workers 反代的 API `tgbotapi.xm.mk` 供使用。

</details>

### 4. Pushdeer

<details>

[PushDeer](https://github.com/easychen/pushdeer)是一个可以自行架设的无APP推送服务，iOS 端基于轻APP，无需安装APP；Android未来将基于快应用（正在开发），目前使用 APP（已接入MI PUSH，因此小米用户可在不开启 APP 的情况下获取通知）。

1. 苹果手机（iOS 14+）用系统相机扫描下方码即可拉起轻应用。亦可在苹果商店搜索「PushDeer」安装（不要安装 PushDeer 自架版）。Android 快应用尚在开发，可下载并安装 Android 测试版 APP([GitHub](https://github.com/easychen/pushdeer/releases/tag/android1.0alpha)|[Gitee](https://gitee.com/easychen/pushdeer/releases/android1.0alpha))。
   ![img](https://github.com/easychen/pushdeer/raw/main/doc/image/clipcode.png)
2. 通过 apple 账号（或微信账号·仅 Android 版支持）登录。
3. 切换到「设备」标签页，点击右上角的加号，注册当前设备。
4. 切换到「Key」标签页，点击右上角的加号，创建一个 Key，将 Key 填入配置文件`PUSHDEER_KEY`中。

</details>

### 5. GO-CQHTTP

<details>

1. 部署 [GO-CQHTTP](https://github.com/Mrs4s/go-cqhttp)，参见文档[快速开始](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B)，也可使用其他兼容 [OneBot-v11](https://github.com/botuniverse/onebot-11) 规范的框架或 SDK。
2. 将 CQHTTP 的服务器`协议头://IP或域名:端口号`填入 `CQHTTP_URL`，需包含协议头，如：`http://1.2.3.4:5700/`或`https://example.com/`。
3. 配置发送模式 `CQHTTP_MESSAGE_TYPE`，`private` 为私聊发送，`group` 为群聊发送。
4. 配置消息接收方的 QQ 号/群号，填入 `CQHTTP_SEND_ID`，与发送模式匹配。
5. 若配置了`Access Token`，需要填写 `CQHTTP_TOKEN`。

</details>

### 6. 钉钉群机器人

<details>

1. 创建钉钉群，并添加自定义机器人，参见 [钉钉开放平台·自定义机器人接入](https://developers.dingtalk.com/document/robots/custom-robot-access?spm=ding_open_doc.document.0.0.7f875e594zPr9w#topic-2026027)。
2. 将生成的 Webhook 地址中的 `access_token`填入 `DD_BOT_TOKEN`。
3. 将创建过程中`加签`的密钥填入`DD_BOT_SECRET`。
</details>

### 7. Server 酱

<details>

1. 前往[Server 酱](https://sct.ftqq.com/) 官网注册并绑定微信。
2. 将获取到的`send key`填入`config.json -> SCKEY`中即可。

注：Server 酱免费版每天有 5 次的调用次数上限。

</details>

### 8. Push Plus

<details>

1. 登录 [pushplus 网站](http://www.pushplus.plus/) ，复制 token 填入 `PUSH_PLUS_TOKEN`。
2. 若要一对多推送，需要创建群组并将群组编号填入 `PUSH_PLUS_USER`，一对一推送无需填写。

</details>

### 9. Discord Webhook

<details>

1. 进入 Server Settings（服务器设定） - Integrations（整合），点击 Create Webhook，点击 Copy Webhook URL，填写到配置文件 `DISCORD_WEBHOOK` 中。
2. 可根据需要设置机器人显示的名字`DISCORD_USERNAME`、机器人头像`DISCORD_AVATAR`（需要是 web 图片地址）和消息卡片颜色`DISCORD_COLOR`，详情可阅读 [Discord Webhooks Guide](https://birdie0.github.io/discord-webhooks-guide/structure/embeds.html)。

</details>

### 10. CoolPush 酷推

<details>

注：现在酷推公共服务不可用，可能需要私有化部署。

1. 登录 [CoolPush](https://cp.xuthus.cc/)，绑定 QQ 号/QQ 群及私有化部署地址，获取`调用代码Skey`。
2. 将 Skey 填入 `COOL_PUSH_SKEY` ，`COOL_PUSH_MODE` 支持 QQ 私聊推送/QQ 群消息推送/QQ 私有化私聊推送/QQ 私有化群聊推送，不支持一对多推送。
3. 如果需要动态的指定推送消息给特定的 QQ 号或者群，将 QQ 号/群号填入 `COOL_PUSH_SENDID` 即可。

</details>

### 11. Qmsg 酱

<details>

登录 [Qmsg 酱](https://qmsg.zendee.cn/)，获取 KEY 填入 `QMSG_KEY` 即可。

注：Qmsg 酱容易被判定违规=\_=，且无法进行群聊推送（审核不通过）。

</details>

## 更新日志

### v2.0.0（2022-02-09）

BREAKING CHANGE:

- 配置文件改用 yaml 格式

New Features:

- 支持多账号、多角色
- 支持云函数部署
- 支持 Discord 推送

Removed：

- 移除 QQ 主动查询模块

Others:

- 添加国内 docker 镜像
- 优化推送体验
- 重构部分模块

### v1.3.3（2022-02-06）

New Features:

- 新增 Pushdeer 推送通道
- 移除旧版 Serverchan 推送通道
- 优化推送内容

Bug Fixes:

- 调整 cqhttp 参数，将`CQHTTP_IP`和`CQHTTP_PORT`合并为`CQHTTP_URL`
- 调整部分通道渲染样式

### v1.3.2（2022-01-12）

Bug Fixes

### v1.3.1（2022-01-10）

New Features:

- 支持自定义 BARK 推送服务器

Bug Fixes:

- 修复 BARK 推送状态检测错误的问题

### v1.3.0（2022-01-10）

新年新气象~

New Features:

- 加入洞天宝钱信息，支持设置洞天宝钱溢出提醒，配置文件新增`RECEIVE_HOMECOIN_ALERT`字段
- 增加睡前检查，若树脂在休眠期间溢出将在睡眠前发送提醒
- 加入 API 切换选项，支持云服务器运行时指定使用旧版 API
- 优化消息排版

Bug Fixes:

- 修复树脂溢出提示无效的问题
- 更新探索派遣新角色信息
- 修复诺艾尔角色信息错误
- 优化休眠逻辑

### v1.2.5（2021-12-24）

Bug Fixes：

- 同步米游社 API 变动，更换新的 API。

### v1.2.4（2021-11-24）

Bug Fixes：

- 修复 cookie 出错时的异常退出问题

### v1.2.3（2021-11-23）

New Features:

- CQHTTP 推送 IP 字段支持协议头，以支持 HTTPS

### v1.2.2（2021-11-10）

New Features:

- 优化每日委托提醒时间判断逻辑
- 增加每日委托奖励领取情况判断，去他人世界做委托领取奖励后不再会被误认为未完成委托。

### v1.2.1（2021-11-01）

Bug Fixes：

- 修复 CQ-HTTP 推送鉴权错误，请使用 CQ-HTTP 的用户注意**配置文件字段变动**。

New Features:

- 增加群推送模式支持
- 增加自定义端口支持

### v1.2.0 (2021-11-01)

New Features:

- 支持夜间休眠，再也不会深夜不停扰民了
- 日志增加每轮检查树脂值显示

Bug Fixes：
- 修复 cqhttp 推送错误提示
- 配置文件部分字段改为可选配置

### v1.1.2（2021-10-29）

New Features:

- 增加 cqhttp 推送

Others:
- 更新文档

### v1.1.1 (2021-10-28)

New Features:

- 增加探索派遣完成提醒
- 优化提醒标题

### v1.1.0 (2021-10-28)

New Features:
- 优化提醒逻辑
- 增加账号信息显示

Bug Fixes:
- 修复休眠时间不正确的问题

## 致谢

|                                                  Project                                                  |   Author    |                                                License                                                |     Comment      |
| :-------------------------------------------------------------------------------------------------------: | :---------: | :---------------------------------------------------------------------------------------------------: | :--------------: |
| [genshin_task-resin-expedition_alert](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert) | yaomeng0722 | [MIT LICENSE](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert/blob/master/LICENSE) | 本项目的初始版本 |
|                               [onepush](https://github.com/y1ndan/onepush)                                |    y1ndan    |                  [MIT LICENSE](https://github.com/y1ndan/onepush/blob/main/LICENSE)                   |   消息推送通道   |
|                [genshin-checkin-helper](https://gitlab.com/y1ndan/genshin-checkin-helper)                 |    y1ndan    |         [GPLv3 LICENSE](https://gitlab.com/y1ndan/genshin-checkin-helper/-/blob/main/LICENSE)         |   API 调用方法   |



## License

[GNU GPLv3](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/master/LICENSE)
