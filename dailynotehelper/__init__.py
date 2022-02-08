from .getinfo import MysAPI, APIError
from .config import config
from . import notifiers
from .getinfo.dataanalystic import *
import time
import datetime

from .notifiers.utils import log
from .getinfo.receivedata import receive_data


def send(text:str,status:str,message:str) -> None:
    try:
        notifiers.send2all(text=text,status=status, desp=message)
    except Exception as e:
        print(e)

def get_data(uid, cookie):
    api = 'new' if config.RUN_ENV == "local" else 'old'
    try:
        base_data: BaseData = MysAPI(uid, cookie, api).get_dailyNote()
        result: str = receive_data(base_data,uid)
        message = "\n".join(result)
    except APIError:
        send(text='',status="error", message="发生错误，请检查配置文件中运行环境是否配置正确、cookie与id是否对应以及是否已开启米游社实时便笺功能。")
        exit()
    return base_data,message

def time_in_sleep(time, interval: str):
    t1, t2 = interval.split('-')
    sleep_start = datetime.datetime.strptime(t1, "%H:%M")
    sleep_end = datetime.datetime.strptime(t2, "%H:%M")
    today = datetime.date.today()
    if sleep_start.time() < sleep_end.time():
        # 同一天
        sleep_start = datetime.datetime.combine(today, sleep_start.time())
        sleep_end = datetime.datetime.combine(today, sleep_end.time())
    else:
        # 不同一天
        if datetime.datetime.now().time() > sleep_end.time():
            #还在开始时间相同一天
            tomorrow = today + datetime.timedelta(days=1)
            sleep_start = datetime.datetime.combine(today, sleep_start.time())
            sleep_end = datetime.datetime.combine(tomorrow, sleep_end.time())
        else:
            #已经进入了第二天
            yesterday = today - datetime.timedelta(days=1)
            sleep_start = datetime.datetime.combine(yesterday, sleep_start.time())
            sleep_end = datetime.datetime.combine(today, sleep_end.time())
    result = sleep_start <= time <= sleep_end
    return result

def check(base_data,message):
    alert = alert_task = alert_resin = alert_expedition = alert_homecoin = False
    status = ""

    # 检查委托
    if (config.COMMISSION_NOTICE_TIME):
        alert_time = datetime.datetime.strptime(config.COMMISSION_NOTICE_TIME, "%H:%M") + datetime.timedelta(hours=-4)
        now = datetime.datetime.now() + datetime.timedelta(hours=-4)
        if now.time() > alert_time.time():
            if ("奖励未领取" in message):
                if (base_data.finished_task_num != 4):
                    status = "你今日的委托还没有完成哦！"
                    alert_task = True
                    log.info('今日委托未完成，发送提醒。')
                else:
                    alert_task = True
                    status = "你今日的委托奖励还没有领取哦！"
                    log.info('今日委托已完成，奖励未领取，发送提醒。')
            elif ("奖励已领取" in message):
                alert_task = False
                log.info('委托检查结束，今日委托已完成，奖励已领取。')
        else:
            alert_task = False
            log.info('未到每日委托检查提醒时间。')
    else:
        log.info('未配置每日委托检查，已跳过。')

    # 检查原粹树脂
    if(config.RESIN_THRESHOLD):
        if(base_data.current_resin >= int(config.RESIN_THRESHOLD)):
            if(base_data.current_resin >= 160):
                status= status + "树脂已经溢出啦！"
            else:
                status= status + "树脂快要溢出啦！"
            alert_resin = True
            log.info(f'树脂已到临界值，当前树脂{base_data.current_resin}，发送提醒。')
        else:
            alert_resin = False
            log.info(f'树脂检查结束，当前树脂{base_data.current_resin}，未到提醒临界值。')
    else:
        log.info('未开启树脂检查，已跳过。')

    # 检查洞天宝钱
    if(config.HOMECOIN_NOTICE):
        if(base_data.current_home_coin >= base_data.max_home_coin):
            status= status + "洞天宝钱已经溢出啦！"
            alert_homecoin = True
            log.info('洞天宝钱已经溢出，发送提醒。')
        else:
            alert_homecoin = False
            log.info('洞天宝钱检查结束，未溢出。')
    else:
        log.info('未开启洞天宝钱检查，已跳过。')

    # 检查探索派遣
    if(config.EXPEDITION_NOTICE):
        if("已完成" in message):
            status= status + "探索派遣已经完成啦！"
            alert_expedition = True
            log.info('有已完成的探索派遣，发送提醒。')
        else:
            alert_expedition = False
            log.info('探索派遣检查结束，不存在完成的探索派遣。')
    else:
        log.info('未开启探索派遣完成提醒，已跳过。')

    alert = alert_resin or alert_task or alert_expedition or alert_homecoin
    # 睡前检查
    if config.SLEEP_TIME:
        overflow,status = check_before_sleep(config.CHECK_INTERVAL,base_data,status)
    # 推送消息
    if alert or overflow:
        send(text="亲爱的旅行者，",status=status, message=message)
    # 开始休眠
    log.info(f'😴 本轮运行结束，休眠{config.CHECK_INTERVAL}秒')

def check_before_sleep(check_interval,base_data,status):
    overflow = False
    # 本轮休眠结束时间落入程序休眠区间内
    next_check_time = datetime.datetime.now() + datetime.timedelta(seconds=check_interval)
    if time_in_sleep(next_check_time,config.SLEEP_TIME):
        # 检查睡眠期间树脂是否溢出
        log.info("执行睡前树脂溢出检查……")
        overflow_time = datetime.datetime.now() + datetime.timedelta(seconds=base_data.resin_recovery_time)
        if time_in_sleep(overflow_time, config.SLEEP_TIME):
            overflow = True
            status += f"树脂将会在{overflow_time.strftime('%X')}溢出，睡前记得清树脂哦！"
            log.info(f'睡眠期间树脂将会溢出，发送提醒。')
        else:
            log.info(f'睡眠期间树脂不会溢出，放心休息。')
        # 开始休眠
    return overflow,status

def run_once() -> None:
    for uid,cookie in zip(config.UID,config.COOKIE):
        base_data,message=get_data(uid, cookie)
        check(base_data,message)

def run() -> None:
    for uid,cookie in zip(config.UID,config.COOKIE):
        base_data,message=get_data(uid, cookie)
        check(base_data,message)
    