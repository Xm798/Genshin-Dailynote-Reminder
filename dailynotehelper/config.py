import json

import yaml
import os
from .getinfo.model.configdata import ConfigData
import ast
import logging
from urllib import parse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


class Config:
    def __init__(self):
        self.config_data = {}

    def get_config(self):
        project_path = os.path.dirname(__file__)
        config_file = os.path.join(project_path, 'config', 'config.yaml')
        try:
            f = open(config_file, 'r', encoding='utf-8')
        except IOError:
            logging.warning('Cannot read the configuration file.')
            self.get_config_from_env()
        else:
            config_dict = yaml.load(f, Loader=yaml.FullLoader)
            for key in config_dict:
                k = key
                for key in config_dict[k]:
                    if 'COOKIE' in key or 'EXCLUDE_UID' in key:
                        self.config_data[key] = (
                            config_dict[k][key] if config_dict[k][key] else []
                        )
                    else:
                        self.config_data[key] = config_dict[k][key]

    def get_config_from_env(self):
        logging.info('Trying loading config from environment variables.')
        config_items = [
            "LANGUAGE",
            "COOKIE",
            "COOKIE_HOYOLAB",
            "EXCLUDE_UID",
            "DISPLAY_UID",
            "NICK_NAME",
            "RESIN_INFO",
            "COMMISSION_INFO",
            "EXPEDITION_INFO",
            "TROUNCE_INFO",
            "HOMECOIN_INFO",
            "TRANSFORMER_INFO",
            "RESIN_THRESHOLD",
            "COMMISSION_NOTICE_TIME",
            "EXPEDITION_NOTICE",
            "WAIT_ALL_EXPEDITION",
            "HOMECOIN_NOTICE",
            "HOMECOIN_THRESHOLD",
            "TRANSFORMER",
            "CHECK_INTERVAL",
            "SLEEP_TIME",
            "WW_ID",
            "WW_APP_AGENTID",
            "WW_APP_SECRET",
            "WW_APP_USERID",
            "WW_BOT_KEY",
            "BARK_URL",
            "BARK_GROUP",
            "BARK_ICON",
            "BARK_ARCHIVE",
            "BARK_LEVEL",
            "TG_BOT_API",
            "TG_BOT_TOKEN",
            "TG_USER_ID",
            "PUSHDEER_KEY",
            "CQHTTP_URL",
            "CQHTTP_MESSAGE_TYPE",
            "CQHTTP_SEND_ID",
            "CQHTTP_SEND_CHANNEL_ID",
            "CQHTTP_TOKEN",
            "DD_BOT_TOKEN",
            "DD_BOT_SECRET",
            "SCTKEY",
            "PUSH_PLUS_TOKEN",
            "PUSH_PLUS_USER",
            "COOL_PUSH_SKEY",
            "COOL_PUSH_MODE",
            "COOL_PUSH_SENDID",
            "QMSG_KEY",
            "DISCORD_WEBHOOK",
            "DISCORD_USERNAME",
            "DISCORD_AVATAR",
            "DISCORD_COLOR",
            "IGOT_KEY",
            "MAIL_HOST",
            "MAIL_PORT",
            "MAIL_STARTTLS",
            "MAIL_USERNAME",
            "MAIL_PASSWORD",
            "MAIL_TO",
            "CUSTOM_NOTIFIER",
            "GOTIFY_URL",
            "GOTIFY_TOKEN",
            "GOTIFY_PRIORITY",
        ]

        for key in config_items:
            eval_items = [
                'COOKIE',
                'EXCLUDE_UID',
                'CUSTOM_NOTIFIER',
                'RESIN_INFO',
                'COMMISSION_INFO',
                'EXPEDITION_INFO',
                'TROUNCE_INFO',
                'HOMECOIN_INFO',
                'TRANSFORMER_INFO',
                'EXPEDITION_NOTICE',
                'WAIT_ALL_EXPEDITION',
                'HOMECOIN_NOTICE',
                'TRANSFORMER',
                'MAIL_STARTTLS',
            ]
            if key in os.environ:
                if key == 'NICK_NAME':
                    value = (
                        parse.unquote(os.environ.get(key))
                        if '%' in os.environ.get(key)
                        else os.environ.get(key)
                    )
                else:
                    value = (
                        ast.literal_eval(os.environ.get(key))
                        if any([w in key and w for w in eval_items])
                        else os.environ.get(key)
                    )
                self.config_data.update({key: value})

    def parse_config(self):
        self.get_config()
        return ConfigData.parse_obj(self.config_data)


config = Config().parse_config()