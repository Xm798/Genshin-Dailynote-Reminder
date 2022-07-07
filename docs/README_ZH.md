# 原神实时便笺提醒小助手 | Genshin Dailynote Helper

<div align="center">

[![](https://img.shields.io/badge/Author-Xm798-blueviolet?style=flat-square)](https://github.com/Xm798/)
[![](https://img.shields.io/badge/Github-blue?style=flat-square&logo=Github&logoColor=181717&labelColor=eeeeee&color=181717)](https://github.com/Xm798/Genshin-Dailynote-Helper)
[![](https://img.shields.io/badge/Gitee-blue?style=flat-square&logo=Gitee&logoColor=C71D23&labelColor=eeeeee&color=C71D23)](https://gitee.com/Xm798/Genshin-Dailynote-Helper)
[![](https://img.shields.io/badge/Python-3.6%2B-blue?style=flat-square&color=3776AB)](https://github.com/Xm798/)
[![](https://img.shields.io/github/license/Xm798/Genshin-Dailynote-Helper?style=flat-square)](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/master/LICENSE)
[![](https://img.shields.io/github/contributors/Xm798/Genshin-Dailynote-Helper?style=flat-square)](https://github.com/Xm798/Genshin-Dailynote-Helper/graphs/contributors)
[![](https://img.shields.io/docker/pulls/xm798/genshin-dailynote-helper?style=flat-square)](https://hub.docker.com/r/xm798/genshin-dailynote-helper)
[![](https://img.shields.io/github/v/release/xm798/Genshin-Dailynote-Helper?color=success&style=flat-square)](https://github.com/Xm798/Genshin-Dailynote-Helper/releases)

</div>

## 简介

检查并推送原神内树脂、委托、周本、探索派遣和洞天宝钱情况。

特性：

- 支持云函数、Docker 和本地运行
- 支持多账号、多角色
- 支持推送到多个渠道
- 支持国服（官服以及渠道服）和国际服
- 支持跳过某些角色（同一米游社/ Hoyolab 账号下绑定了多个角色时）

支持当如下情况时发送提醒：

- 树脂即将溢出
- 今日委托未完成
- 洞天宝钱溢出
- 探索派遣已完成
- 免打扰时间段内树脂会溢出
- 参量质变仪已就绪

## 目录

- [示例](#示例)
- [使用方法](#使用方法)
  - [1. 云函数运行](#1-云函数运行)
    - [阿里云函数计算 FC](#阿里云函数计算-fc)
    - [腾讯云云函数 SCF](#腾讯云云函数-scf)
  - [2. Docker 运行](#2-docker-运行)
  - [3. 本地运行](#3-本地运行)
- [配置文件参数说明](#配置文件参数说明)
  - [一些基础信息](#一些基础信息)
  - [示例配置文件](#示例配置文件)
  - [通过环境变量进行配置](#通过环境变量进行配置)
- [推送方式配置](#推送方式配置)
- [💬交流反馈](#交流反馈)
- [更新日志](#更新日志)
- [致谢](#致谢)
  - [开源项目及贡献者](#开源项目及贡献者)
  - [本地化译者](#本地化译者)
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

#### 阿里云函数计算 FC

<details>

1. 登录阿里云函数计算控制台，在最上方选择好地域（**如果是推送 Telegram 或 Discord，或者检测国际服账号，务必选择中国大陆以外的地区**）。进入“服务及函数” - “创建服务”，输入名称，点击确定。

   ![img](https://s2.loli.net/2022/02/16/pVxDnS1NZrlIAsB.png)

2. 进入创建好的服务，点击**创建函数**，**从零开始创建**。输入**函数名称**，运行环境选择 **Python 3**，触发方式为**通过事件触发**，内存规格选择 **128MB**。

   ![image-20220216224031752](https://s2.loli.net/2022/02/16/ICsPuWiD2d6GQ4U.png)

3. 创建完成后，进入**函数代码**页面，选择“上传代码” - 上传 zip 包，选择下载的 serverless 包并上传。

   ![image-20220216224242175](https://s2.loli.net/2022/02/16/PMyYGEqgZ1cx9dF.png)

4. 参数设置，配置文件和环境变量二选一
   1. **通过配置文件进行设置**：在函数代码的编辑器中找到 `dailynotehelper/config/` 文件夹，将`config.example.yaml`右键重命名为`config.yaml`，并填入你自己的配置。保存后，点击 **“部署代码”**，再点击 **“测试函数”**。测试时，**可以将树脂提醒阈值改为 1 以便触发推送**，测试完成后再改回去。此时，应当能够看到上方有“执行成功”的提示和运行日志。

      ![image-20220216224710614](https://s2.loli.net/2022/02/16/Iwek8gxYybHdLcT.png)

   2. **通过环境变量进行配置**：切换到“**函数配置**”选项卡，下拉找到“**环境变量**”，点击**编辑**，参照[通过环境变量进行配置](#通过环境变量进行配置)的说明依次添加需要的环境变量，不设置的项目即为默认值。至少需要设置`COOKIE`或`COOKIE_HOYOLAB`以及对应的推送通道。需要注意阿里云函数计算不支持将中文设置为环境变量的值，因此如果需要自定义称呼`NICK_NAME`，需要进行 [URL-encode 编码](https://www.urlencoder.org/) 后再填入其中。

      ![image.png](https://s2.loli.net/2022/05/19/DojfQPLSy9AuWc7.png)

5. 切换到“**函数配置**”选项卡，下拉找到“**环境变量**”，点击**编辑**，新建环境变量，key 为 `TZ`，value 为 `Asia/Shanghai`。如果你在其他时区，请修改为对应的时区，请在[这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518)查询时区列表（**十分重要**，否则时间会不正确）。最后点击保存。

   ![image-20220216225056405](https://s2.loli.net/2022/02/16/dBhXO34xH18YUrD.png)

6. 切换到 **“触发器管理”** 选项卡，**创建触发器**，选择**定时触发器**，输入**名称**，选择**按照时间间隔触发**，输入你想要的时间间隔，如 30 分钟。注意，配置文件中的 `CHECK_INTERVAL` 应当与此处一致。

   ![image-20220216224947289](https://s2.loli.net/2022/02/16/bUgnSdypPJZQT73.png)

7. 阿里云函数计算的配置方法到此结束。

</details>

#### 腾讯云云函数 SCF

自 2022 年 5 月 23 日起，腾讯云不再提供免费额度。建议使用阿里云函数计算服务，或购买 1 元资源包。见 [关于云函数运行的免费额度问题](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/5) 。

<details>

1. 从 [Release 页面](https://github.com/Xm798/Genshin-Dailynote-Helper/releases) 下载最新代码包，国内可从 [Gitee 镜像](https://gitee.com/Xm798/Genshin-Dailynote-Helper/releases) 下载。

2. 打开[腾讯云云函数控制台](https://console.cloud.tencent.com/scf)，登录账号，点击“函数服务” - “新建”。

3. 选择“从头开始”，输入一个函数名。地域在国内随便选择，如需检测国际服或者推送 Telegram 或 Discord，必须选择大陆以外如中国香港地区。运行环境为 Python3.7。

   ![img](https://s2.loli.net/2022/02/09/BVQ1sZnSfRj2UhF.png)

4. 函数代码部分，选择“本地上传 zip 包”，选择下载的程序包并上传。

   ![img](https://s2.loli.net/2022/02/09/HM275iAPhzxRyBn.png)

5. 展开“高级配置”，**修改执行超时时间为 60 秒或更长**，**添加环境变量** key 为 `TZ`，value 为 `Asia/Shanghai`。如果你在其他时区，请修改为对应的时区，可以在 [这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518) 查询时区列表（**十分重要**，否则时间会不正确）。

   ![img](https://s2.loli.net/2022/02/12/Lw2Hn48jKSGBPJF.png)

6. 展开触发器配置，选择自定义触发周期，填写 cron 表达式。例如：每 15 分钟检查一次，填写`0 */15 * * * * *`，每 30 分钟检查一次，填写`0 */30 * * * * *`，每小时整点触发，填写`0 0 * * * * *`。该间隔请注意与配置文件中`CHECK_INTERVAL`一致，以便运行睡前检查功能。

   ![img](https://s2.loli.net/2022/02/14/KQGvlWOq5EiARY8.png)

7. 跳转到 **函数管理 - 函数代码**页面，在目录中找到`dailynotehelper/config/config.example.yaml`，右键重命名为`config.yaml`，**并填写你的配置**（不支持环境变量）。

    ![img](https://s2.loli.net/2022/02/09/vxkaqoOfVw6hBgW.png)

8. 点击下方“**部署并测试**”，查看日志测试是否运行正常。

</details>

### 2. Docker 运行

i. **使用镜像**

  1. 点击 [链接](https://raw.githubusercontent.com/Xm798/Genshin-Dailynote-Helper/master/dailynotehelper/config/config.example.yaml) 或从本项目路径`dailynotehelper/config/config.example.yaml`提取示例配置文件并填写，重命名为`config.yaml`。

  2. 运行，`/PATH-to-YOUR-CONFIG/config.yaml`是你本地配置文件的路径，需要根据实际情况填写。环境变量 TZ 为你所在地的时区（**十分重要**，否则时间会不正确），可以在[这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518)查询时区列表。

     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --env TZ=Asia/Shanghai \
     --restart=always \
     --name=genshin-dailynote-helper \
     xm798/genshin-dailynote-helper:latest
     ```

     若在国内机器运行，可使用在阿里云的镜像。

     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --env TZ=Asia/Shanghai \
     --restart=always \
     --name=genshin-dailynote-helper \
     registry.cn-shanghai.aliyuncs.com/xm798/genshin-dailynote-helper:latest
     ```

ii. **使用 docker-compose**

  克隆项目，填写配置文件后构建运行。环境变量 TZ 为你所在地的时区，可以在[这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518)查询时区列表。

  ```sh
  git clone https://github.com/Xm798/Genshin-Dailynote-Helper.git
  cd Genshin-Dailynote-Helper
  cp ./dailynotehelper/config/config.example.yaml ./dailynotehelper/config/config.yaml
  docker-compose up -d
  ```

### 3. 本地运行

1. 安装 [python3](https://www.python.org) 环境，版本>=3.6。

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

1. ~~RUN_ENV~~：

    ~~指定运行环境，国内云服务商运行使用`cloud`，否则使用`local`，仅对国服生效。该选项旨在为在国内云服务器运行的用户提供兼容性选项，`cloud`为旧版 API，曾经无法使用，现在又恢复了。但由于米游社已全面更换为新的 API，因此默认使用`local`环境即新 API 运行。详情参考：[米游社可能已经禁止国内特定 VPS 服务商的 IP 或 ASN](https://github.com/Arondight/Adachi-BOT/issues/522)。~~

    ~~**2022/3/14 更新**：由于新接口极不稳定，本地请求也会概率触发阿里云应用防火墙的盾，因此请使用 `cloud` 环境，等老接口不能用了再说。~~

    **2022/5/18 更新**：米哈游仿佛已经关闭了旧接口，因此此项配置已被移除，默认使用新接口（即`local`环境）。

2. **COOKIE**:
      1. 国服打开[米游社社区](https://bbs.mihoyo.com/ys)并登录，国际服打开[Hoyolab](https://www.hoyolab.com/)并登录
      2. 按 F12 打开开发者工具；
      3. 将开发者工具切换至控制台 (Console) 页签；
      4. 复制下方的代码，并将其粘贴在控制台中，按下回车，结果粘贴到配置文件中。

    ```javascript
    javascript:(()=>{_=(n)=>{for(i in(r=document.cookie.split(';'))){var a=r[i].split('=');if(a[0].trim()==n)return a[1]}};c=_('account_id')||alert('无效的 Cookie，请重新登录！');c&&confirm('将 Cookie 复制到剪贴板？')&&copy(document.cookie)})();
    ```

3. EXCLUDE_UID

   如果你的米游社/ Hoyolab 账号绑定了多个角色，但不想接收其中某些角色的提醒，可以将它们的 UID 写在这里，每行一个。

### 示例配置文件

[config.example.yaml](../dailynotehelper/config/config.example.yaml)

### 通过环境变量进行配置

支持通过环境变量进行参数配置，方便云函数使用。

所有配置项的键名见下，其含义与配置文件相同，请参照配置文件进行设置。所有的值都应为字符串形式的标准 Python 类型。

其中：

- `COOKIE`、`COOKIE_HOYOLAB`、`EXCLUDE_UID`的值应形如：`['COOKIE1', 'COOKIE2']`、`[UID1, UID2]`。例如：COOKIE：`['ltuid=xxxxx; cookie_token=xxxxxx']`，EXCLUDE_UID：`[100234567]`。
- 所有需要填 true 或 false 的变量的值应为`True`或`False`；
- `NICK_NAME` 如果有中文字符且云函数平台不支持环境变量设置中文（如阿里云），则需要经过 [URL-encode 编码](https://www.urlencoder.org/) 。
- `CUSTOM_NOTIFIER`的值应形如：`{'method': 'POST','url': '','data_type': 'data','headers': {},'data': {},'title_key': null,'desp_key': '','markdown': False,'retcode_key': '','retcode_value': ''}`。

```text
LANGUAGE
COOKIE
COOKIE_HOYOLAB
EXCLUDE_UID
DISPLAY_UID
NICK_NAME
RESIN_INFO
COMMISSION_INFO
EXPEDITION_INFO
TROUNCE_INFO
HOMECOIN_INFO
TRANSFORMER_INFO
RESIN_THRESHOLD
COMMISSION_NOTICE_TIME
EXPEDITION_NOTICE
WAIT_ALL_EXPEDITION
HOMECOIN_NOTICE
HOMECOIN_THRESHOLD
TRANSFORMER
CHECK_INTERVAL
SLEEP_TIME
WW_ID
WW_APP_AGENTID
WW_APP_SECRET
WW_APP_USERID
WW_BOT_KEY
BARK_URL
BARK_GROUP
BARK_ICON
BARK_ARCHIVE
BARK_LEVEL
TG_BOT_API
TG_BOT_TOKEN
TG_USER_ID
PUSHDEER_KEY
CQHTTP_URL
CQHTTP_MESSAGE_TYPE
CQHTTP_SEND_ID
CQHTTP_SEND_CHANNEL_ID
CQHTTP_TOKEN
DD_BOT_TOKEN
DD_BOT_SECRET
SCTKEY
PUSH_PLUS_TOKEN
PUSH_PLUS_USER
COOL_PUSH_SKEY
COOL_PUSH_MODE
COOL_PUSH_SENDID
QMSG_KEY
DISCORD_WEBHOOK
DISCORD_USERNAME
DISCORD_AVATAR
DISCORD_COLOR
IGOT_KEY
MAIL_HOST
MAIL_PORT
MAIL_STARTTLS
MAIL_USERNAME
MAIL_PASSWORD
MAIL_TO
CUSTOM_NOTIFIER
```

## 推送方式配置

**目前支持的推送渠道详情如下表**，建议：

- **微信推送**：使用企业微信或 pushplus；
- **系统通知推送**：iOS 用户使用 Bark 或 Pushdeer，MIUI 用户使用 Pushdeer；
- **全平台推送**：使用 Telegram 或企业微信；
- **QQ 推送**：自行部署 go-cqhttp 并使用。

|                                  推送渠道                                   | 支持情况 |             推送通道             |          备注           |
| :-------------------------------------------------------------------------: | :------: | :------------------------------: | :---------------------: |
|        [企业微信](./Push-method-configuration_ZH.md#1-企业微信)        |  ✅ 支持  |          微信（全平台）        |         推荐 ⭐          |
| [企业微信机器人](./Push-method-configuration_ZH.md#ii-企业微信机器人)  |  ✅ 支持  |          微信（全平台）        |                         |
|            [Bark](./Push-method-configuration_ZH.md#2-bark)            |  ✅ 支持  |         APP（仅限 iOS）        |         推荐 ⭐          |
|    [Telegram Bot](./Push-method-configuration_ZH.md#3-telegram-bot)    |  ✅ 支持  |        Telegram（全平台）      |   推荐 ⭐，需科学上网    |
|        [Pushdeer](./Push-method-configuration_ZH.md#4-pushdeer)        |  ✅ 支持  | 轻 APP(iOS)/APP(安卓)/APP(MacOS) | 推荐 iOS 和小米设备使用 |
|       [go-cqhttp](./Push-method-configuration_ZH.md#5-go-cqhttp)       |  ✅ 支持  |                QQ                |  需自行部署 go-cqhttp   |
|    [钉钉群机器人](./Push-method-configuration_ZH.md#6-钉钉群机器人)    |  ✅ 支持  |              钉钉群              |                         |
|       [Server 酱](./Push-method-configuration_ZH.md#7-server-酱)       |  ✅ 支持  |        多渠道推送 (微信等)        |    免费版每天限 5 条    |
|       [pushplus](./Push-method-configuration_ZH.md#8-push-plus)        |  ✅ 支持  |     多渠道推送 (微信/邮件等)      |                         |
| [Discord Webhook](./Push-method-configuration_ZH.md#9-discord-webhook) |  ✅ 支持  |             Discord              |       需科学上网        |
|       [邮件推送](./Push-method-configuration_ZH.md#10-邮件推送)        |  ✅ 支持  |                                  |                         |
|    [Cool Push](./Push-method-configuration_ZH.md#11-coolpush-酷推)     |  ✅ 支持  |                QQ                |                         |
|        [Qmsg 酱](./Push-method-configuration_ZH.md#12-qmsg-酱)         |  ✅ 支持  |                QQ                |                         |
|     [自定义推送](./Push-method-configuration_ZH.md#13-自定义推送)      |  ✅ 支持  |                                  |                         |
|                                    IGOT                                     | 🛠️ 未测试 |                                  |                         |

**各渠道详细设置方法参见：[推送渠道配置文档](./Push-method-configuration_ZH.md)**

## 💬交流反馈

[![QQ](https://img.shields.io/badge/%20-QQ%20Group-blue?style=for-the-badge&logo=Tencent%20QQ&logoColor=EB1923&labelColor=eeeeee&color=EB1923)](https://jq.qq.com/?_wv=1027&k=CnNxc9hp)
[![Telegram](https://img.shields.io/badge/%20-Telegram%20Group-blue?style=for-the-badge&logo=Telegram&logoColor=26A5E4&labelColor=eeeeee&color=26A5E4)](https://t.me/+QtSxha7rXsc2ZTg1)

## 更新日志

参见：[CHANGELOG_ZH.md](./CHANGELOG_ZH.md)

## 致谢

### 开源项目及贡献者

|                                                  Project                                                  |                     Author                     |                                            License                                            |     Comment      |
| :-------------------------------------------------------------------------------------------------------: | :--------------------------------------------: | :-------------------------------------------------------------------------------------------: | :--------------: |
| [genshin_task-resin-expedition_alert](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert) | [yaomeng0722](https://gitlab.com/yaomeng0722/) | [MIT](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert/blob/master/LICENSE) | 本项目的初始版本 |
|                               [onepush](https://github.com/y1ndan/onepush)                                |      [y1ndan](https://gitlab.com/y1ndan/)      |                  [MIT](https://github.com/y1ndan/onepush/blob/main/LICENSE)                   |   消息推送通道   |
|                [genshin-checkin-helper](https://gitlab.com/y1ndan/genshin-checkin-helper)                 |      [y1ndan](https://gitlab.com/y1ndan/)      |         [GPLv3](https://gitlab.com/y1ndan/genshin-checkin-helper/-/blob/main/LICENSE)         |   API 调用方法   |
|                                                     -                                                     |      [yllhwa](https://github.com/yllhwa)       |                                               -                                               | DS 加密算法逆向  |

### 本地化译者

| Language |      Name       |             Translators             |
| :------: | :-------------: | :---------------------------------: |
|  zh_TW   | 繁體中文 (台灣) | [KT-Yeh](https://github.com/KT-Yeh) |

## License

[GNU GPLv3](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/master/LICENSE)
