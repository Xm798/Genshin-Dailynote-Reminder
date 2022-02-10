import schedule
import datetime
from .config import config
from .getinfo.praseinfo import *
from .getinfo.client import Yuanshen
from . import notifiers
from time import sleep
from .utils import log

__version__ = 'v2.0.0'
__banner__ = f'''
-------------------------------------------------------------
|                Genshin Dailynote Helper                   |
-------------------------------------------------------------
| Current Version: {__version__}                                   |
| Last Update: Feb 09, 2022                                 |
| Github: https://github.com/Xm798/Genshin-Dailynote-Helper |
-------------------------------------------------------------
'''

def send(text:str,status:str,message:str) -> None:
    try:
        notifiers.send2all(text=text,status=status, desp=message)
    except Exception as e:
        print(e)

def time_in_sleep(t0: str) -> bool:
    t1, t2 = config.SLEEP_TIME.split('-')
    time = datetime.datetime.strptime(t0, '%H:%M').time()
    start = datetime.datetime.strptime(t1, '%H:%M').time()
    end = datetime.datetime.strptime(t2, '%H:%M').time()
    result = start <= time or time <= end
    if start <= end:
        result = start <= time <= end
    return result

def check(base_data,message):
    alert = False
    status = ""

    # 检查委托
    if (config.COMMISSION_NOTICE_TIME):
        alert_time = datetime.datetime.strptime(config.COMMISSION_NOTICE_TIME, "%H:%M") + datetime.timedelta(hours=-4)
        now = datetime.datetime.now() + datetime.timedelta(hours=-4)
        if now.time() > alert_time.time():
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

    # 检查原粹树脂
    if(config.RESIN_THRESHOLD):
        if(base_data.current_resin >= int(config.RESIN_THRESHOLD)):
            status += ("树脂已经溢出啦！") if(base_data.current_resin >= 160) else ("树脂快要溢出啦！")
            alert = True
            log.info(f'🔔树脂已到临界值，当前树脂{base_data.current_resin}，发送提醒。')
        else:
            log.info(f'✅树脂检查结束，当前树脂{base_data.current_resin}，未到提醒临界值。')
    else:
        log.info('⏩︎未开启树脂检查，已跳过。')

    # 检查洞天宝钱
    if(config.HOMECOIN_NOTICE):
        if(base_data.current_home_coin >= base_data.max_home_coin):
            status= status + "洞天宝钱已经溢出啦！"
            alert = True
            log.info('🔔洞天宝钱已经溢出，发送提醒。')
        else:
            log.info('✅洞天宝钱检查结束，未溢出。')
    else:
        log.info('⏩︎未开启洞天宝钱检查，已跳过。')

    # 检查探索派遣
    if(config.EXPEDITION_NOTICE):
        if("已完成" in message):
            status= status + "探索派遣已经完成啦！"
            alert = True
            log.info('🔔有已完成的探索派遣，发送提醒。')
        else:
            log.info('✅探索派遣检查结束，不存在完成的探索派遣。')
    else:
        log.info('⏩︎未开启探索派遣完成提醒，已跳过。')

    # 睡前检查
    if config.SLEEP_TIME:
        overflow,status = check_before_sleep(base_data,status)

    # 推送消息
    if alert or overflow:
        send(text="亲爱的旅行者，",status=status, message=message)

def check_before_sleep(base_data,status: str):
    # 检查睡眠期间树脂是否溢出
    overflow = False
    time_nextcheck = (datetime.datetime.now() + datetime.timedelta(minutes=config.CHECK_INTERVAL)).strftime('%H:%S')
    if time_in_sleep(time_nextcheck):
        overflow_time = (datetime.datetime.now() + datetime.timedelta(seconds=base_data.resin_recovery_time)).strftime('%H:%S')
        if time_in_sleep(overflow_time):
            overflow = True
            status += f"树脂将会在{overflow_time}溢出，睡前记得清树脂哦！"
            log.info(f'🔔睡眠期间树脂将会溢出，发送提醒。')
        else:
            log.info(f'✅睡眠期间树脂不会溢出，放心休息。')
    return overflow,status

def run_once() -> None:
    if time_in_sleep(datetime.datetime.now().strftime('%H:%M')):
        log.info('😴休眠中……')
        return
    for index,cookie in enumerate(config.COOKIE):
        log.info(f'-------------------------')
        log.info(f'🗝️  当前配置了{len(config.COOKIE)}个账号，正在执行第{index+1}个')
        client = Yuanshen(cookie, config.RUN_ENV)
        roles_info = client.roles_info
        log.info(f'获取到{len(roles_info)}个角色...')
        for index,role in enumerate(roles_info):
            log.info(f"第{index+1}个角色，{role['game_uid']} {role['nickname']}")
            daily_info,message = client.prase_dailynote_info(role)
        check(daily_info,message)
    print('\n')
    log.info('本轮运行结束，等待下次检查...')

def run() -> None:
    log.info(__banner__)
    run_once()
    schedule.every(config.CHECK_INTERVAL).minutes.do(run_once)
    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == '__main__':
    run()