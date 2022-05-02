
# 更新日志

## v2.1.7.5（2022-05-02）

Fix:

- 修复国际服接口偶发异常不返回参量质变仪数据，导致意外崩溃的问题，issue #29。
- 修复 Discord 推送状态检测异常的问题，issue #29。

## v2.1.7.4（2022-04-30）

Fix:

- 修复台港澳服报错问题, issue #28。

## v2.1.7.3（2022-04-28）

Fix:

- 调整部分中文繁体-台湾本地化翻译, PR #27.

## v2.1.7.2（2022-04-27）

Fix:

- 修复 Cookie 失效时不推送提醒的问题

## v2.1.7.1（2022-04-14）

New Features:

- 增加称呼自定义，配置文件字段增加 [NICK_NAME](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/da7e545940c76ef6c30cbc2d767d74137bf9513f/dailynotehelper/config/config.example.yaml#L32-L34) 。

Fix:

- 修复神里绫人在简体中文下显示英文名字的错误

Others:

- 格式化和重构了一些代码

## v2.1.7（2022-03-31）

New Features:

- 增加参量质变仪提醒，配置文件字段增加 [TRANSFORMER_INFO](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/4c182324f0597c4964ef8aaf10711e6b38e76be7/dailynotehelper/config/config.example.yaml#L51-L53) 和 [TRANSFORMER_INFO](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/4c182324f0597c4964ef8aaf10711e6b38e76be7/dailynotehelper/config/config.example.yaml#L76-L78) 。
- 角色列表添加神里绫人

## v2.1.6.1 (2022-03-16)

Others:

- 更新国服每日便笺接口 APP 版本为 2.23.1，更新加密算法 salt，更新 headers
- 更新国际服每日便笺接口 APP 版本为 2.6.0，更新 headers

## v2.1.6（2022-03-09）

New Features:

- 增加 QQ 频道推送支持，[#19](https://github.com/Xm798/Genshin-Dailynote-Helper/pull/19) ，[配置文件字段调整](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/e8f190812a864f266e7f32c02793a2cfccc14722/dailynotehelper/config/config.example.yaml#L124-L128) 。
- 增加洞天宝钱提醒阈值设置，配置文件增加字段 [HOMECOIN_THRESHOLD](https://github.com/Xm798/Genshin-Dailynote-Helper/blob/1f0730a2f7525bdf9aaac66c498b0e2412a6ebc7/dailynotehelper/config/config.example.yaml#L72) 。

## v2.1.5（2022-02-28）

New Features:

- 调整探索派遣倒计时为完成时间
- 增加自定义推送支持，[#18](https://github.com/Xm798/Genshin-Dailynote-Helper/issues/18)

## v2.1.4（2022-02-16）

New Features:

- 新增阿里云 FC 入口

## v2.1.3（2022-02-16）

New Features:

- 本地化新增中文繁体 - 台湾支持

Others:

- 重构本地化模块

## v2.1.2（2022-02-14）

New Features:

- 添加国际化支持并添加英文版，但英文文本需要校对。

## v2.1.1（2022-02-13）

New Features:

- 支持设置是否等全部探索派遣完成后再提醒，配置文件增加字段`WAIT_ALL_EXPEDITION`
  
Bug Fixes:

- 修复是否接收洞天宝钱信息开关不起作用的问题

## v2.1.0（2022-02-12）

New Features:

- 新增国际服支持
- 新增屏蔽部分角色功能

Bug Fixes:

- 修复 API 请求失败时异常退出的问题

## v2.0.1（2022-02-10）

New Features:

- 支持通过自定义 SMTP 服务器进行邮件推送

Bug Fixes:

- 修正部分推送配置为空时异常的问题

## v2.0.0（2022-02-09）

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

## v1.3.3（2022-02-06）

New Features:

- 新增 Pushdeer 推送通道
- 移除旧版 Serverchan 推送通道
- 优化推送内容

Bug Fixes:

- 调整 cqhttp 参数，将`CQHTTP_IP`和`CQHTTP_PORT`合并为`CQHTTP_URL`
- 调整部分通道渲染样式

## v1.3.2（2022-01-12）

Bug Fixes

## v1.3.1（2022-01-10）

New Features:

- 支持自定义 BARK 推送服务器

Bug Fixes:

- 修复 BARK 推送状态检测错误的问题

## v1.3.0（2022-01-10）

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

## v1.2.5（2021-12-24）

Bug Fixes：

- 同步米游社 API 变动，更换新的 API。

## v1.2.4（2021-11-24）

Bug Fixes：

- 修复 cookie 出错时的异常退出问题

## v1.2.3（2021-11-23）

New Features:

- CQHTTP 推送 IP 字段支持协议头，以支持 HTTPS

## v1.2.2（2021-11-10）

New Features:

- 优化每日委托提醒时间判断逻辑
- 增加每日委托奖励领取情况判断，去他人世界做委托领取奖励后不再会被误认为未完成委托。

## v1.2.1（2021-11-01）

Bug Fixes：

- 修复 CQ-HTTP 推送鉴权错误，请使用 CQ-HTTP 的用户注意**配置文件字段变动**。

New Features:

- 增加群推送模式支持
- 增加自定义端口支持

## v1.2.0 (2021-11-01)

New Features:

- 支持夜间休眠，再也不会深夜不停扰民了
- 日志增加每轮检查树脂值显示

Bug Fixes：

- 修复 cqhttp 推送错误提示
- 配置文件部分字段改为可选配置

## v1.1.2（2021-10-29）

New Features:

- 增加 cqhttp 推送

Others:

- 更新文档

## v1.1.1 (2021-10-28)

New Features:

- 增加探索派遣完成提醒
- 优化提醒标题

## v1.1.0 (2021-10-28)

New Features:

- 优化提醒逻辑
- 增加账号信息显示

Bug Fixes:

- 修复休眠时间不正确的问题
