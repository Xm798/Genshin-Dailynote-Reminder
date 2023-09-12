# Changelog

## v2.3.3 (2023-09-12)

Feat:

- Added a roles info caching mechanism. The cache file is located in the config directory to avoid repeatedly fetching character information from the server. The default cache validity period is 3 days, and it will also be refreshed when the Cookie changes. Note: This does not apply to cloud function environments, as they cannot write to files.
- Updated the version notification default to only alert for significant updates, unless `CHECK_UPDATE` is set to `all` to alert for all versions, or `false` to disable.

## v2.3.2 (2023-09-11)

Fix:

- Changed the Cookie handling method to resolve the issue where V2 Cookies of oversea server could not be used

## v2.3.1 (2023-09-07)

Feat:

- Added update checking, enabled by default, can be turned off by setting `CHECK_UPDATE` to `false` in the configuration file.

Fix:

- Updated i18n resources.

## v2.3 (2023-09-05)

Fix:

- Fixed issue where standard mode could not run after the game updating to version 3.8

Feat:

- Added `DEVICE_INFO` to the configuration file to attempt to bypass the verification on the CN server. Ref [Miao-Yunzai](https://github.com/yoimiya-kokomi/Miao-Yunzai)

## v2.2.1 (2022-11-25)

Fix:

- Fix a bug that the oversea account can not work normally when the `LITE_MODE` is set to `true`

## v2.2.0 (2022-11-17)

Feat:

- A new lite mode for cn server when encountering a verification code

## v2.1.15（2022-11-15）

Fix:

- Fix the crash when switching language to English

## v2.1.14（2022-11-06）

Others:

- Add an prompt message of 1034 error

## v2.1.13（2022-10-05）

Fix:

- A cookie loading exception in some cases

## v2.1.12 (2022-10-03)

Feat:

- Now you can set the proxy [in the config file](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/9465eb0a1ad8f97344142e9de69b3f6878437b2b/dailynotereminder/config/config.example.yaml#L35-L37), and it will work on the fetch of oversea server info, requests of Telegram bot and Discord webhook, which can't be connected directly in China mainland. ([#7](https://github.com/Xm798/Genshin-Dailynote-Reminder/issues/7))
- You can set the reverse proxy api of oversea's daily note api [in the config file](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/9465eb0a1ad8f97344142e9de69b3f6878437b2b/dailynotereminder/config/config.example.yaml#L38-L39), which can be used to fetch the oversea server info without proxy

## v2.1.11 (2022-08-22)

Feat:

- Use the account role name when the nickname is empty in the configuration. ([@phpgao](https://github.com/phpgao)) ([#6](https://github.com/Xm798/Genshin-Dailynote-Helper/pull/6))
- Add push provider Gotify. ([@phpgao](https://github.com/phpgao)) ([#6](https://github.com/Xm798/Genshin-Dailynote-Helper/pull/6))
- Add localization translations of roles in version 3.0

Fix:

- Fix some wrong localized translations of some characters

## v2.1.10.1 (2022-08-07)

Fix:

- Update the api of oversear server, #22

## v2.1.10 (2022-07-25)

Feat:

- Added Russian language support by [@qarudeka](https://github.com/qarudeka), Ref [#2](https://github.com/Xm798/Genshin-Dailynote-Helper/pull/2)

## v2.1.9 (2022-07-24)

Feat:

- Added [Chanify](https://github.com/chanify/chanify) push support, [some fields](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/ffe9dd3751ba430040bfe7e39309525808c77e26/dailynotereminder/config/config.example.yaml#L207-L221) were added to the configuration file

## v2.1.8.2 (2022-07-07)

Feat:

- Updated the localized character names of Yelan and Shinobu

Others:

- Migrated the Chinese mainland docker image to Aliyun `registry.cn-shanghai.aliyuncs.com/xm798/genshin-dailynote-helper:latest`

## v2.1.8.1 (2022-05-19)

Feat:

- Supported loading configuration from environment variables, Ref [#37](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/37)

## v2.1.8 (2022-05-18)

Fix:

- Fixed the bug caused by the API change of cn server
- Fixed the incorrect time in the message title sent when the resin will overflow during sleep

## v2.1.7.5 (2022-05-02)

Fix:

- Fixed unexpected crash due to the API of oversea server did not return the information of the transformer, Ref [#29](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/29)
- Fixed the bug of the incorrect detection of Discord push status, Ref [#29](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/29)

## v2.1.7.4 (2022-04-30)

Fix:

- Added TW, HK, MO server support, fixed Ref [#28](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/28)

## v2.1.7.3 (2022-04-28)

Fix:

- Adjusted some zh-tw sentences, merged PR [#27](https://github.com/Xm798/Genshin-Dailynote-Helper/pull/27)

## v2.1.7.2 (2022-04-27)

Fix:

- Fixed a bug that the notification message will not be sent when the cookie expired

## v2.1.7.1 (2022-04-14)

New Features:

- Added custom title support and [NICK_NAME](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/da7e545940c76ef6c30cbc2d767d74137bf9513f/dailynotereminder/config/config.example.yaml#L32-L34) in the configuration file field

Fix:

- Fixed a bug that Ayato displayed English in zh_CN environment

Others:

- Formated and refactored some code

## v2.1.7 (2022-03-31)

New Features:

- Added parametric transformer reminder, added [TRANSFORMER_INFO](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/4c182324f0597c4964ef8aaf10711e6b38e76be7/dailynotereminder/config/config.example.yaml#L50-L53) and [TRANSFORMER_INFO](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/4c182324f0597c4964ef8aaf10711e6b38e76be7/dailynotereminder/config/config.example.yaml#L76-L78) to config file
- Added Kannari Ayato to the character list
  
## v2.1.6.1 (2022-03-16)

Others:

- Updated APP version in dailynote API of CN server to 2.23.1，update salt and request headers
- Updated APP version in dailynote API of oversea server to 2.6.0, update request headers

## v2.1.6 (2022-03-09)

New Features:

- Added QQ guild(channel) support，[#19](https://github.com/Xm798/Genshin-Dailynote-Helper/pull/19)，[config file adjustment](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/e8f190812a864f266e7f32c02793a2cfccc14722/dailynotereminder/config/config.example.yaml#L124-L128)
- Added alert threshold of homecoin，add [HOMECOIN_THRESHOLD](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/1f0730a2f7525bdf9aaac66c498b0e2412a6ebc7/dailynotereminder/config/config.example.yaml#L72) item in config file

## v2.1.5 (2022-02-28)

New Features:

- Changed expedition remaining time to finishing time
- Added custom notifier support, [#18](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/18)

## v2.1.4 (2022-02-16)

New Features:

- Added Aliyun Function Compute entry func

## v2.1.3 (2022-02-16)

New Features:

- Added zh_TW localization support

Others:

- Refactor localization modules

## v2.1.2 (2022-02-14)

New Features:

- Added multilingual internationalization support and add English version (But need someone to proofread the English translation)

## v2.1.1 (2022-02-13)

New Features:

- Supported setting whether to wait for all exploration dispatch to be completed before reminding, and adding the field `WAIT_ALL_EXPEDITION` to the configuration file
  
Bug Fixes:

- Fixed the problem that the switch of whether to receive information of Dongtianbao money does not work

## v2.1.0 (2022-02-12)

New Features:

- New international service support
- New function of blocking some roles

Bug Fixes:

- Fixed the problem of abnormal exit when API request fails

## v2.0.1 (2022-02-10)

New Features:

- Support email push via custom SMTP server

Bug Fixes:

- Fixed the problem that some push configurations are abnormal when they are empty

## v2.0.0 (2022-02-09)

BREAKING CHANGE:

- Changed the configuration file to yaml format

New Features:

- Supported multi-account and multi-role
- Supported for cloud function deployment
- Discord push support

Removed:

- Remove QQ active query module

Others:

- Added a domestic docker image
- Optimized push experience
- Refactored of some modules

## v1.3.3 (2022-02-06)

New Features:

- New Pushdeer push channel
- Removed old Serverchan push channel
- Optimized push content

Bug Fixes:

- Adjusted the cqhttp parameter to merge `CQHTTP_IP` and `CQHTTP_PORT` into `CQHTTP_URL`
- Adjusted the rendering style of some channels

## v1.3.2 (2022-01-12)

Bug Fixes

## v1.3.1 (2022-01-10)

New Features:

- Supported for custom BARK push servers

Bug Fixes:

- Fixed the problem of BARK push status detection error

## v1.3.0 (2022-01-10)

New Year

New Features:

- Added Caveman treasure money information, support setting Caveman treasure money overflow alert, new `RECEIVE_HOMECOIN_ALERT` field in configuration file
- Added a bedtime check, if the resin overflows during sleep will send an alert before sleep
- Added API switching options to support specifying older APIs when running on cloud servers
- Optimized message layout

Bug Fixes:

- Fixed the problem of invalid resin overflow prompt
- Updated the information of exploring and sending new characters
- Fixed Noelle character information error
- Optimized hibernation logic

## v1.2.5 (2021-12-24)

Bug Fixes:

- Synchronized the API changes

## v1.2.4 (2021-11-24)

Bug Fixes:

- Fix edan abnormal exit when a cookie error occurs

## v1.2.3 (2021-11-23)

New Features:

- CQHTTP push IP field support protocol header to support HTTPS

## v1.2.2 (2021-11-10)

New Features:

- Optimized the logic of daily commission reminder time judgment
- Added the judgment of daily commission rewards collection, so you will no longer be mistaken for not completing the commission after going to other worlds to collect rewards

## v1.2.1 (2021-11-01)

Bug Fixes:

- Fixed CQ-HTTP push authentication error, please note **profile field change**for users using CQ-HTTP

New Features:

- Added support for group push mode
- Added custom port support

## v1.2.0 (2021-11-01)

New Features:

- Supported night hibernation, no more late night non-stop disturbance
- Logs add per-round check resin value display

Bug Fixes:

- Fixed cqhttp push error prompt
- Some fields of the configuration file are changed to optional configuration

## v1.1.2 (2021-10-29)

New Features:

- Added cqhttp push

Others:

- Updated documentation

## v1.1.1 (2021-10-28)

New Features:

- Added a reminder of the completion of exploration dispatch
- Optimized alert titles

## v1.1.0 (2021-10-28)

New Features:

- Optimized alert logic
- Added account information display

Bug Fixes:

- Fixed the problem of incorrect hibernation time
