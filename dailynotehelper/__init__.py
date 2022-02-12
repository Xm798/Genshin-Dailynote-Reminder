import schedule
import datetime
import os
from time import sleep
from . import notifiers
from . import __banner__
from .utils import *
from .config import config
from .getinfo.praseinfo import *
from .getinfo.mihoyo import Yuanshen
from .getinfo.hoyolab import Genshin


def send(text: str, status: str, message: str) -> None:
    try:
        notifiers.send2all(text=text, status=status, desp=message)
    except Exception as e:
        print(e)


def check(region, base_data, message):
    alert = False
    status = ""
    
    # CHECK COMMISSION
    if (config.COMMISSION_NOTICE_TIME):
        time_delta = reset_time_offset(region)
        time_config = datetime.datetime.strptime(
            config.COMMISSION_NOTICE_TIME, "%H:%M") + datetime.timedelta(hours=time_delta)
        time_now = datetime.datetime.now() + datetime.timedelta(hours=time_delta)
        if time_now.time() > time_config.time():
            if ("奖励未领取" in message):
                alert = True
                if (base_data.finished_task_num != 4):
                    status = "你今日的委托还没有完成哦！"
                    log.info('🔔今日委托未完成，发送提醒。')
                else:
                    status = "你今日的委托奖励还没有领取哦！"
                    log.info('🔔今日委托已完成，奖励未领取，发送提醒。')
            elif ("奖励已领取" in message):
                log.info('✅委托检查结束，今日委托已完成，奖励已领取。')
        else:
            log.info('⏩︎未到每日委托检查提醒时间。')
    else:
        log.info('⏩︎未开启每日委托检查，已跳过。')

    # CHECK RESIN
    if(config.RESIN_THRESHOLD):
        if(base_data.current_resin >= int(config.RESIN_THRESHOLD)):

            status += ("树脂已经溢出啦！") if(base_data.current_resin >=160) else ("树脂快要溢出啦！")
            log.info(f'🔔树脂已到临界值，当前树脂{base_data.current_resin}，发送提醒。')
        else:
            log.info(f'✅树脂检查结束，当前树脂{base_data.current_resin}，未到提醒临界值。')
    else:
        log.info('⏩︎未开启树脂检查，已跳过。')

    # CHECK HOMECOIN
    if(config.HOMECOIN_NOTICE):
        if(base_data.current_home_coin >= base_data.max_home_coin):
            alert = True
            status = status + "洞天宝钱已经溢出啦！"
            log.info('🔔洞天宝钱已经溢出，发送提醒。')
        else:
            log.info('✅洞天宝钱检查结束，未溢出。')
    else:
        log.info('⏩︎未开启洞天宝钱检查，已跳过。')

    # CHECK EXPEDITION
    if(config.EXPEDITION_NOTICE):
        if("已完成" in message):
            alert = True
            status = status + "探索派遣已经完成啦！"
            log.info('🔔有已完成的探索派遣，发送提醒。')
        else:
            log.info('✅探索派遣检查结束，不存在完成的探索派遣。')
    else:
        log.info('⏩︎未开启探索派遣完成提醒，已跳过。')

    # CHECK BEFORE SLEEP
    if config.SLEEP_TIME:
        overflow, status = check_before_sleep(base_data, status)

    # 推送消息
    if alert or overflow:
        send(text="亲爱的旅行者，", status=status, message=message)


def check_before_sleep(base_data, status: str):
    overflow = False
    time_nextcheck = (datetime.datetime.now(
    ) + datetime.timedelta(minutes=config.CHECK_INTERVAL)).strftime('%H:%S')
    if time_in_range(time_nextcheck, config.SLEEP_TIME):
        overflow_time = (datetime.datetime.now(
        ) + datetime.timedelta(seconds=base_data.resin_recovery_time)).strftime('%H:%S')
        if time_in_range(overflow_time, config.SLEEP_TIME):
            overflow = True
            status += f"树脂将会在{overflow_time}溢出，睡前记得清树脂哦！"
            log.info(f'🔔睡眠期间树脂将会溢出，发送提醒。')
        else:
            log.info(f'✅睡眠期间树脂不会溢出，放心休息。')
    return overflow, status


def start(cookies: list, server: str) -> None:
    for index, cookie in enumerate(cookies):
        log.info(
            f"🗝️  当前配置了{os.environ['ACCOUNT_NUM']}个账号，正在执行第{os.environ['ACCOUNT_INDEX']}个")
        log.info(f'-------------------------')
        os.environ['ACCOUNT_INDEX'] = str(int(os.environ['ACCOUNT_INDEX']) + 1)
        client = Yuanshen(
            cookie, config.RUN_ENV) if server == 'cn' else Genshin(cookie)
        roles_info = client.roles_info
        log.info(
            f"获取到{'国服' if server == 'cn' else '国际服'}的{len(roles_info)}个角色...")
        for index, role in enumerate(roles_info):
            log.info(f"第{index+1}个角色，{role['game_uid']} {role['nickname']}")
            if role['game_uid'] in str(config.EXCLUDE_UID):
                log.info(f'跳过该角色')
            else:
                daily_info, message = client.prase_dailynote_info(role)
                check(role['region'], daily_info, message)
            log.info(f'-------------------------')


def run_once() -> None:
    if time_in_range(datetime.datetime.now().strftime('%H:%M'), config.SLEEP_TIME):
        log.info('😴休眠中……')
        return
    os.environ['ACCOUNT_INDEX'] = '1'
    os.environ['ACCOUNT_NUM'] = str(len(config.COOKIE + config.COOKIE_HOYOLAB))
    if len(config.COOKIE):
        start(config.COOKIE, 'cn')
    if len(config.COOKIE_HOYOLAB):
        start(config.COOKIE_HOYOLAB, 'os')
    log.info(f'本轮运行结束，等待下次检查...')


def run() -> None:
    log.info(__banner__)
    run_once()
    schedule.every(config.CHECK_INTERVAL).minutes.do(run_once)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    run()
