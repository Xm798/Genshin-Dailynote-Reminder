from ..config import config
from .basenotifier import BaseNotifier as Base


class Discord(Base):
    def __init__(self):
        self.name = 'Discord'
        self.token = config.DISCORD_WEBHOOK
        self.retcode_value = 204
        self.proxies = (
            {'http': config.PROXY, 'https': config.PROXY} if config.PROXY else None
        )

    def send(self, text, status, desp):
        url = config.DISCORD_WEBHOOK
        data = {
            'username': config.DISCORD_USERNAME,
            'avatar_url': config.DISCORD_AVATAR,
            'embeds': [
                {
                    'title': f'{text}{status}',
                    'description': desp,
                    'color': config.DISCORD_COLOR,
                }
            ],
        }
        return self.push('post', url, json=data, proxies=self.proxies)
