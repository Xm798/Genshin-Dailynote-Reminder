from ..config import config
from .dataanalystic import *

def receive_data(base_data,uid) -> list:
    """
    
    Configure the data you want to receive
    """
    result: list = []

    # if (name):
    #     result.append(f'账号：{config.NAME}')

    hidden_uid = str(uid).replace(str(uid)[3:-3], '***', 1)
    result.append(f'UID：{hidden_uid}\n--------------------')

    if config.RESIN_INFO:
        result.append(get_resin_data(base_data))

    # resin_discount_num_limit
    if config.TROUNCE_INFO:
        result.append(get_resin_discount_data(base_data))

    # task_num
    if config.COMMISSION_INFO:
        result.append(get_task_num_data(base_data))

    # home_coin
    result.append(get_home_coin_data(base_data))

    # expedition_num
    if config.EXPEDITION_INFO:
        result.append(get_expedition_data(base_data))

    return result