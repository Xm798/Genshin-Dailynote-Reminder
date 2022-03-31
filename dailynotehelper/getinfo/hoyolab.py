from .client import Client
from .utils import *


class Genshin(Client):
    def __init__(self, cookie: str = None):
        super().__init__(cookie)
        self.headers = get_headers(oversea=True)
        self.oversea = True
        self.roles_info_url = 'https://api-os-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_global'
        self.daily_note_url = (
            'https://bbs-api-os.mihoyo.com/game_record/app/genshin/api/dailyNote'
        )
