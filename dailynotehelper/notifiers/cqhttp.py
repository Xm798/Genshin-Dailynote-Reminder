from .basenotifier import BaseNotifier as Base
from ..config import config


class Cqhttp(Base):
    def __init__(self):
        self.name = 'Cqhttp'
        self.token = config.CQHTTP_URL and config.CQHTTP_MESSAGE_TYPE and config.CQHTTP_SEND_ID
        self.retcode_key = 'retcode'
        self.retcode_value = 0
        self.url = config.CQHTTP_URL if config.CQHTTP_URL else ''
        self.auth = config.CQHTTP_TOKEN if config.CQHTTP_TOKEN else ''


    def send(self, text, status, desp):
        if config.CQHTTP_MESSAGE_TYPE == "group":
            url = (f'{self.url}send_group_msg' if self.url.endswith('/') else f'{self.url}/send_group_msg' )
            header = {'Authorization': 'Bearer ' + self.auth}
            data = {
                "group_id": config.CQHTTP_SEND_ID,
                "message": f'{text} {status}\n\n{desp}'
            }
        elif config.CQHTTP_MESSAGE_TYPE == "private":
            url = (f'{self.url}send_private_msg' if self.url.endswith('/') else f'{self.url}/send_private_msg')
            header = {'Authorization': 'Bearer ' + self.auth}
            data = {
                "user_id": config.CQHTTP_SEND_ID,
                "message": f'{text} {status}\n\n{desp}'
            }

        return self.push('post', url, headers=header, data=data)
