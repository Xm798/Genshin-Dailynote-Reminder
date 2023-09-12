"""
Thanks to y1ndan's genshin-checkin-helper(https://gitlab.com/y1ndan/genshin-checkin-helper), GPLv3 License.
"""
import hashlib
import json
import random
import time
import uuid
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional
from urllib.parse import urlencode

import pydantic

from ..config import config
from ..locale import _
from ..utils import log
from .model import BaseData
from .parse_info import parse_info
from .utils import (
    cookie_to_dict,
    extract_subset_of_dict,
    hash_string,
    nested_lookup,
    request,
)


class Client(ABC):
    class Response(pydantic.BaseModel):
        retcode: int
        message: str
        data: Optional[dict]

    def __init__(self, cookie: str = None):
        self.daily_note_api = None
        self.roles_api = None
        self.cookie = cookie_to_dict(cookie)
        self.cookie_hash = hash_string(json.dumps(self.cookie, sort_keys=True))
        self.headers = None
        self.client_type = None
        self.required_keys = {'region', 'game_uid', 'nickname', 'region_name'}
        self.proxies = None
        device_id = config.DEVICE_INFO.get('device_id')
        self.device_id = (
            device_id
            if device_id
            else str(
                uuid.uuid3(uuid.NAMESPACE_URL, uuid.UUID(int=uuid.getnode()).hex[-12:])
            )
        )
        self.headers = self.get_headers()
        self.roles_cache_file = (
            Path(__file__).parent.parent / 'config' / '.roles_info.cache'
        )
        self.cache_expire_time = 3 * 24 * 60 * 60

    def load_roles_info_cache(self):
        if self.roles_cache_file.exists():
            try:
                with self.roles_cache_file.open('r') as f:
                    all_cache_data = json.load(f)

                if all_cache_data:
                    cache_data = all_cache_data.get(self.cookie_hash, {})
                    last_update_time = cache_data.get('last_update_time', 0)
                    roles_list = cache_data.get('roles_list', None)

                    if (
                        time.time() - last_update_time < self.cache_expire_time
                        and roles_list
                    ):
                        return roles_list

                    self.cleanup_cache(all_cache_data)

            except Exception as e:
                log.error(f"Could not load roles info from cache file: {e}")

        return None

    def cleanup_cache(self, all_cache_data):
        updated_cache_data = {}
        current_time = time.time()
        for k, v in all_cache_data.items():
            if current_time - v.get('last_update_time', 0) <= self.cache_expire_time:
                updated_cache_data[k] = v

        with self.roles_cache_file.open('w') as f:
            json.dump(updated_cache_data, f)

    def fetch_roles_info(self):
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

        if response.get('retcode') == 0:
            roles_list = self.parse_roles_info(response)
            cache_data = {'roles_list': roles_list, 'last_update_time': time.time()}
            all_cache_data = {}

            if self.roles_cache_file.exists():
                try:
                    with self.roles_cache_file.open('r') as f:
                        all_cache_data = json.load(f)
                except Exception as e:
                    log.error(f"Could not load roles info from cache file: {e}")

            all_cache_data[self.cookie_hash] = cache_data

            try:
                with self.roles_cache_file.open('w') as f:
                    json.dump(all_cache_data, f)
            except Exception as e:
                log.error(f"Could not write roles info to cache file: {e}")
            return roles_list
        else:
            message = response.get('message')
            log.error(message)
            return message

    @abstractmethod
    def get_roles_info(self):
        roles_list = self.load_roles_info_cache()

        if roles_list:
            log.info(_('从缓存文件中获取角色信息'))
            return roles_list
        else:
            log.info(_('正在从服务器获取角色信息'))
            return self.fetch_roles_info()

    def parse_roles_info(self, response):
        roles = nested_lookup(response, 'list', fetch_first=True)
        roles_list = [extract_subset_of_dict(i, self.required_keys) for i in roles]
        return roles_list

    @abstractmethod
    def get_daily_note_info(self, role):
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
