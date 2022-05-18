from typing_extensions import Literal
from typing import Optional, List
from pydantic import BaseModel, StrictBool, Field


class ConfigData(BaseModel):
    LANGUAGE: Literal['zh_CN', 'en_US', 'zh_TW'] = 'zh_CN'
    RUN_ENV: Literal['local', 'cloud'] = 'local'
    COOKIE: List[str] = []
    COOKIE_HOYOLAB: List[str] = []
    EXCLUDE_UID: List[int] = []
    DISPLAY_UID: StrictBool = True
    NICK_NAME: str = '亲爱的旅行者'

    RESIN_INFO: StrictBool = True
    COMMISSION_INFO: StrictBool = True
    EXPEDITION_INFO: StrictBool = True
    TROUNCE_INFO: StrictBool = True
    HOMECOIN_INFO: StrictBool = True
    HOMECOIN_THRESHOLD: float = 0.95
    TRANSFORMER_INFO: StrictBool = True

    RESIN_THRESHOLD: int = 140
    COMMISSION_NOTICE_TIME: Optional[str] = '21:00'
    EXPEDITION_NOTICE: StrictBool = True
    WAIT_ALL_EXPEDITION: StrictBool = False
    HOMECOIN_NOTICE: StrictBool = True
    TRANSFORMER: StrictBool = True

    CHECK_INTERVAL: int = 30
    SLEEP_TIME: Optional[str] = '23:00-07:00'

    WW_ID: Optional[str]
    WW_APP_SECRET: Optional[str]
    WW_APP_USERID: Optional[str]
    WW_APP_AGENTID: Optional[int]
    WW_BOT_KEY: Optional[str]

    BARK_URL: Optional[str]
    BARK_GROUP: Optional[str]
    BARK_ICON: Optional[str]
    BARK_ARCHIVE: Optional[str]
    BARK_LEVEL: Optional[str]

    TG_BOT_API: Optional[str]
    TG_BOT_TOKEN: Optional[str]
    TG_USER_ID: Optional[str]

    PUSHDEER_KEY: Optional[str]

    CQHTTP_URL: Optional[str]
    CQHTTP_MESSAGE_TYPE: Literal['private', 'group', 'guild'] = 'private'
    CQHTTP_SEND_ID: Optional[str]
    CQHTTP_SEND_CHANNEL_ID: Optional[str]
    CQHTTP_TOKEN: Optional[str]

    DD_BOT_TOKEN: Optional[str]
    DD_BOT_SECRET: Optional[str]

    SCTKEY: Optional[str]

    PUSH_PLUS_TOKEN: Optional[str]
    PUSH_PLUS_USER: Optional[str]

    COOL_PUSH_SKEY: Optional[str]
    COOL_PUSH_MODE: Literal['send', 'psend', 'group', 'pgroup'] = 'send'
    COOL_PUSH_SENDID: Optional[str]

    QMSG_KEY: Optional[str]

    DISCORD_WEBHOOK: Optional[str]
    DISCORD_USERNAME: Optional[str]
    DISCORD_AVATAR: Optional[str]
    DISCORD_COLOR: Optional[int]

    IGOT_KEY: Optional[str]

    MAIL_HOST: Optional[str]
    MAIL_PORT: Optional[int] = 465
    MAIL_STARTTLS: Optional[bool] = False
    MAIL_USERNAME: Optional[str]
    MAIL_PASSWORD: Optional[str]
    MAIL_TO: Optional[str]

    CUSTOM_NOTIFIER: dict = {}
