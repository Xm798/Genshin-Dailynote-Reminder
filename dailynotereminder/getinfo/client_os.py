from .client import Client
from ..config import config
from .utils import request
from ..utils import log
from ..locale import _


class ClientOS(Client):
    def __init__(self, cookie: str = None):
        self.ltoken_map = {}
        self.client_type = 'os'
        self.server_list = ['os_usa', 'os_euro', 'os_cht', 'os_asia']
        self.user_agent = self.user_agent = (
            config.DEVICE_INFO.get('user_agent')
            or 'Mozilla/5.0 (Linux; Android 12; Mi 10 Pro Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 miHoYoBBSOversea/2.9.0'
        )
        super().__init__(cookie)
        self.roles_api = (
            'https://api-account-os.hoyolab.com/binding/api/getUserGameRolesByCookie'
        )
        self.daily_note_host = (
            config.OS_REVERSE_PROXY_HOST
            if config.OS_REVERSE_PROXY_HOST
            else 'bbs-api-os.hoyolab.com'
        )
        self.daily_note_api = (
            'https://' + self.daily_note_host + '/game_record/app/genshin/api/dailyNote'
        )
        self.proxies = (
            {'http': config.PROXY, 'https': config.PROXY} if config.PROXY else None
        )

    def _get_ds_salt(self) -> str:
        salt = 'okr4obncj8bw5a65hbnn5oo6ixjc3l9w'
        return salt

    def _get_headers(self) -> dict:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            "x-rpc-app_version": "2.9.0",
            "User-Agent": self.user_agent,
            "x-rpc-client_type": "2",
            "Origin": "https://webstatic-sea.hoyolab.com",
            "X-Requested-With": "com.mihoyo.hoyolab",
            "Referer": "https://webstatic-sea.hoyolab.com",
        }
        return headers

    def get_ltoken_map(self):
        for server in self.server_list:
            body = {'server': server, 'role_id': '12345678'}
            headers = self.get_headers(params=body, ds=True)
            try:
                r = request(
                    'get',
                    self.daily_note_api,
                    headers=headers,
                    params=body,
                    cookies=self.cookie,
                    proxies=self.proxies,
                )
                cookies_dict = r.cookies.get_dict()
                if cookies_dict.get('ltoken_v2'):
                    ltoken = {server: cookies_dict.get('ltoken_v2')}
                    self.ltoken_map.update(ltoken)
            except Exception as e:
                log.error(_(f'获取 {server} ltoken 失败！'))
                log.error(e)

    def get_roles_info(self):
        return super().get_roles_info()
        # self.get_ltoken_map()
        # roles_list = []
        # log.info(_('正在获取角色信息'))
        # for server in self.server_list:
        #     body = {'game_biz': 'hk4e_global', 'region': server}
        #     ltoken = {'ltoken_v2': self.ltoken_map.get(server)}
        #     cookie = self.cookie
        #     try:
        #         response = request(
        #             'get',
        #             self.roles_api,
        #             params=body,
        #             headers=self.headers,
        #             cookies=cookie,
        #             proxies=self.proxies,
        #         ).json()
        #     except Exception as e:
        #         log.error(e)
        #     else:
        #         if response.get('retcode') == 0:
        #             roles = self.parse_roles_info(response)
        #             roles_list.extend(roles)
        # return roles_list

    def get_daily_note_info(self, role):
        return super().get_daily_note_info(role)
