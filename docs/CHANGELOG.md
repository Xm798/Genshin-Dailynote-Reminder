# Changelog

### v2.1.6.1 (2022-03-16)

Others:

- Update APP version in dailynote API of CN server to 2.23.1，update salt and request headers.
- Update APP version in dailynote API of oversea server to 2.6.0, update request headers.

### v2.1.6（2022-03-09）

New Features:

- Add QQ guild(channel) support，[#19](https://github.com/Xm798/Genshin-Dailynote-Helper/pull/19)，[config file adjustment](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/e8f190812a864f266e7f32c02793a2cfccc14722/dailynotehelper/config/config.example.yaml#L124-L128).
- Add alert threshold of homecoin，add [HOMECOIN_THRESHOLD](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/1f0730a2f7525bdf9aaac66c498b0e2412a6ebc7/dailynotehelper/config/config.example.yaml#L72) item in config file.


### v2.1.5 (2022-02-28)

New Features:

- Change expedition remaining time to finishing time.
- Add custom notifier support, [#18](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/18).

### v2.1.4 (2022-02-16)

New Features:

- Add Aliyun Function Compute entry func.

### v2.1.3 (2022-02-16)

New Features:

- Add zh_TW localization support.

Others:

- Refactor localization modules.

### v2.1.2 (2022-02-14)

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
- Fix the problem of incorrect hibernation time.