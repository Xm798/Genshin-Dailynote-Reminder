import os
import re
import json
import datetime
from ..utils import _
from ..config import config
from .model import BaseData


def parse_info(info, role, mode='standard'):
    """
    Configure the data you want to receive
    """
    result: list = []
    server = {
        'cn_gf01': _('天空岛 🌈'),
        'cn_qd01': _('世界树 🌲'),
        'os_usa': _('美服 🦙'),
        'os_euro': _('欧服 🏰'),
        'os_asia': _('亚服 🐯'),
        'os_cht': _('台港澳服 🧋'),
    }
    result.append(f"{role['nickname']} {server[role['region']]}")
    if config.DISPLAY_UID:
        hidden_uid = str(role['game_uid']).replace(
            str(role['game_uid'])[3:-3], '***', 1
        )
        result.append(f'UID：{hidden_uid}')
    result.append('--------------------')

    if mode == 'standard':
        if config.RESIN_INFO:
            result.append(
                get_resin_info(
                    info.current_resin, info.max_resin, info.resin_recovery_time
                )
            )
        # resin_discount_num_limit
        if config.TROUNCE_INFO:
            result.append(get_trounce_info(info))
        # task_num
        if config.COMMISSION_INFO:
            result.append(get_commission_info(info))
        # transformer
        if config.TRANSFORMER_INFO and info.transformer:
            result.append(get_transformer_info(info))
        # home_coin
        if config.HOMECOIN_INFO:
            result.append(get_homecoin_info(info))
        # expedition_num
        if config.EXPEDITION_INFO:
            result.append(get_expedition_info(info))
        return result
    else:
        data_lite = {}
        for i in info:
            data_lite[i['name']] = i['value']
        is_extra_task_reward_received = True if data_lite['每日委托进度'] == '全部完成' else False
        finished_task_num = (
            4
            if data_lite['每日委托进度'] == '全部完成' or data_lite['每日委托进度'] == '尚未领取'
            else int(data_lite['每日委托进度'].split('/')[0])
        )

        data = {
            'current_resin': int(data_lite['原粹树脂'].split('/')[0]),
            'max_resin': int(data_lite['原粹树脂'].split('/')[1]),
            'current_home_coin': int(data_lite['洞天财瓮'].split('/')[0]),
            'max_home_coin': int(data_lite['洞天财瓮'].split('/')[1]),
            'finished_task_num': finished_task_num,
            'is_extra_task_reward_received': is_extra_task_reward_received,
            'resin_recovery_time': (int(data_lite['原粹树脂'].split('/')[1]) - int(data_lite['原粹树脂'].split('/')[0])) * 8 * 60
        }
        info = BaseData.parse_obj(data)
        result.append(get_resin_info(info.current_resin, info.max_resin, None))
        result.append(get_commission_info(info))
        result.append(
            _('当前洞天宝钱/上限：{} / {}\n').format(info.current_home_coin, info.max_home_coin)
        )
        return result, info


def seconds2hours(seconds: int) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def get_resin_info(current_resin, max_resin, resin_recovery_time) -> str:
    resin_data = (_('当前树脂：{} / {}\n')).format(current_resin, max_resin)
    if current_resin < 160:
        if resin_recovery_time:
            next_resin_rec_time = seconds2hours(
                8 * 60 - ((max_resin - current_resin) * 8 * 60 - resin_recovery_time)
            )
            resin_data += (_('下个回复倒计时：{}\n')).format(next_resin_rec_time)
            overflow_time = datetime.datetime.now() + datetime.timedelta(
                seconds=resin_recovery_time
            )
        else:
            overflow_time = datetime.datetime.now() + datetime.timedelta(
                seconds=(max_resin - current_resin) * 8 * 60
            )
        day = _('今天') if datetime.datetime.now().day == overflow_time.day else _('明天')
        resin_data += _('预估回复时间：{} {}').format(day, overflow_time.strftime('%X'))
    return resin_data


def get_trounce_info(info: BaseData) -> str:
    return _('周本树脂减半：{} / {}').format(
        info.remain_resin_discount_num, info.resin_discount_num_limit
    )


def get_commission_info(info) -> str:
    task_num: str = f"{info.finished_task_num} / {info.total_task_num}"
    if info.is_extra_task_reward_received:
        status = _('奖励已领取')
    elif info.finished_task_num == info.total_task_num:
        status = _('奖励未领取')
    else:
        status = _('委托未完成')
    return _('今日委托任务：{}   {}\n--------------------').format(task_num, status)


def get_homecoin_info(info) -> str:
    week_day_dict = {
        0: _('周一'),
        1: _('周二'),
        2: _('周三'),
        3: _('周四'),
        4: _('周五'),
        5: _('周六'),
        6: _('周日'),
    }
    coin_data = _('当前洞天宝钱/上限：{} / {}\n').format(
        info.current_home_coin, info.max_home_coin
    )
    if info.home_coin_recovery_time:
        coin_overflow_time = datetime.datetime.now() + datetime.timedelta(
            seconds=info.home_coin_recovery_time
        )
        coin_data += _('洞天宝钱全部恢复时间：{} {}\n').format(
            week_day_dict[coin_overflow_time.weekday()],
            coin_overflow_time.strftime('%X'),
        )
    coin_data += '--------------------'
    return coin_data


def get_expedition_info(info: BaseData) -> str:
    project_path = os.path.dirname(os.path.dirname(__file__))
    config_file = os.path.join(
        project_path, '', f'./locale/{config.LANGUAGE}/avatar.json'
    )
    with open(config_file, 'r', encoding='utf-8') as f:
        avatar_json = json.load(f)

    expedition_info: list[str] = []
    finished = 0
    for expedition in info.expeditions:
        avatar = re.search(
            r'(?<=(UI_AvatarIcon_Side_)).*(?=.png)', expedition['avatar_side_icon']
        ).group()
        try:
            avatar_name: str = avatar_json[avatar]
        except KeyError:
            avatar_name: str = avatar

        if expedition['status'] == 'Finished':
            expedition_info.append(_('  · {}：已完成').format(avatar_name))
            finished += 1
        else:
            finish_time = datetime.datetime.now() + datetime.timedelta(
                seconds=int(expedition['remained_time'])
            )
            day = _('今天') if datetime.datetime.now().day == finish_time.day else _('明天')
            expedition_info.append(
                (_('  · {} 完成时间：{}{}')).format(
                    avatar_name, day, finish_time.strftime('%X')
                )
            )

    expedition_num: str = (
        f'{info.current_expedition_num}/{finished}/{info.max_expedition_num}'
    )
    info.finished_expedition_num = finished
    expedition_data: str = '\n'.join(expedition_info)
    return (_('当前探索派遣总数/完成/上限：{}\n{}')).format(expedition_num, expedition_data)


def get_transformer_info(info: BaseData) -> str:
    if info.transformer.get('obtained'):
        if info.transformer.get('recovery_time')['reached']:
            return _('参量质变仪：已就绪')
        else:
            return (_('参量质变仪： {} 天 {} 小时后可用')).format(
                info.transformer.get('recovery_time')['Day'],
                info.transformer.get('recovery_time')['Hour'],
            )
    else:
        return _('参量质变仪： 未获得')
