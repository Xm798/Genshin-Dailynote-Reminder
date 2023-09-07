import os
import json

from .client import Client
from .utils import *
from ..utils import log, _
from ..config import config


class ClientCN(Client):
    def __init__(self, cookie: str = None):
        self._device_fp = None
        self._device_seed = None
        self.client_type = 'cn'
        self.get_fp_api = 'https://public-data-api.mihoyo.com/device-fp/api/getFp'
        ua = config.DEVICE_INFO.get('user_agent')
        default_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.45.1"
        self.user_agent = ua if ua else default_ua
        super().__init__(cookie)
        base_takumi_api = 'https://api-takumi.mihoyo.com'
        base_takumi_record_api = 'https://api-takumi-record.mihoyo.com'
        self.roles_api = (
            base_takumi_api + '/binding/api/getUserGameRolesByCookie?game_biz=hk4e_cn'
        )
        self.get_multi_token_api = (
            base_takumi_api + '/auth/api/getMultiTokenByLoginTicket'
        )
        self.daily_note_api = (
            base_takumi_record_api + '/game_record/app/genshin/api/dailyNote'
        )
        # self.widget_api = api_takumi_record + '/game_record/app/genshin/aapi/widget/v2'

    @property
    def device_fp(self) -> str:
        if not self._device_fp:
            self._device_fp = (
                config.DEVICE_INFO.get('device_fp')
                or os.environ.get('GDR_DEVICE_FP')
                or self.get_device_fp()
            )
            os.environ['GDR_DEVICE_FP'] = self._device_fp
        return self._device_fp

    def generate_device_seed(self):
        device_seed_id = sample_string('abcdefghijklmnopqrstuvwxyz0123456789', 16)
        device_seed_time = str(int(round(time.time() * 1000)))
        self._device_seed = {"id": device_seed_id, "time": device_seed_time}
        device_seed_str = json.dumps(self._device_seed)
        os.environ['DEVICE_SEED'] = device_seed_str

    @property
    def device_seed(self) -> dict:
        if not self._device_seed:
            device_seed_str = os.getenv('DEVICE_SEED')
            if device_seed_str:
                try:
                    self._device_seed = json.loads(device_seed_str)
                    log.info(
                        f'Loaded DEVICE_SEED from environment variables: {self._device_seed}'
                    )
                except json.JSONDecodeError:
                    log.warning(
                        'Invalid DEVICE_SEED in environment variables. Regenerating.'
                    )
                    self.generate_device_seed()
            else:
                self.generate_device_seed()
        return self._device_seed

    def get_device_fp(self):
        default_fp = "38d7ee834d1e9"
        headers = {
            "Host": "public-data-api.mihoyo.com",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-site",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Fetch-Mode": "cors",
            "Origin": "https://bbs.mihoyo.com",
            "User-Agent": self.user_agent,
            "Referer": "https://bbs.mihoyo.com/",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Content-Type": "application/json;charset=UTF-8",
        }

        body = {
            "device_id": self.device_id.lower(),
            "seed_id": self.device_seed["id"],
            "seed_time": self.device_seed["time"],
            "platform": "5",
            "device_fp": default_fp,
            "app_name": "account_cn",
            "ext_fields": json.dumps(
                {
                    "userAgent": self.user_agent,
                    "browserScreenSize": 243750,
                    "maxTouchPoints": 5,
                    "isTouchSupported": True,
                    "browserLanguage": "en-US",
                    "browserPlat": "iPhone",
                    "browserTimeZone": "Asia/Shanghai",
                    "webGlRender": "Apple GPU",
                    "webGlVendor": "Apple Inc.",
                    "numOfPlugins": 5,
                    "listOfPlugins": [
                        "PDF Viewer",
                        "Chrome PDF Viewer",
                        "Chromium PDF Viewer",
                        "Microsoft Edge PDF Viewer",
                        "WebKit built-in PDF",
                    ],
                    "screenRatio": 3,
                    "deviceMemory": "unknown",
                    "hardwareConcurrency": "4",
                    "cpuClass": "unknown",
                    "ifNotTrack": "unknown",
                    "ifAdBlock": 0,
                    "hasLiedResolution": 1,
                    "hasLiedOs": 0,
                    "hasLiedBrowser": 0,
                }
            ),
        }
        try:
            # TODO: delete
            print(headers)
            r = request(
                'post',
                self.get_fp_api,
                json=body,
                headers=headers,
                cookies=self.cookie,
            ).json()
            if r.get('retcode') == 0 and r.get('data').get('code') == 200:
                fp = r.get('data').get('device_fp')
                log.info(f'获取到新的 device_fp，建议写入配置文件。DEVICE_FP: {fp}')
            else:
                log.error('Get device_fp failed!' + r.get('message'))
                fp = None
            return fp
        except Exception as e:
            log.error('Get device_fp failed!' + str(e))
            return None

    def _get_ds_salt(self) -> str:
        salt = 'xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs'
        return salt

    def _get_headers(self) -> dict:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            "x-rpc-app_version": "2.45.1",
            "User-Agent": self.user_agent,
            "x-rpc-client_type": "5",
            "x-rpc-page": "v4.0.5-ys_#/ys/daily",
            "Origin": "https://webstatic.mihoyo.com",
            "Referer": "https://webstatic.mihoyo.com/",
        }
        if self.device_fp:
            headers.update({'x-rpc-device_fp': self.device_fp})
        return headers
