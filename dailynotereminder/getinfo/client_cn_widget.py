import os
import json

from .client import Client
from .utils import *
from ..utils import log, _
from .parse_info import parse_info
from ..config import config


class ClientCNWidget(Client):
    def __init__(self, cookie: str = None):
        base_takumi_api = 'https://api-takumi.mihoyo.com'
        base_takumi_record_api = 'https://api-takumi-record.mihoyo.com'
        self.roles_api = (
            base_takumi_api + '/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn'
        )
        self.get_multi_token_api = (
            base_takumi_api + '/auth/api/getMultiTokenByLoginTicket'
        )
        self.widget_api = (
            base_takumi_record_api + '/game_record/app/card/api/getWidgetData?game_id=2'
        )
        # self.widget_api = api_takumi_record + '/game_record/app/genshin/aapi/widget/v2'

        super().__init__(cookie)
        self.client_type = 'cn_widget'
        self.login_ticket: str = ''
        self.cookie_widget = {
            'stuid': self.cookie.get('ltuid')
            or self.cookie.get('account_id')
            or self.cookie.get('login_uid'),
            'ltuid': self.cookie.get('ltuid')
            or self.cookie.get('account_id')
            or self.cookie.get('login_uid'),
            'stoken': self.cookie.get('stoken'),
            'ltoken': self.cookie.get('ltoken'),
        }

    def parse_info(self, role) -> dict:
        data = None
        ck_updated = ''
        if not self.cookie_widget['stoken']:
            s = self._get_multi_token()
            if not s['status']:
                return s
            elif s['retcode'] == 200:
                ck_updated = s['message']
        try:
            r = request(
                'get',
                self.widget_api,
                headers=self.get_headers(params={'game_id': '2'}, ds=True),
                cookies=self.cookie_widget,
            )
            response = self.Response.parse_obj(r.json())
        except Exception as e:
            log.error(_('获取数据失败！'))
            log.error(e)
            message = e
            retcode = 999
        else:
            retcode = response.retcode
            if retcode == 0:
                data = response.data.get('data').get('data')
                result, data = parse_info(data, role, mode='lite')
                message = "\n".join(result) + f'\n\n️{ck_updated}'
            else:
                message = f'Retcode: {retcode}\nMessage: {response.message}'

        return {
            'status': True if retcode == 0 else False,
            'retcode': retcode,
            'data': data,
            'message': message,
            'ck_updated': True if ck_updated else False,
        }

    def _get_multi_token(self) -> dict:
        status = False
        retcode = 900
        if 'login_ticket' in self.cookie.keys():
            try:
                body = {
                    'login_ticket': self.cookie['login_ticket'],
                    'token_types': 3,
                    'uid': self.cookie_widget['stuid'],
                }
                r = request(
                    'get',
                    self.get_multi_token_api,
                    params=body,
                    headers=self.headers,
                    cookies=self.cookie,
                ).json()
            except Exception as e:
                log.error(e)
                message = e
            else:
                if r.get('retcode') == 0:
                    self.cookie_widget['stoken'] = r.get('data')['list'][0]['token']
                    self.cookie_widget['ltoken'] = r.get('data')['list'][1]['token']
                    status = True
                    cookie_new = {**self.cookie, **self.cookie_widget}
                    message = f"⭐更新 stoken 成功，以下是新的 Cookie，请手动更新至配置文件或环境变量中，以免下次运行失效。\n{dict_to_cookie(cookie_new)}"
                    retcode = 200
                    log.info(message)
                else:
                    message = r.get('message')
        else:
            message = _('Cookie 中缺少 login_ticket，请重新获取完整 Cookie！')

        return {'status': status, 'retcode': retcode, 'data': None, 'message': message}

    def _get_ds_salt(self) -> str:
        salt = 't0qEgfub6cvueAPgR5m9aQWWVciEer7v'
        return salt

    def _get_headers(self) -> dict:
        headers = {
            "Accept": '*/*',
            "x-rpc-sys_version": "16.3",
            "x-rpc-channel": 'appstore',
            "x-rpc-client_type": "1",
            "Referer": 'https://app.mihoyo.com',
            "x-rpc-device_name": 'iPhone',
            "x-rpc-device_model": 'iPhone14,2',
            "x-rpc-app_version": '2.45.1',
            "User-Agent": 'WidgetExtension/289 CFNetwork/1402.0.8 Darwin/22.2.0',
        }
        return headers
