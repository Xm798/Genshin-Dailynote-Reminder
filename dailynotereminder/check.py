import datetime
import os

from .config import config
from .getinfo.client_cn import ClientCN
from .getinfo.client_cn_widget import ClientCNWidget
from .getinfo.client_os import ClientOS
from .locale import _
from .notifiers import send
from .utils import log, reset_time_offset, time_in_range


class Check:
    def __init__(self):
        self.alert = False
        self.status = ''
        self.data = None
        self.message = ''

    def check_commision(self, role, finished_task_num):
        time_delta = reset_time_offset(role['region'])
        time_config = datetime.datetime.strptime(
            config.COMMISSION_NOTICE_TIME, '%H:%M'
        ) + datetime.timedelta(hours=time_delta)
        time_now = datetime.datetime.now() + datetime.timedelta(hours=time_delta)
        if time_now.time() > time_config.time():
            if not _('奖励已领取') in self.message:
                self.alert = True
                if finished_task_num != 4:
                    self.status += _('你今日的委托还没有完成哦！')
                    log.info(_('🔔今日委托未完成，发送提醒。'))
                else:
                    self.status += _('你今日的委托奖励还没有领取哦！')
                    log.info(_('🔔今日委托已完成，奖励未领取，发送提醒。'))
            else:
                log.info(_('✅委托检查结束，今日委托已完成，奖励已领取。'))
        else:
            log.info(_('⏩︎未到每日委托检查提醒时间。'))

    def check_resin(self, current_resin):
        if current_resin >= int(config.RESIN_THRESHOLD):
            self.alert = True
            self.status += _('树脂已经溢出啦！') if (current_resin >= 160) else _('树脂快要溢出啦！')
            log.info(_('🔔树脂已到临界值，当前树脂{}，发送提醒。').format(current_resin))
        else:
            log.info(_('✅树脂检查结束，当前树脂{}，未到提醒临界值。').format(current_resin))

    def check_home_coin(self):
        if (
            self.data.current_home_coin
            >= config.HOMECOIN_THRESHOLD * self.data.max_home_coin
        ) and self.data.max_home_coin:
            self.alert = True
            self.status = (
                (self.status + _('洞天宝钱已经溢出啦！'))
                if (self.data.current_home_coin >= self.data.max_home_coin)
                else (self.status + _('洞天宝钱快要溢出啦！'))
            )
            log.info(
                _('🔔当前洞天宝钱{}，已到临界值{}，发送提醒。').format(
                    self.data.current_home_coin,
                    config.HOMECOIN_THRESHOLD * self.data.max_home_coin,
                )
            )
        else:
            log.info(_('✅洞天宝钱检查结束，未溢出。'))

    def check_expedition(self):
        if self.data.finished_expedition_num > 0:
            if config.WAIT_ALL_EXPEDITION and (
                self.data.finished_expedition_num != self.data.current_expedition_num
            ):
                log.info(_('✅探索派遣未全部完成。'))
            else:
                self.alert = True
                self.status += _('探索派遣已经完成啦！')
                log.info(_('🔔有已完成的探索派遣，发送提醒。'))
        else:
            log.info(_('✅探索派遣检查结束，不存在完成的探索派遣。'))

    def check(self, role, lite=False, push=False):
        if config.COMMISSION_NOTICE_TIME:
            self.check_commision(role, self.data.finished_task_num)
        else:
            log.info(_('⏩︎未开启每日委托检查，已跳过。'))

        if config.RESIN_THRESHOLD:
            self.check_resin(self.data.current_resin)
        else:
            log.info(_('⏩︎未开启树脂检查，已跳过。'))

        if config.HOMECOIN_NOTICE:
            self.check_home_coin()
        else:
            log.info(_('⏩︎未开启洞天宝钱检查，已跳过。'))

        if config.EXPEDITION_NOTICE and not lite:
            self.check_expedition()
        else:
            log.info(_('⏩︎未开启探索派遣完成提醒，已跳过。'))

        if config.TRANSFORMER and not lite:
            if self.data.transformer:
                if self.data.transformer.get('obtained'):
                    if self.data.transformer.get('recovery_time')['reached']:
                        self.alert = True
                        self.status += _('参量质变仪已就绪！')
                        log.info(_('🔔参量质变仪已就绪，发送提醒。'))
                    else:
                        log.info(_('✅参量质变仪未准备好。'))
                else:
                    log.info(_('⏩︎未获得参量质变仪。'))
            else:
                log.warning(_('⏩︎接口未返回参量质变仪信息。'))
        else:
            log.info(_('⏩︎未开启参量质变仪就绪提醒，已跳过。'))

        overflow = False
        if config.SLEEP_TIME:
            overflow = self.check_before_sleep(self.data.resin_recovery_time)

        if config.NICK_NAME:
            nickname = (
                f'{config.NICK_NAME}，'
                if 'zh' in config.LANGUAGE
                else f'{config.NICK_NAME},'
            )
        else:
            nickname = f"{role['nickname']}, "
        # 推送消息
        if self.alert or overflow or push:
            send(text=nickname, status=self.status, message=self.message)

    def check_before_sleep(self, recovery_seconds: int) -> bool:
        time_nextcheck = (
            datetime.datetime.now() + datetime.timedelta(minutes=config.CHECK_INTERVAL)
        ).strftime('%H:%M')
        if time_in_range(time_nextcheck, config.SLEEP_TIME):
            overflow_time = (
                datetime.datetime.now() + datetime.timedelta(seconds=recovery_seconds)
            ).strftime('%H:%M')
            if time_in_range(overflow_time, config.SLEEP_TIME):
                self.status += _('树脂将会在{}溢出，睡前记得清树脂哦！').format(overflow_time)
                log.info(_('🔔睡眠期间树脂将会溢出，发送提醒。'))
                return True
            else:
                log.info(_('✅睡眠期间树脂不会溢出，放心休息。'))
                return False

    def lite_mode(self, cookie, role, fallback=False):
        client = ClientCNWidget(cookie)
        info = client.get_daily_note_info(role)
        log.info(_('⚠️处于轻量模式，仅检查树脂、委托、洞天宝钱。'))
        if info['retcode'] == 0:
            self.data = info['data']
            self.message = (
                info['message']
                if not fallback
                else info['message'] + '\n⚠️账号异常，本次自动回落至轻量模式'
            )
            self.check(role, lite=True, push=info['ck_updated'])
        else:
            log.error(info['message'])
            send(
                text='❌ERROR! ',
                status=(_('获取UID: {} 数据失败！')).format(role['game_uid']),
                message=info['message']
                if not fallback
                else '⚠️账号异常，本次尝试自动回落至轻量模式失败！\n\n' + info['message'],
            )

    def standard_mode(self, client, role, fallback):
        info = client.get_daily_note_info(role)
        if info['retcode'] == 0:
            self.data = info['data']
            self.message = info['message']
            self.check(role)
        else:
            if info['retcode'] == 1034 and fallback:
                log.warning(_('⚠️UID: {} 账号异常，自动回落到轻量模式。').format(role['game_uid']))
                self.lite_mode(client.cookie, role, fallback=True)
            else:
                log.error(info['message'])
                send(
                    text='❌ERROR! ',
                    status=(_('获取UID: {} 数据失败！')).format(role['game_uid']),
                    message=info['message'],
                )


def start(cookies: list, server: str) -> None:
    for index, cookie in enumerate(cookies):
        log.info(
            _('🗝️ 当前配置了{}个账号，正在执行第{}个').format(
                os.environ['ACCOUNT_NUM'], os.environ['ACCOUNT_INDEX']
            )
        )
        log.info('-------------------------')
        os.environ['ACCOUNT_INDEX'] = str(int(os.environ['ACCOUNT_INDEX']) + 1)
        client = ClientCN(cookie) if server == 'cn' else ClientOS(cookie)
        roles_info = client.get_roles_info()
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
                    check = Check()
                    if config.LITE_MODE == 'auto':
                        check.standard_mode(client, role, True)
                    elif config.LITE_MODE and server == 'cn':
                        check.lite_mode(cookie, role)
                    else:
                        check.standard_mode(client, role, False)
        else:
            status = _('获取米游社角色信息失败！')
            message = str(roles_info)
            send(text='❌ERROR! ', status=status, message=message)
        log.info(f'-------------------------')
