import hashlib
import random
import time
import requests
import uuid
import json
from ..utils import log
from urllib.parse import urlencode


def get_ds(ds_type: str, params, body: dict) -> str:
    t = str(int(time.time()))
    r = str(random.randint(100000, 200000))
    b = json.dumps(body) if body else ''
    q = urlencode(params) if params else ''
    salt = {
        'cn': 'xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs',
        'os': 'okr4obncj8bw5a65hbnn5oo6ixjc3l9w',
        'cn_widget': 't0qEgfub6cvueAPgR5m9aQWWVciEer7v',
    }
    text = f'salt={salt[ds_type]}&t={t}&r={r}&b={b}&q={q}'
    md5 = hashlib.md5()
    md5.update(text.encode())
    c = md5.hexdigest()
    return f'{t},{r},{c}'


def get_headers(
        params: dict = None, body: dict = None, ds: bool = False, client_type: str = 'cn'
) -> dict:
    client = {
        'cn': {
            'Accept': 'application/json, text/plain, */*',
            "x-rpc-app_version": "2.40.1",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/2.40.1",
            "x-rpc-client_type": "5",
            "x-rpc-page": "3.1.3_#/ys",
            "Origin": "https://webstatic.mihoyo.com",
            "X-Requested-With": "com.mihoyo.hyperion",
            "Referer": "https://webstatic.mihoyo.com/",
        },
        'os': {
            'Accept': 'application/json, text/plain, */*',
            "x-rpc-app_version": "2.9.0",
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mi 10 Pro Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 miHoYoBBSOversea/2.9.0",
            "x-rpc-client_type": "2",
            "Origin": "https://webstatic-sea.hoyolab.com",
            "X-Requested-With": "com.mihoyo.hoyolab",
            "Referer": "https://webstatic-sea.hoyolab.com",
        },
        'cn_widget': {
            "Accept": '*/*',
            "x-rpc-sys_version": "16.1",
            "x-rpc-channel": 'appstore',
            "x-rpc-client_type": "2",
            "Referer": 'https://app.mihoyo.com',
            "x-rpc-device_name": 'iPhone',
            "x-rpc-device_model": 'iPhone14,2',
            "x-rpc-app_version": '2.40.1',
            "User-Agent": 'WidgetExtension/264 CFNetwork/1399 Darwin/22.1.0'
        }
    }
    headers = client[client_type]
    if ds:
        ds = get_ds(client_type, params, body)
        headers.update(
            {
                'DS': ds,
                'x-rpc-device_id': str(
                    uuid.uuid3(uuid.NAMESPACE_URL, uuid.UUID(int = uuid.getnode()).hex[-12:])
                )
                .replace('-', '')
                .upper(),
            }
        )
    return headers


def nested_lookup(obj, key, with_keys=False, fetch_first=False):
    result = list(_nested_lookup(obj, key, with_keys=with_keys))
    if with_keys:
        values = [v for k, v in _nested_lookup(obj, key, with_keys=with_keys)]
        result = {key: values}
    if fetch_first:
        result = result[0] if result else result
    return result


def _nested_lookup(obj, key, with_keys=False):
    if isinstance(obj, list):
        for i in obj:
            yield from _nested_lookup(i, key, with_keys=with_keys)
    if isinstance(obj, dict):
        for k, v in obj.items():
            if key == k:
                if with_keys:
                    yield k, v
                else:
                    yield v

            if isinstance(v, list) or isinstance(v, dict):
                yield from _nested_lookup(v, key, with_keys=with_keys)


def extract_subset_of_dict(raw_dict, keys):
    subset = {}
    if isinstance(raw_dict, dict):
        subset = {key: value for key, value in raw_dict.items() if key in keys}
    return subset


def request(*args, **kwargs):
    is_retry = True
    count = 0
    max_retries = 3
    sleep_seconds = 5
    while is_retry and count <= max_retries:
        try:
            s = requests.Session()
            response = s.request(*args, **kwargs)
            is_retry = False
        except Exception as e:
            if count == max_retries:
                raise e
            log.error(f'Request failed: {e}')
            count += 1
            log.info(
                f'Trying to reconnect in {sleep_seconds} seconds ({count}/{max_retries})...'
            )
            time.sleep(sleep_seconds)
        else:
            return response


def cookie_to_dict(cookie: str) -> dict:
    if cookie and '=' in cookie:
        lines = [line.strip().split('=') for line in cookie.split(';')]
        cookie = {}
        for item in lines:
            if not item[0]:
                continue
            cookie.setdefault(item[0], item[1])
    return cookie


def dict_to_cookie(cookie: dict) -> str:
    if isinstance(cookie, dict):
        cookie_str = ""
        for i, (k, v) in enumerate(cookie.items()):
            append = f"{k}={v}" if i == len(cookie) - 1 else f"{k}={v}; "
            cookie_str += append
        return cookie_str

