from .client import Client
from .utils import *
from ..config import config


class ClientOS(Client):
    def __init__(self, cookie: str = None):
        self.client_type = 'os'
        self.roles_api = 'https://api-os-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_global'
        self.daily_note_host = (
            config.OS_REVERSE_PROXY_HOST
            if config.OS_REVERSE_PROXY_HOST
            else 'bbs-api-os.hoyolab.com'
        )
        self.dailynote_api = (
            'https://' + self.daily_note_host + '/game_record/app/genshin/api/dailyNote'
        )
        self.proxies = (
            {'http': config.PROXY, 'https': config.PROXY} if config.PROXY else None
        )

        super().__init__(cookie)

    def _get_ds_salt(self) -> str:
        salt = 'okr4obncj8bw5a65hbnn5oo6ixjc3l9w'
        return salt

    def _get_headers(self) -> dict:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            "x-rpc-app_version": "2.9.0",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Pro Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 miHoYoBBSOversea/2.9.0",
            "x-rpc-client_type": "2",
            "Origin": "https://webstatic-sea.hoyolab.com",
            "X-Requested-With": "com.mihoyo.hoyolab",
            "Referer": "https://webstatic-sea.hoyolab.com",
        }
        return headers
