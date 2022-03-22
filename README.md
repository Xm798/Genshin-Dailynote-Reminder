English | [简体中文](./docs/README_ZH.md)

# Genshin Dailynote Helper


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
  - [Examples](#examples)
  - [How to use](#how-to-use)
  - [Configuration file parameters description](#configuration-file-parameters-description)
    - [Some basic information](#some-basic-information)
    - [Configuration file example](#configuration-file-example)
  - [Push method configuration](#push-method-configuration)
  - [💬Feedback](#feedback)
  - [Changelog](#changelog)
  - [Acknowledgements](#acknowledgements)
    - [Open Source Projects](#open-source-projects)
    - [Translators](#translators)
  - [License](#license)

## Examples

**Push Example**

<img src="https://s2.loli.net/2022/02/10/fop8SNLW1bqejEQ.png" width="300px" />


**Display of each push channel**

<details>


**Notification Center**

<img src="https://s2.loli.net/2022/02/10/TJH8Kly4n7pwazg.png" width="300px" />

<img src="https://s2.loli.net/2022/02/10/orsvg2lk794aIKZ.png" width="300px" />

**WeChat**

<img src="https://s2.loli.net/2022/02/10/D1n58XafpIWUYZ9.png" width="300px" />

**Bark**

<img src="https://s2.loli.net/2022/02/10/WCyNp9mEUziFt2d.png" width="300px" />

**Server Chan**

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

   ![](https://s2.loli.net/2022/02/09/BVQ1sZnSfRj2UhF.png)

4. In the function code section, select "Upload zip package locally", select the downloaded package and upload it.

   ![](https://s2.loli.net/2022/02/09/HM275iAPhzxRyBn.png)

5. Expand "Advanced Configuration", **change the execution timeout to 90 seconds or longer**, **add environment variable**key to `TZ`and value to `Asia/Shanghai`. If you are in another time zone, please change it to the corresponding time zone, you can check the time zone list at [这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518)(**very important**, otherwise the time will be incorrect).

   ![](https://s2.loli.net/2022/02/12/Lw2Hn48jKSGBPJF.png)

6. Expand Trigger Configuration, select Custom Trigger Period and fill in the cron expression. For example, to check every 15 minutes, fill in `0 * /15 * * * * *`, to check every 30 minutes, fill in `0 * /30 * * * * *`, and to trigger every hour exactly, fill in `0 0 * * * * *`. Please note that this interval is consistent with `CHECK_INTERVAL` in the configuration file to run the bedtime check function.

   ![](https://s2.loli.net/2022/02/14/KQGvlWOq5EiARY8.png)

7. Jump to the **Function Management - Function Code** page, find `dailynotehelper/config/config.example.yaml` in the directory, right-click and rename it to `config.yaml`, **and fill in your configuration**(environment variables are not supported).

    ![](https://s2.loli.net/2022/02/09/vxkaqoOfVw6hBgW.png)

8. Click **Deploy and Test** below to see if the log test is working properly.

</details>

### 2. Docker

i. **Using Docker Image**

  1. Click [here](https://raw.githubusercontent.com/Xm798/Genshin-Dailynote-Helper/master/dailynotehelper/config/config.example.yaml) or get the sample configuration file from this project path `dailynotehelper/config/config.example.yaml` and fill it out, renaming it to `config.yaml`.

  2. Run, `/PATH-to-YOUR-CONFIG/config.yaml` is the path to your local configuration file, you need to fill it according to the actual situation. The environment variable `TZ` is the time zone of your location (**very important**, otherwise the time will be incorrect), you can check the list of time zones at [here](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518).


     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --env TZ=Asia/Shanghai \
     --restart=always \
     --name=genshin-dailynote-helper \
     xm798/genshin-dailynote-helper:latest
     ```
     If you are running on a chinese mainland machine, you can use the image on Tencent Cloud.

     ```shell
     docker run -d \
     -v /PATH-to-YOUR-CONFIG/config.yaml:/app/dailynotehelper/config/config.yaml \
     --env TZ=Asia/Shanghai \
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

1. Install [python3](https://www.python.org) environment, version >= 3.6.

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
      1. Open [Mihoyo bbs](https://bbs.mihoyo.com/ys) for cn server and [Hoyolab](https://www.hoyolab.com/) for oversea server, then login.
      2. Press F12 to open Developer Tools.
      3. Switching the developer tools to the Console tab.
      4. Copy the code below and paste it in the console, press enter and the result is pasted into the configuration file.

    ```javascript
    javascript:(()=>{_=(n)=>{for(i in(r=document.cookie.split(';'))){var a=r[i].split('=');if(a[0].trim()==n)return a[1]}};c=_('account_id')||alert('Invalid Cookie,please relogin!');c&&confirm('Copy cookies to clipboard?')&&copy(document.cookie)})();
    ```

3. **EXCLUDE_UID**
   
   If you have multiple characters bound to your MiYosha/Hoyolab account, but don't want to receive alerts for some of them, you can write their UIDs here, one per line.

### Example configuration file 

[config.example.yaml](./dailynotehelper/config/config.example.yaml)

## Push method configuration

**Details of the supported push channels currently are listed below**, recommended:

- **System notification push**: Bark or Pushdeer for iOS users, Pushdeer for MIUI users.
- **Full Platform Push**: Use Telegram or Discord.
- **WeChat Push**: Using WeChat Work or Pushplus.
- **QQ Push**: Use go-cqhttp.

|                                  Push Channels                                   | Support Situation |              Push Channel              |                  Remark                  |
| :------------------------------------------------------------------------------: | :---------------: | :------------------------------------: | :--------------------------------------: |
|         [WeChat Work](./docs/Push-method-configuration.md#1-wechat-work)         |    ✅ Supported    |         WeChat (All Platforms)         |               Recommend ⭐                |
|    [WeChat Work group bot](./docs/Push-method-configuration.md#1-wechat-work)    |    ✅ Supported    |         WeChat (All Platforms)         |                                          |
|                [Bark](./docs/Push-method-configuration.md#2-bark)                |    ✅ Supported    |           APP (only for iOS)           |               Recommend ⭐                |
|        [Telegram Bot](./docs/Push-method-configuration.md#3-telegram-bot)        |    ✅ Supported    |        Telegram (All platforms)        |               Recommend ⭐                |
|            [Pushdeer](./docs/Push-method-configuration.md#4-pushdeer)            |    ✅ Supported    | Light APP(iOS)/APP(Android)/APP(MacOS) |  Recommended for iOS and Xiaomi devices  |
|           [go-cqhttp](./docs/Push-method-configuration.md#5-go-cqhttp)           |    ✅ Supported    |                   QQ                   |        Need to deploy by yourself        |
| [DingTalk group bot](./docs/Push-method-configuration.md#6-dingtalk-group-robot) |    ✅ Supported    |             DingTalk group             |                                          |
|         [Server Chan](./docs/Push-method-configuration.md#7-server-chan)         |    ✅ Supported    |       Multi-channel aggregation        | The free version is limited to 5 per day |
|           [pushplus](./docs/Push-method-configuration.md#8-push-plus)            |    ✅ Supported    |       Multi-channel aggregation        |                                          |
|     [Discord Webhook](./docs/Push-method-configuration.md#9-discord-webhook)     |    ✅ Supported    |                Discord                 |                                          |
|              [Email](./docs/Push-method-configuration.md#10-email)               |    ✅ Supported    |                                        |                                          |
|           [Cool Push](./docs/Push-method-configuration.md#11-coolpush)           |    ✅ Supported    |                   QQ                   |                                          |
|               [Qmsg](./docs/Push-method-configuration.md#12-qmsg)                |    ✅ Supported    |                   QQ                   |                                          |
|    [Custom Notifier](./docs/Push-method-configuration.md#13-custom-notifier)     |    ✅ Supported    |                                        |                                          |
|                                       IGOT                                       |   🛠️ Not tested    |                                        |                                          |


## 💬Feedback

[![](https://img.shields.io/badge/%20-QQ%20Group-blue?style=for-the-badge&logo=Tencent%20QQ&logoColor=EB1923&labelColor=eeeeee&color=EB1923)](https://jq.qq.com/?_wv=1027&k=CnNxc9hp)
[![](https://img.shields.io/badge/%20-Telegram%20Group-blue?style=for-the-badge&logo=Telegram&logoColor=26A5E4&labelColor=eeeeee&color=26A5E4)](https://t.me/+QtSxha7rXsc2ZTg1)



## Changelog

See [Changelog.md](./docs/CHANGELOG.md)


## Acknowledgements

### Open Source Projects and Contributors

|                                                   Project                                                   |                     Author                     |                                            License                                            |             Comment             |
| :---------------------------------------------------------------------------------------------------------: | :--------------------------------------------: | :-------------------------------------------------------------------------------------------: | :-----------------------------: |
| [ genshin_task-resin-expedition_alert ](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert) | [yaomeng0722](https://gitlab.com/yaomeng0722/) | [MIT](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert/blob/master/LICENSE) | Initial version of this project |
|                                [onepush](https://github.com/y1ndan/onepush)                                 |      [y1ndan](https://gitlab.com/y1ndan/)      |                  [MIT](https://github.com/y1ndan/onepush/blob/main/LICENSE)                   |      message push channel       |
|                [ genshin-checkin-helper ](https://gitlab.com/y1ndan/genshin-checkin-helper)                 |      [y1ndan](https://gitlab.com/y1ndan/)      |         [GPLv3](https://gitlab.com/y1ndan/genshin-checkin-helper/-/blob/main/LICENSE)         |         API call method         |
|                                                      -                                                      |      [yllhwa](https://github.com/yllhwa)       |                                               -                                               | DS encryption algorithm reverse |

### Translators

| Language |      Name       |             Translators             |
| :------: | :-------------: | :---------------------------------: |
|  zh_TW   | 繁體中文 (台灣) | [KT-Yeh](https://github.com/KT-Yeh) |


## License

[GNU GPLv3](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/master/LICENSE)


> Translated by DeepL and Google from Simplified Chinese.
