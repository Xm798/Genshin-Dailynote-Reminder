import os
import pytz
import gettext
import logging
import datetime
from tzlocal import get_localzone_name
from .config import config

_localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
_translate = gettext.translation(
    'dailynotereminder', _localedir, languages=[config.LANGUAGE], fallback=True
)
_ = _translate.gettext

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

log = logging


def time_in_range(t0: str, t_range: str) -> bool:
    t1, t2 = t_range.split('-')
    time = datetime.datetime.strptime(t0, '%H:%M').time()
    start = datetime.datetime.strptime(t1, '%H:%M').time()
    end = datetime.datetime.strptime(t2, '%H:%M').time()
    result = start <= time or time <= end
    if start <= end:
        result = start <= time <= end
    return result


def tz_diff(tz_server: str, tz_local: str):
    offset_local = (
            datetime.datetime.utcnow()
            .replace(tzinfo=pytz.utc)
            .astimezone(pytz.timezone(tz_local))
            .utcoffset()
            .total_seconds()
            / 60
            / 60
    )
    offset_server = (
            datetime.datetime.utcnow()
            .replace(tzinfo=pytz.utc)
            .astimezone(pytz.timezone(tz_server))
            .utcoffset()
            .total_seconds()
            / 60
            / 60
    )
    diff = offset_local - offset_server
    if abs(diff) > 12.0:
        if diff < 0.0:
            diff += 24.0
        else:
            diff -= 24.0
    return diff


def reset_time_offset(region: str):
    tz_server = {
        'cn_gf01': 'Etc/GMT-8',
        'cn_qd01': 'Etc/GMT-8',
        'os_usa': 'Etc/GMT+5',
        'os_euro': 'Etc/GMT-1',
        'os_asia': 'Etc/GMT-8',
        'os_cht': 'Etc/GMT-8'
    }
    tz_local = get_localzone_name()
    delta = -tz_diff(tz_server[region], tz_local) - 4
    return delta
