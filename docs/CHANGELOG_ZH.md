
# 更新日志

### v2.1.4（2022-02-16）

New Features:

- 新增阿里云 FC 入口

### v2.1.3（2022-02-16）

New Features:

- 本地化新增中文繁体-台湾支持

Others:

- 重构本地化模块

### v2.1.2（2022-02-14）

New Features:

- 添加国际化支持并添加英文版，但英文文本需要校对。

### v2.1.1（2022-02-13）

New Features:

- 支持设置是否等全部探索派遣完成后再提醒，配置文件增加字段`WAIT_ALL_EXPEDITION`
  
Bug Fixes:

- 修复是否接收洞天宝钱信息开关不起作用的问题

### v2.1.0（2022-02-12）

New Features:

- 新增国际服支持
- 新增屏蔽部分角色功能

Bug Fixes:

- 修复 API 请求失败时异常退出的问题

### v2.0.1（2022-02-10）

New Features:

- 支持通过自定义 SMTP 服务器进行邮件推送

Bug Fixes:

- 修正部分推送配置为空时异常的问题

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