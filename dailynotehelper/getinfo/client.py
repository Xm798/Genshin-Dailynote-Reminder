"""
Thanks to y1ndan's genshin-checkin-helper(https://gitlab.com/y1ndan/genshin-checkin-helper), GPLv3 License.
"""
import pydantic
from .utils import *
from ..utils import log, _
from .model import BaseData
from typing import Optional
from .praseinfo import prase_info


class Response(pydantic.BaseModel):
    retcode: int
    message: str
    data: Optional[dict]


class Client(object):
    def __init__(self, cookie: str = None):
        self.daily_note_url = None
        self.roles_info_url = None
        self.dailynote_info = None
        self.error_message = None
        self.cookie = cookie_to_dict(cookie)
        self.headers = None
        self.oversea = None
        self._roles_info = None
        self.required_keys = {'region', 'game_uid', 'nickname', 'level', 'region_name'}
        self.proxies = None

    @property
    def roles_info(self):
        log.info(_('正在获取角色信息'))
        url = self.roles_info_url
        try:
            response = request(
                'get',
                url,
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

    def _get_dailynote_info(self, uid: str, region: str):
        url = self.daily_note_url
        body = {'role_id': uid, 'server': region}
        try:
            r = request(
                'get',
                url,
                headers=get_headers(params=body, ds=True, oversea=self.oversea),
                params=body,
                cookies=self.cookie,
                proxies=self.proxies,
            )
            # log.info(r.text)
            response = Response.parse_obj(r.json())
        except Exception as e:
            log.error(_('获取数据失败！'))
            log.error(e)
            self.dailynote_info = None
        else:
            if response.retcode == 0:
                self.dailynote_info = BaseData.parse_obj(response.data)
                pass
            elif response.retcode == -10001:
                log.error(f'Retcode: {response.retcode},\nMessage: {response.message}')
                self.dailynote_info = None
                self.error_message = f'Retcode: {response.retcode}\nMessage: {response.message}'
            elif response.retcode == 10102:
                log.error(_('未开启实时便笺！'))
                self.dailynote_info = None
                self.error_message = _('未开启实时便笺！')
            elif response.retcode == 1034:
                log.error(_('账号异常！请登录米游社APP进行验证。'))
                self.dailynote_info = None
                self.error_message = _('账号异常！请登录米游社APP进行验证。')
            else:
                log.error(f'Retcode: {response.retcode},\nMessage: {response.message}')
                self.dailynote_info = None
                self.error_message = f'Retcode: {response.retcode}\nMessage: {response.message}'

    def prase_dailynote_info(self, role):
        self._get_dailynote_info(role['game_uid'], role['region'])
        if self.dailynote_info:
            result = prase_info(self.dailynote_info, role)
            message = "\n".join(result)
        else:
            message = self.error_message
        return self.dailynote_info, message
