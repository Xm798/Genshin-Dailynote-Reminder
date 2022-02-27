import pydantic
from typing import List
from typing_extensions import Literal


class BaseData(pydantic.BaseModel):
    """
    current_resin=35 当前树脂
    max_resin=160 树脂上限
    resin_recovery_time=59900 树脂恢复时间
    remain_resin_discount_num=3 本周剩余树脂减半次数
    resin_discount_num_limit=3 本周树脂减半次数上限

    current_expedition_num=5 当前派遣数量
    max_expedition_num=5 最大派遣数量
    finished_task_num=0 完成的委托数量
    total_task_num=4 全部委托数量
    is_extra_task_reward_received=False 每日委托奖励是否领取
    current_home_coin: 当前洞天宝钱数量
    max_home_coin: 洞天宝钱存储上限
    home_coin_recovery_time: 洞天宝钱溢出时间

    """
    current_resin: int = 0
    max_resin: int = 0
    resin_recovery_time: int = 0
    remain_resin_discount_num: Literal[0, 1, 2, 3] = 0
    resin_discount_num_limit: int = 3
    current_expedition_num: Literal[0, 1, 2, 3, 4, 5] = 0
    max_expedition_num: Literal[0, 1, 2, 3, 4, 5] = 0
    finished_task_num: Literal[0, 1, 2, 3, 4] = 0
    total_task_num: int = 4
    is_extra_task_reward_received: bool = False
    current_home_coin: int = 0
    max_home_coin: int = 0
    home_coin_recovery_time: int = 0

    expeditions: List[dict] = []

    finished_expedition_num: Literal[0, 1, 2, 3, 4, 5] = 0
