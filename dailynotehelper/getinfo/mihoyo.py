from .client import Client
from .utils import *
from ..utils import log, _
from .parse_info import parse_info

class Yuanshen(Client):
    def __init__(self, cookie: str = None):
        super().__init__(cookie)
        self.headers = get_headers(client_type='cn')
        self.client_type = 'cn'
        self.login_ticket: str = ''
        self.cookie_widget = {
            'stuid': self.cookie.get('ltuid') or self.cookie.get('account_id') or self.cookie.get('login_uid'),
            'ltuid': self.cookie.get('ltuid') or self.cookie.get('account_id') or self.cookie.get('login_uid'),
            'stoken': self.cookie.get('stoken'),
            'ltoken': self.cookie.get('ltoken')
        }
        api_takumi = 'https://api-takumi.mihoyo.com'
        api_takumi_record = 'https://api-takumi-record.mihoyo.com'
        self.roles_api = api_takumi + '/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn'
        self.get_multitoken_api = api_takumi + '/auth/api/getMultiTokenByLoginTicket'
        self.dailynote_api = api_takumi_record + '/game_record/app/genshin/api/dailyNote'
        self.widget_api = api_takumi_record + '/game_record/app/card/api/getWidgetData?game_id=2'

    def parse_widget_info(self, role):
        data = None
        ck_updated = ''
        if not self.cookie_widget['stoken']:
            s = self._get_multitoken()
            if not s['status']:
                return s
            elif s['retcode'] == 200:
                ck_updated = s['message']
        try:
            r = request(
                'get',
                self.widget_api,
                headers=get_headers(params={'game_id': '2'}, ds=True, client_type='cn_widget'),
                cookies=self.cookie_widget
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
            'message': message
        }

    def _get_multitoken(self):
        status = False
        retcode = 900
        if 'login_ticket' in self.cookie.keys():
            try:
                body = {'login_ticket': self.cookie['login_ticket'], 'token_types': 3,
                        'uid': self.cookie_widget['stuid']}
                r = request(
                    'get',
                    self.get_multitoken_api,
                    params=body,
                    headers=self.headers,
                    cookies=self.cookie,
                ).json()
            except Exception as e:
                log.error(e)
                message = e
            else:
                if r.get('retcode') == 0:
                    self.cookie_widget['stoken'] = r.get("data")["list"][0]["token"]
                    self.cookie_widget['ltoken'] = r.get("data")["list"][1]["token"]
                    status = True
                    cookie_new = {**self.cookie, **self.cookie_widget}
                    message = f"⭐更新 stoken 成功，以下是新的 Cookie，请手动更新至配置文件或环境变量中，以免下次运行失效。\n{dict_to_cookie(cookie_new)}"
                    retcode = 200
                    log.info(message)
                else:
                    message = r.get("message")
        else:
            message = _('Cookie 中缺少 login_ticket，请重新获取完整 Cookie！')

        return {
                'status': status,
                'retcode': retcode,
                'data': None,
                'message': message
            }

