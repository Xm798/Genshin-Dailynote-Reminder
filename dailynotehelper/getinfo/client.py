'''
Thanks to y1ndan's genshin-checkin-helper(https://gitlab.com/y1ndan/genshin-checkin-helper), GPLv3 License.
'''
import pydantic
from .utils import *
from ..utils import log
from .model import BaseData
from typing import Optional
from .praseinfo import prase_info
from .exceptions import APIError


class Response(pydantic.BaseModel):
    retcode: int
    message: str
    data: Optional[dict]


class Client(object):
    def __init__(self, cookie: str = None):
        self.cookie = cookie_to_dict(cookie)
        self.headers = None
        self.oversea = None
        self._roles_info = None
        self.required_keys = {'region', 'game_uid',
                              'nickname', 'level', 'region_name'}

    @property
    def roles_info(self):
        if not self._roles_info:
            log.info('正在获取角色信息')
            url = self.roles_info_url
            response = request('get', url, headers=self.headers,
                               cookies=self.cookie).json()
            if response.get('retcode') != 0:
                log.error(response.get('message'))
            raw_roles_info = nested_lookup(response, 'list', fetch_first=True)
            self._roles_info = [
                extract_subset_of_dict(i, self.required_keys)
                for i in raw_roles_info
            ]
        return self._roles_info

    @property
    def daily_note(self):
        roles_info = self.roles_info
        self._daily_note = [
            self.get_daily_note(i['game_uid'], i['region'])
            for i in roles_info
        ]
        return self._daily_note

    def _get_dailynote_info(self, uid: str, region: str):
        url = self.daily_note_url
        body = {
            'role_id': uid,
            'server': region
        }
        response = Response.parse_obj(request('get', url, headers=get_headers(
            params=body, ds=True, oversea=self.oversea), params=body, cookies=self.cookie).json())
        if response.retcode == 0:
            pass
        elif response.retcode == -10001:
            log.error(response.retcode,response.message)
            raise APIError
        elif response.retcode == 10102:
            log.error('未开启实时便笺！')
            raise APIError
        else:
            log.error(response.retcode,response.message)
            raise APIError
        self.dailynote_info = BaseData.parse_obj(response.data)

    def prase_dailynote_info(self, role):
        self._get_dailynote_info(role['game_uid'], role['region'])
        result: str = prase_info(self.dailynote_info, role)
        message = "\n".join(result)
        return self.dailynote_info, message
