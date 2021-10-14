from getinfo import MysAPI
from exwecom import SendWeixin
from getinfo.exceptions import APIError
from serverchan import ServerChan
from config import config
import json
import time

"""
current_resin=35 当前树脂
max_resin=160 树脂上限
resin_discount_num_limit=3  本周剩余树脂减半次数
resin_recovery_time=59900 树脂恢复时间

current_expedition_num=5 当前派遣数量
finished_task_num=0 完成的委托数量
total_task_num=4 全部委托数量
is_extra_task_reward_received=False  额外委托？突发事件？不知道~
max_expedition_num=5 最大派遣数量

"""


def seconds2hours(seconds: int) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def sendAll(title: str, info: str) -> None:
    if config.WECOM_STATUS == "ON":
        wx = SendWeixin(title, info)
        wx.send_message()
        # wx.send_message("markdown")

    if config.SERVER_CHAN_STATUS == "ON":
        ServerChan.send(title, status="", desp=info)


def main() -> None:
    uid = config.UID
    cookie = config.COOKIE
    try:
        res = MysAPI(uid, cookie).get_dailyNote()
    except APIError:
        send = SendWeixin("error", "发生错误，请检查cookie与id是否对应").main()
        exit()

    result: list[str] = []

    # current_resin
    if(config.RECEIVE_RESIN_DATA == "ON"):
        current_resin: str = f"{res['current_resin']}/{res['max_resin']}"
        result.append(f"当前树脂：{current_resin}")
        if(res['current_resin'] != 160):
            # resin_recovery_time
            resin_recovery_time = seconds2hours(res['resin_recovery_time'])
            result.append(f"树脂恢复时间：{resin_recovery_time}")

    # resin_discount_num_limit
    if(config.RECEIVE_BOSS_COUNT == "ON"):
        count: int = res['resin_discount_num_limit']
        result.append(f"本周boss战树脂减半剩余使用次数：{3-count}/3")

    # task_num
    if(config.RECEIVE_TASK_NUM == "ON"):
        task_num: str = f"{res['finished_task_num']}/{res['total_task_num']}"
        result.append(f"今日完成委托数量：{task_num}")

    # expedition_num
    if(config.REVEIVE_EXPEDITION_NUM == "ON"):
        with open('avatar_name.json', 'r', encoding='utf-8') as f:
            avatar_json = json.load(f)
        expedition_num = f"{res['current_expedition_num']}/{res['max_expedition_num']}"
        expedition_info: list[str] = []
        for expedition in res["expeditions"]:
            avatar: str = expedition['avatar_side_icon'][89:-4]
            try:
                avatar_name: str = avatar_json[avatar]
            except KeyError:
                avatar_name: str = avatar+"（请自行修改avatar_name.json或获取更新）"

            if(expedition['status'] == 'Finished'):
                expedition_info.append(f"{avatar_name} 已完成")
            else:
                remained_timed: str = seconds2hours(
                    expedition['remained_time'])
                expedition_info.append(
                    f"{avatar_name} 未完成，剩余时间{remained_timed}")

        expedition_data: str = "\n".join(expedition_info)
        fin_data: str = f"当前探索派遣数量：{expedition_num}\n详细:\n{expedition_data}"
        result.append(fin_data)

    info = "\n".join(result)

    if(int(res['current_resin']) >= int(config.RESIN_ALERT_NUM)):
        sendAll("亲爱的亲爱的亲爱的旅行者！树脂快溢出啦！", info)

    if(config.INCOMPLETE_ALERT != "" and res['finished_task_num'] != 4):
        time1 = time.strptime(config.INCOMPLETE_ALERT, '%H%M%S')
        time2 = time.localtime()
        if(time2.tm_hour == time1.tm_hour and time2.tm_min >= time1.tm_min or time2.tm_hour > time1.tm_hour and time2.tm_min < time1.tm_min):
            sendAll("亲爱的亲爱的亲爱的旅行者！你今日的委托还没有完成哦~", info)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
