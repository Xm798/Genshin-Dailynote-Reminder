import schedule
from time import sleep
from .utils import *
from .utils import _
from .check import start
from .config import config
from .__banner__ import banner


def run_once() -> None:
    if time_in_range(datetime.datetime.now().strftime('%H:%M'), config.SLEEP_TIME):
        log.info(_('😴休眠中……'))
        return
    os.environ['ACCOUNT_INDEX'] = '1'
    os.environ['ACCOUNT_NUM'] = str(len(config.COOKIE + config.COOKIE_HOYOLAB))
    if len(config.COOKIE):
        start(config.COOKIE, 'cn')
    if len(config.COOKIE_HOYOLAB):
        start(config.COOKIE_HOYOLAB, 'os')
    log.info(_('本轮运行结束，等待下次检查...'))


def run() -> None:
    log.info(banner)
    run_once()
    schedule.every(config.CHECK_INTERVAL).minutes.do(run_once)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    run()
