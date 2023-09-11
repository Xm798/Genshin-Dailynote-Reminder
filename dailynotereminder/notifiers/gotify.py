from ..config import config
from .basenotifier import BaseNotifier as Base


class Gotify(Base):
    def __init__(self):
        self.name = 'gotify'
        self.token = config.GOTIFY_TOKEN
        self.retcode_value = 200

    def send(self, text, status, desp):
        url = f'{config.GOTIFY_URL}/message?token={config.GOTIFY_TOKEN}'
        data = {
            'title': f'{text}{status}',
            'message': f'{text}{status}\n\n{desp}',
            'priority': config.GOTIFY_PRIORITY
        }
        return self.push('post', url, json=data)