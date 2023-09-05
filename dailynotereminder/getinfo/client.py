"""
Thanks to y1ndan's genshin-checkin-helper(https://gitlab.com/y1ndan/genshin-checkin-helper), GPLv3 License.
"""
import hashlib
import json
import pydantic
import uuid
from typing import Optional
from urllib.parse import urlencode
from .utils import *
from ..utils import log, _
from .model import BaseData
from .parse_info import parse_info
from abc import ABC, abstractmethod


class Client(ABC):
    class Response(pydantic.BaseModel):
        retcode: int
        message: str
        data: Optional[dict]

    def __init__(self, cookie: str = None):
        self.daily_note_api = None
        self.roles_api = None
        self.cookie = cookie_to_dict(cookie)
        self.headers = None
        self.client_type = None
        self._roles_info = None
        self.required_keys = {'region', 'game_uid', 'nickname', 'level', 'region_name'}
        self.proxies = None
        self.device_id = str(
            uuid.uuid3(uuid.NAMESPACE_URL, uuid.UUID(int=uuid.getnode()).hex[-12:])
        )
        self.headers = self.get_headers()

    @property
    def roles_info(self):
        log.info(_('正在获取角色信息'))
        try:
            response = request(
                'get',
                self.roles_api,
                headers=self.headers,
                cookies=self.cookie,
                proxies=self.proxies,
            ).json()
        except Exception as e:
            log.error(e)
            return e
        else:
            if response.get('retcode') == 0:
                raw_roles_info = nested_lookup(response, 'list', fetch_first=True)
                self._roles_info = [
                    extract_subset_of_dict(i, self.required_keys)
                    for i in raw_roles_info
                ]
                return self._roles_info
            else:
                return response.get('message')

    def parse_info(self, role):
        data = None
        body = {'role_id': role['game_uid'], 'server': role['region']}
        try:
            r = request(
                'get',
                self.daily_note_api,
                headers=self.get_headers(params=body, ds=True),
                params=body,
                cookies=self.cookie,
                proxies=self.proxies,
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
                data = BaseData.parse_obj(response.data)
                result = parse_info(data, role, mode='standard')
                message = "\n".join(result)
            else:
                if retcode == 10102:
                    message = _('未开启实时便笺！')
                elif retcode == 1034:
                    message = _('账号异常！请登录米游社APP进行验证。')
                else:
                    message = f'Retcode: {retcode}\nMessage: {response.message}'
                log.error(message)

        return {
            'status': True if retcode == 0 else False,
            'retcode': retcode,
            'data': data,
            'message': message,
        }

    def get_headers(
        self,
        params: dict = None,
        body: dict = None,
        ds: bool = False,
    ) -> dict:
        headers = self._get_headers()
        if ds:
            ds = self.get_ds(params, body)
            headers.update({'DS': ds, 'x-rpc-device_id': self.device_id.upper()})
        return headers

    def get_ds(self, params, body: dict) -> str:
        t = str(int(time.time()))
        r = str(random.randint(100000, 200000))
        b = json.dumps(body) if body else ''
        q = urlencode(params) if params else ''
        salt = self._get_ds_salt()
        text = f'salt={salt}&t={t}&r={r}&b={b}&q={q}'
        md5 = hashlib.md5()
        md5.update(text.encode())
        c = md5.hexdigest()
        return f'{t},{r},{c}'

    @abstractmethod
    def _get_ds_salt(self) -> str:
        pass

    @abstractmethod
    def _get_headers(self) -> dict:
        pass