from ..config import config
from .basenotifier import BaseNotifier as Base


class Chanify(Base):
    def __init__(self):
        self.name = 'Chanify'
        self.url = config.CHANIFY_URL if config.CHANIFY_URL else ''
        self.token = config.CHANIFY_TOKEN

        self.retcode_key = 'code'
        self.retcode_value = 200

    def send(self, text, status, desp):
        url = (
            f'{self.url}v1/sender/{self.token}'
            if self.url.endswith('/')
            else f'{self.url}/v1/sender/{self.token}'
        )
        data = {'title': f'{text}{status}', 'text': desp}

        # 可选项
        if config.CHAINFY_SOUND:
            data['sound'] = f'{config.CHAINFY_SOUND}'
        if config.CHAINFY_PRIORITY:
            data['priority'] = f'{config.CHAINFY_PRIORITY}'
        if config.CHAINFY_INTERRUPTION_LEVEL:
            data['interruption-level'] = f'{config.CHAINFY_INTERRUPTION_LEVEL}'

        return self.push('get', url, params=data)
