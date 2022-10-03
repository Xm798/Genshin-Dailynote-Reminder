from .client import Client
from .utils import *
from ..config import config


class Genshin(Client):
    def __init__(self, cookie: str = None):
        super().__init__(cookie)
        self.headers = get_headers(oversea=True)
        self.oversea = True
        self.roles_info_url = 'https://api-os-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_global'
        self.daily_note_host = (
            config.OS_REVERSE_PROXY_HOST
            if config.OS_REVERSE_PROXY_HOST
            else 'bbs-api-os.hoyolab.com'
        )
        self.daily_note_url = (
            'https://' + self.daily_note_host + '/game_record/app/genshin/api/dailyNote'
        )
        self.proxies = (
            {'http': config.PROXY, 'https': config.PROXY} if config.PROXY else None
        )
