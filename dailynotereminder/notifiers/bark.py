from .basenotifier import BaseNotifier as Base
from ..config import config


class Bark(Base):
    def __init__(self):
        self.name = 'Bark'
        self.token = config.BARK_URL if config.BARK_URL else ''
        self.retcode_key = 'code'
        self.retcode_value = 200

    def send(self, text, status, desp):
        url = self.token if self.token.endswith('/') else f'{self.token}/'
        data = {'title': f'{text}{status}', 'body': desp}

        # 可选项
        if config.BARK_GROUP:
            data['group'] = f'{config.BARK_GROUP}'
        if config.BARK_ICON:
            data['icon'] = f'{config.BARK_ICON}'
        if config.BARK_ARCHIVE:
            data['isArchive'] = f'{config.BARK_ARCHIVE}'
        if config.BARK_LEVEL:
            data['level'] = f'{config.BARK_LEVEL}'

        return self.push('post', url, data=data)
