from .client import Client
from .utils import *

class Yuanshen(Client):
    def __init__(self, cookie: str = None, run_env: str = 'cloud'):
        super().__init__(cookie)
        self.headers = get_headers()
        self.oversea = False
        self.roles_info_url = 'https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn'
        self.daily_note_url = 'https://api-takumi.mihoyo.com/game_record/app/genshin/api/dailyNote' if run_env == 'cloud' \
            else 'https://api-takumi-record.mihoyo.com/game_record/app/genshin/api/dailyNote'