import random
import time
import requests
from ..utils import log
import urllib3
from http.cookies import SimpleCookie


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
    urllib3.disable_warnings()
    is_retry = True
    count = 0
    max_retries = 3
    sleep_seconds = 5
    while is_retry and count <= max_retries:
        try:
            s = requests.Session()
            response = s.request(verify=False, *args, **kwargs)
            # response = s.request(*args, **kwargs)
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


def cookie_to_dict(rawdata: str) -> dict:
    cookie = SimpleCookie(rawdata)
    return {k: v.value for k, v in cookie.items()}


def dict_to_cookie(cookie: dict) -> str:
    if isinstance(cookie, dict):
        cookie_str = ""
        for i, (k, v) in enumerate(cookie.items()):
            append = f"{k}={v}" if i == len(cookie) - 1 else f"{k}={v}; "
            cookie_str += append
        return cookie_str


def sample_string(s, k):
    return ''.join(random.sample(s, k))
