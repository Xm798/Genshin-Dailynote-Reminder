from . import (
    dingtalkbot,
    discord,
    igot,
    pushplus,
    serverchanturbo,
    telegrambot,
    wechatworkapp,
    wechatworkbot,
    coolpush,
    qmsg,
    bark,
    cqhttp,
    pushdeer,
    mail,
    custom,
    chanify,
    gotify
)

from .exceptions import NoSuchNotifierError


_all_notifiers = {
    'dingtalkbot': dingtalkbot.DingTalkBot,
    'discord': discord.Discord,
    'igot': igot.Igot,
    'pushplus': pushplus.PushPlus,
    'serverchanturbo': serverchanturbo.ServerChanTurbo,
    'telegrambot': telegrambot.TelegramBot,
    'wechatworkapp': wechatworkapp.WechatWorkApp,
    'wechatworkbot': wechatworkbot.WechatWorkBot,
    'coolpush': coolpush.CoolPush,
    'qmsg': qmsg.Qmsg,
    'bark': bark.Bark,
    'cqhttp': cqhttp.Cqhttp,
    'pushdeer': pushdeer.Pushdeer,
    'mail': mail.Mail,
    'custom': custom.Custom,
    'chanify': chanify.Chanify,
    'gotify': gotify.Gotify,
}


def get_notifiers():
    return list(enumerate(_all_notifiers, start=1))


def get_notifier(name=None):
    notifiers = get_notifiers()
    notifier = [x for x in notifiers if name in x]
    if not notifier:
        raise NoSuchNotifierError(f'No {name} Notifier')
    return _all_notifiers[notifier[0][1]]()


def send2all(text='', status: str = '', desp: str = ''):
    for notifier in _all_notifiers:
        # 不支持 MARKDOWN 语法的推送渠道不做处理
        if notifier in ['serverchanturbo', 'pushdeer']:
            message = f'```\n{desp}\n```'
        else:
            message = desp
        get_notifier(notifier).send(text, status, message)
