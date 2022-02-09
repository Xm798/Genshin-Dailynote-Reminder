from typing_extensions import Literal
from typing import Optional, List
from pydantic import BaseModel,StrictBool

class ConfigData(BaseModel):
    RUN_ENV: Literal['local', 'cloud']
    UID: List
    COOKIE: List
    NAME: List

    RESIN_INFO: StrictBool
    COMMISSION_INFO: StrictBool
    EXPEDITION_INFO: StrictBool
    TROUNCE_INFO: StrictBool
    HOMECOIN_INFO: StrictBool

    RESIN_NOTICE: StrictBool
    RESIN_THRESHOLD: int
    COMMISSION_NOTICE_TIME: Optional[str]
    EXPEDITION_NOTICE: StrictBool
    HOMECOIN_NOTICE: StrictBool

    CHECK_INTERVAL: int
    CHECK_INTERVAL_AFTER_ALERT: Optional[int]
    SLEEP_TIME: Optional[str]

    WW_ID: Optional[str]
    WW_APP_SECRET: Optional[str]
    WW_APP_USERID: Optional[str]
    WW_APP_AGENTID: Optional[str]
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
    CQHTTP_MESSAGE_TYPE: Literal["private", "group"]
    CQHTTP_SEND_ID: Optional[str]
    CQHTTP_TOKEN: Optional[str]

    DD_BOT_TOKEN: Optional[str] 
    DD_BOT_SECRET: Optional[str]

    SCTKEY: Optional[str]

    PUSH_PLUS_TOKEN: Optional[str]
    PUSH_PLUS_USER: Optional[str]

    COOL_PUSH_SKEY: Optional[str]
    COOL_PUSH_MODE: Literal['send', 'psend', 'group', 'pgroup']
    COOL_PUSH_SENDID: Optional[str]

    QMSG_KEY: Optional[str]

    DISCORD_WEBHOOK: Optional[str]
    DISCORD_USERNAME: Optional[str]
    DISCORD_AVATAR: Optional[str]
    DISCORD_COLOR: Optional[int]

    IGOT_KEY: Optional[str]