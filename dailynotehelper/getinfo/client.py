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
        self._daily_note = None
        self.cookie = cookie_to_dict(cookie)
        self.headers = None
        self.oversea = None
        self._roles_info = None
        self.required_keys = {'region', 'game_uid', 'nickname', 'level', 'region_name'}

    @property
    def roles_info(self):
        log.info(_('正在获取角色信息'))
        url = self.roles_info_url
        try:
            response = request(
                'get', url, headers=self.headers, cookies=self.cookie
            ).json()
        except Exception as e:
            log.error(e)
            return e
        else:
            if response.get('retcode') == 0:
                raw_roles_info = nested_lookup(response, 'list', fetch_first=True)
                self._roles_info = [
                    extract_subset_of_dict(i, self.required_keys) for i in raw_roles_info
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
            )
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
                log.error(response.retcode, response.message)
                self.dailynote_info = None
            elif response.retcode == 10102:
                log.error(_('未开启实时便笺！'))
                self.dailynote_info = None
            else:
                log.error(response.retcode, response.message)
                self.dailynote_info = None

    def prase_dailynote_info(self, role):
        self._get_dailynote_info(role['game_uid'], role['region'])
        result: str = (
            prase_info(self.dailynote_info, role) if self.dailynote_info else ''
        )
        message = "\n".join(result)
        return self.dailynote_info, message
