from . import notifiers
from .utils import *
from .utils import _
from .getinfo.praseinfo import *
from .getinfo.mihoyo import Yuanshen
from .getinfo.hoyolab import Genshin


def send(text: str, status: str, message: str) -> None:
    try:
        notifiers.send2all(text=text, status=status, desp=message)
    except Exception as e:
        print(e)


def check(role, base_data, message):
    alert = False
    status = ''

    # CHECK COMMISSION
    if config.COMMISSION_NOTICE_TIME:
        time_delta = reset_time_offset(role['region'])
        time_config = datetime.datetime.strptime(
            config.COMMISSION_NOTICE_TIME, '%H:%M'
        ) + datetime.timedelta(hours=time_delta)
        time_now = datetime.datetime.now() + datetime.timedelta(hours=time_delta)
        if time_now.time() > time_config.time():
            if _('奖励未领取') in message:
                alert = True
                if base_data.finished_task_num != 4:
                    status = _('你今日的委托还没有完成哦！')
                    log.info(_('🔔今日委托未完成，发送提醒。'))
                else:
                    status = _('你今日的委托奖励还没有领取哦！')
                    log.info(_('🔔今日委托已完成，奖励未领取，发送提醒。'))
            elif _('奖励已领取') in message:
                log.info(_('✅委托检查结束，今日委托已完成，奖励已领取。'))
        else:
            log.info(_('⏩︎未到每日委托检查提醒时间。'))
    else:
        log.info(_('⏩︎未开启每日委托检查，已跳过。'))

    # CHECK RESIN
    if config.RESIN_THRESHOLD:
        if base_data.current_resin >= int(config.RESIN_THRESHOLD):
            alert = True
            status += (
                _('树脂已经溢出啦！') if (base_data.current_resin >= 160) else _('树脂快要溢出啦！')
            )
            log.info(_('🔔树脂已到临界值，当前树脂{}，发送提醒。').format(base_data.current_resin))
        else:
            log.info(_('✅树脂检查结束，当前树脂{}，未到提醒临界值。').format(base_data.current_resin))
    else:
        log.info(_('⏩︎未开启树脂检查，已跳过。'))

    # CHECK HOMECOIN
    if config.HOMECOIN_NOTICE:
        if (
            base_data.current_home_coin
            >= config.HOMECOIN_THRESHOLD * base_data.max_home_coin
        ) and base_data.max_home_coin:
            alert = True
            status = (
                (status + _('洞天宝钱已经溢出啦！'))
                if (base_data.current_home_coin >= base_data.max_home_coin)
                else (status + _('洞天宝钱快要溢出啦！'))
            )
            log.info(
                _('🔔当前洞天宝钱{}，已到临界值{}，发送提醒。').format(
                    base_data.current_home_coin,
                    config.HOMECOIN_THRESHOLD * base_data.max_home_coin,
                )
            )
        else:
            log.info(_('✅洞天宝钱检查结束，未溢出。'))
    else:
        log.info(_('⏩︎未开启洞天宝钱检查，已跳过。'))

    # CHECK EXPEDITION
    if config.EXPEDITION_NOTICE:
        if base_data.finished_expedition_num > 0:
            if config.WAIT_ALL_EXPEDITION and (
                base_data.finished_expedition_num != base_data.current_expedition_num
            ):
                log.info(_('✅探索派遣未全部完成。'))
            else:
                alert = True
                status = status + _('探索派遣已经完成啦！')
                log.info(_('🔔有已完成的探索派遣，发送提醒。'))
        else:
            log.info(_('✅探索派遣检查结束，不存在完成的探索派遣。'))
    else:
        log.info(_('⏩︎未开启探索派遣完成提醒，已跳过。'))

    # CHECK TRANSFORMER
    if config.TRANSFORMER:
        if base_data.transformer:
            if base_data.transformer.get('obtained'):
                if base_data.transformer.get('recovery_time')['reached']:
                    alert = True
                    status = status + _('参量质变仪已就绪！')
                    log.info(_('🔔参量质变仪已就绪，发送提醒。'))
                else:
                    log.info(_('✅参量质变仪未准备好。'))
            else:
                log.info(_('⏩︎未获得参量质变仪。'))
        else:
            log.warning(_('⏩︎接口未返回参量质变仪信息。'))
    else:
        log.info(_('⏩︎未开启参量质变仪就绪提醒，已跳过。'))

    # CHECK BEFORE SLEEP
    overflow = False
    if config.SLEEP_TIME:
        overflow, status = check_before_sleep(base_data, status)

    if config.NICK_NAME:
        nickname = (
            f'{config.NICK_NAME}，'
            if 'zh' in config.LANGUAGE
            else f'{config.NICK_NAME},'
        )
    else:
        nickname = f"{role['nickname']}, "
    # 推送消息
    if alert or overflow:
        send(text=nickname, status=status, message=message)


def check_before_sleep(base_data, status: str):
    overflow = False
    time_nextcheck = (
        datetime.datetime.now() + datetime.timedelta(minutes=config.CHECK_INTERVAL)
    ).strftime('%H:%M')
    if time_in_range(time_nextcheck, config.SLEEP_TIME):
        overflow_time = (
            datetime.datetime.now()
            + datetime.timedelta(seconds=base_data.resin_recovery_time)
        ).strftime('%H:%M')
        if time_in_range(overflow_time, config.SLEEP_TIME):
            overflow = True
            status += _('树脂将会在{}溢出，睡前记得清树脂哦！').format(overflow_time)
            log.info(_('🔔睡眠期间树脂将会溢出，发送提醒。'))
        else:
            log.info(_('✅睡眠期间树脂不会溢出，放心休息。'))
    return overflow, status


def start(cookies: list, server: str) -> None:
    for index, cookie in enumerate(cookies):
        log.info(
            _('🗝️ 当前配置了{}个账号，正在执行第{}个').format(
                os.environ['ACCOUNT_NUM'], os.environ['ACCOUNT_INDEX']
            )
        )
        log.info('-------------------------')
        os.environ['ACCOUNT_INDEX'] = str(int(os.environ['ACCOUNT_INDEX']) + 1)
        client = Yuanshen(cookie, config.RUN_ENV) if server == 'cn' else Genshin(cookie)
        roles_info = client.roles_info
        if isinstance(roles_info, list):
            log.info(
                _('获取到{0}的{1}个角色...').format(
                    (_('国服') if server == 'cn' else _('国际服')), len(roles_info)
                )
            )
            for i, role in enumerate(roles_info):
                log.info(
                    (_('第{}个角色，{} {}')).format(
                        i + 1, role['game_uid'], role['nickname']
                    )
                )
                if role['game_uid'] in str(config.EXCLUDE_UID):
                    log.info(_('跳过该角色'))
                else:
                    dailynote_info, message = client.prase_dailynote_info(role)
                    if dailynote_info:
                        check(role, dailynote_info, message)
                    else:
                        status = (_('获取UID: {} 数据失败！')).format(role['game_uid'])
                        message = _('请查阅运行日志获取详细原因。')
                        send(text='ERROR! ', status=status, message=message)
        else:
            log.error(roles_info)
            status = _('获取米游社角色信息失败！')
            message = roles_info
            send(text='ERROR! ', status=status, message=message)
        log.info(f'-------------------------')
