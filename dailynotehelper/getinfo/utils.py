from email import header
import hashlib
import random
import time
import requests
import uuid
import json
from ..utils import log
from urllib.parse import urlencode


def get_ds(params: dict, body: str) -> str:
    t = str(int(time.time()))
    r = str(random.randint(100000, 200000))
    b = json.dumps(body) if body else ''
    q = urlencode(params) if params else ''
    salt = 'xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs'
    text = f'salt={salt}&t={t}&r={r}&b={b}&q={q}'
    md5 = hashlib.md5()
    md5.update(text.encode())
    c = md5.hexdigest()
    return f'{t},{r},{c}'


def get_headers(params: dict = None, body: dict = None, ds: bool = False) -> dict:
    version: str = '2.11.1'
    ua = f'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) miHoYoBBS/{version}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'https://webstatic.mihoyo.com',
        'User-Agent': ua,
    }
    if ds:
        ds = get_ds(params, body)
        headers.update({
            'DS': ds,
            'x-rpc-client_type': '5',
            'x-rpc-app_version': version,
            'x-rpc-device_id': str(uuid.uuid3(uuid.NAMESPACE_URL, ua)).replace('-', '').upper(),
        })
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
                f'Trying to reconnect in {sleep_seconds} seconds ({count}/{max_retries})...')
            time.sleep(sleep_seconds)
        else:
            return response

    def __str__(self) -> str:
        return f"{self.retcode}: {self.message}"


def cookie_to_dict(cookie) -> dict:
    if cookie and '=' in cookie:
        cookie = dict([line.strip().split('=', 1)
                      for line in cookie.split(';')])
    return cookie
