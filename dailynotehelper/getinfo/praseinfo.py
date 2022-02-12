from ..config import config
from .model import BaseData
import json
import datetime
import os


def prase_info(base_data, role) -> list:
    """
    Configure the data you want to receive
    """
    result: list = []
    server = {'cn_gf01': '天空岛 🌈', 'cn_qd01': '世界树 🌲',
              'os_usa': '美服 🦙', 'os_euro': '欧服 🏰', 'os_asia': '亚服 🐯'}
    result.append(f"{role['nickname']} {server[role['region']]}")
    if config.DISPLAY_UID:
        hidden_uid = str(role['game_uid']).replace(
            str(role['game_uid'])[3:-3], '***', 1)
        result.append(f'UID：{hidden_uid}')
    result.append('--------------------')

    if config.RESIN_INFO:
        result.append(get_resin_info(base_data))

    # resin_discount_num_limit
    if config.TROUNCE_INFO:
        result.append(get_trounce_info(base_data))

    # task_num
    if config.COMMISSION_INFO:
        result.append(get_commission_info(base_data))

    # home_coin
    result.append(get_homecoin_info(base_data))

    # expedition_num
    if config.EXPEDITION_INFO:
        result.append(get_expedition_info(base_data))

    return result


def seconds2hours(seconds: int) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def get_resin_info(base_data: BaseData) -> str:
    resin_data = f"当前树脂：{base_data.current_resin} / {base_data.max_resin}\n"
    if(base_data.current_resin < 160):
        next_resin_rec_time = seconds2hours(
            8 * 60 - ((base_data.max_resin - base_data.current_resin) * 8 * 60 - base_data.resin_recovery_time))
        resin_data += f"下个回复倒计时：{next_resin_rec_time}\n"
        overflow_time = datetime.datetime.now(
        ) + datetime.timedelta(seconds=base_data.resin_recovery_time)
        day = '今天' if datetime.datetime.now().day == overflow_time.day else '明天'
        resin_data += f"全部回复时间：{day} {overflow_time.strftime('%X')}"
    return resin_data


def get_trounce_info(base_data: BaseData) -> str:
    return f"周本树脂减半：{base_data.remain_resin_discount_num} / {base_data.resin_discount_num_limit}"


def get_commission_info(base_data: BaseData) -> str:
    task_num: str = f"{base_data.finished_task_num} / {base_data.total_task_num}"
    return f"今日委托任务：{task_num}   奖励{'已' if base_data.is_extra_task_reward_received else '未'}领取\n--------------------"


def get_homecoin_info(base_data: BaseData) -> str:
    week_day_dict = {0: '周一', 1: '周二', 2: '周三',
                     3: '周四', 4: '周五', 5: '周六', 6: '周日', }
    coin_data = f"当前洞天宝钱/上限：{base_data.current_home_coin} / {base_data.max_home_coin}\n"
    if base_data.home_coin_recovery_time:
        coin_overflow_time = datetime.datetime.now(
        ) + datetime.timedelta(seconds=base_data.home_coin_recovery_time)
        coin_data += f"洞天宝钱全部恢复时间：{week_day_dict[coin_overflow_time.weekday()]} {coin_overflow_time.strftime('%X')}\n"
    coin_data += '--------------------'
    return coin_data


def get_expedition_info(base_data: BaseData) -> str:
    project_path = os.path.dirname(__file__)
    config_file = os.path.join(project_path, '', './model/avatar_name.json')
    with open(config_file, 'r', encoding='utf-8') as f:
        avatar_json = json.load(f)

    expedition_info: list[str] = []
    finished = 0
    for expedition in base_data.expeditions:
        avatar: str = expedition['avatar_side_icon'][89:-4]
        try:
            avatar_name: str = avatar_json[avatar]
        except KeyError:
            avatar_name: str = avatar

        if(expedition['status'] == 'Finished'):
            expedition_info.append(f"  · {avatar_name} 已完成")
            finished += 1
        else:
            remained_timed: str = seconds2hours(expedition['remained_time'])
            expedition_info.append(
                f"  · {avatar_name} ，剩余时间{remained_timed}")

    expedition_num: str = f"{base_data.current_expedition_num}/{finished}/{base_data.max_expedition_num}"
    expedition_data: str = "\n".join(expedition_info)
    return f"当前探索派遣总数/完成/上限：{expedition_num}\n{expedition_data}"
