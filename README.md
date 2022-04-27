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
- Home coin is about to overflow
- Expeditions completed
- Resin will overflow during the no-disturb time period
- Parametric transformer is ready

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

#### 阿里云函数计算 FC

<details>

1. 登录阿里云函数计算控制台，在最上方选择好地域（**如果是推送 Telegram 或 Discord，或者检测国际服账号，务必选择中国大陆以外的地区**）。进入“服务及函数” - “创建服务”，输入名称，点击确定。

   ![img](https://s2.loli.net/2022/02/16/pVxDnS1NZrlIAsB.png)

2. 进入创建好的服务，点击**创建函数**，**从零开始创建**。输入**函数名称**，运行环境选择 **Python 3**，触发方式为**通过事件触发**，内存规格选择 **128MB**。

   ![image-20220216224031752](https://s2.loli.net/2022/02/16/ICsPuWiD2d6GQ4U.png)

3. 创建完成后，进入**函数代码**页面，选择“上传代码” - 上传 zip 包，选择下载的 serverless 包并上传。

   ![image-20220216224242175](https://s2.loli.net/2022/02/16/PMyYGEqgZ1cx9dF.png)

4. 上传后，在编辑器中找到 `dailynotehelper/config/` 文件夹，重命名配置 `config.example.yaml`为`config.yaml`，并填入你自己的配置。保存后，点击**“部署代码”**，再点击**“测试函数”**。测试时，可以将树脂提醒阈值改为 1 触发推送，测试完成后再改回去。此时，应当能够看到上方有“执行成功”的提示和运行日志。

   ![image-20220216224710614](https://s2.loli.net/2022/02/16/Iwek8gxYybHdLcT.png)

5. 切换到**“触发器管理”**选项卡，**创建触发器**，选择**定时触发器**，输入**名称**，选择**按照时间间隔触发**，输入你想要的时间间隔，如 30 分钟。注意，配置文件中的 `CHECK_INTERVAL` 应当与此处一致。

   ![image-20220216224947289](https://s2.loli.net/2022/02/16/bUgnSdypPJZQT73.png)

6. 切换到“**函数配置**”选项卡，下拉找到“**环境变量**”，点击**编辑**，新建环境变量，key 为 `TZ`，value 为 `Asia/Shanghai`。如果你在其他时区，请修改为对应的时区，请在[这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518)查询时区列表（**十分重要**，否则时间会不正确）。最后点击保存。

   ![image-20220216225056405](https://s2.loli.net/2022/02/16/dBhXO34xH18YUrD.png)

7. 阿里云函数计算的配置方法到此结束。

</details>

#### 腾讯云云函数 SCF

<details>

**自 2022 年 5 月 23 日起，腾讯云不再提供免费额度。建议使用阿里云函数计算服务，或购买 1 元资源包。见 [关于云函数运行的免费额度问题](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/5) 。**


1. 从 [Release 页面](https://github.com/Xm798/Genshin-Dailynote-Helper/releases) 下载最新代码包，国内可从 [Gitee 镜像](https://gitee.com/Xm798/Genshin-Dailynote-Helper/releases) 下载。

2. 打开[腾讯云云函数控制台](https://console.cloud.tencent.com/scf)，登录账号，点击“函数服务” - “新建”。

3. 选择“从头开始”，输入一个函数名。地域在国内随便选择，如需检测国际服或者推送 Telegram 或 Discord，必须选择大陆以外如中国香港地区。运行环境为 Python3.7。

   ![img](https://s2.loli.net/2022/02/09/BVQ1sZnSfRj2UhF.png)

4. 函数代码部分，选择“本地上传 zip 包”，选择下载的程序包并上传。

   ![img](https://s2.loli.net/2022/02/09/HM275iAPhzxRyBn.png)

5. 展开“高级配置”，**修改执行超时时间为 90 秒或更长**，**添加环境变量** key 为 `TZ`，value 为 `Asia/Shanghai`。如果你在其他时区，请修改为对应的时区，可以在[这里](https://gist.github.com/Xm798/54d188c65f683b84a74cfbe340c09518)查询时区列表（**十分重要**，否则时间会不正确）。

   ![img](https://s2.loli.net/2022/02/12/Lw2Hn48jKSGBPJF.png)

6. 展开触发器配置，选择自定义触发周期，填写 cron 表达式。例如：每 15 分钟检查一次，填写`0 */15 * * * * *`，每 30 分钟检查一次，填写`0 */30 * * * * *`，每小时整点触发，填写`0 0 * * * * *`。该间隔请注意与配置文件中`CHECK_INTERVAL`一致，以便运行睡前检查功能。

   ![img](https://s2.loli.net/2022/02/14/KQGvlWOq5EiARY8.png)

7. 跳转到 **函数管理 - 函数代码**页面，在目录中找到`dailynotehelper/config/config.example.yaml`，右键重命名为`config.yaml`，**并填写你的配置**（不支持环境变量）。

    ![img](https://s2.loli.net/2022/02/09/vxkaqoOfVw6hBgW.png)

8. 点击下方“**部署并测试**”，查看日志测试是否运行正常。

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

[![QQ](https://img.shields.io/badge/%20-QQ%20Group-blue?style=for-the-badge&logo=Tencent%20QQ&logoColor=EB1923&labelColor=eeeeee&color=EB1923)](https://jq.qq.com/?_wv=1027&k=CnNxc9hp)
[![Telegram](https://img.shields.io/badge/%20-Telegram%20Group-blue?style=for-the-badge&logo=Telegram&logoColor=26A5E4&labelColor=eeeeee&color=26A5E4)](https://t.me/+QtSxha7rXsc2ZTg1)

## Changelog

See [Changelog.md](./docs/CHANGELOG.md)

## Acknowledgements

### Open Source Projects and Contributors

|                                                   Project                                                   |                     Author                     |                                            License                                            |             Comment             |
| :---------------------------------------------------------------------------------------------------------: | :--------------------------------------------: | :-------------------------------------------------------------------------------------------: | :-----------------------------: |
| [genshin_task-resin-expedition_alert](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert) | [yaomeng0722](https://gitlab.com/yaomeng0722/) | [MIT](https://github.com/yaomeng0722/genshin_task-resin-expedition_alert/blob/master/LICENSE) | Initial version of this project |
|                                [onepush](https://github.com/y1ndan/onepush)                                 |      [y1ndan](https://gitlab.com/y1ndan/)      |                  [MIT](https://github.com/y1ndan/onepush/blob/main/LICENSE)                   |      message push channel       |
|                [genshin-checkin-helper](https://gitlab.com/y1ndan/genshin-checkin-helper)                 |      [y1ndan](https://gitlab.com/y1ndan/)      |         [GPLv3](https://gitlab.com/y1ndan/genshin-checkin-helper/-/blob/main/LICENSE)         |         API call method         |
|                                                      -                                                      |      [yllhwa](https://github.com/yllhwa)       |                                               -                                               | DS encryption algorithm reverse |

### Translators

| Language |      Name       |             Translators             |
| :------: | :-------------: | :---------------------------------: |
|  zh_TW   | 繁體中文 (台灣) | [KT-Yeh](https://github.com/KT-Yeh) |

## License

[GNU GPLv3](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/master/LICENSE)

> Translated by DeepL and Google from Simplified Chinese.
