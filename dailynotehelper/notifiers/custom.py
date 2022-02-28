from .basenotifier import BaseNotifier as Base
from ..config import config


class Custom(Base):
    def __init__(self):
        self.name = 'Custom'
        self.conf = config.CUSTOM_NOTIFIER
        self.token = self.url = self.conf.get('url')
        self.data = self.conf.get('data')
        self.headers = self.conf.get('headers')
        self.retcode_key = self.conf.get('retcode_key')
        self.retcode_value = self.conf.get('retcode_value')


    def send(self, text, status, desp):
        if not self.token:
            return self.push('post', '')
        
        title = f'{text} {status}'
        if self.conf.get('markdown'):
            desp = f'```\n{desp}\n```'
        if self.conf.get('desp_key'):
            self.data[self.conf.get('title_key')] = title
            self.data[self.conf.get('desp_key')] = desp
        else:
            self.data[self.conf.get('title_key')] = f'{title}\n\n{desp}'

        if self.conf['method'].upper() == 'GET':
            return self.push('get', self.url, params=self.data, headers=self.headers)
        elif self.conf['method'].upper() == 'POST' and self.conf['data_type'].lower() == 'json':
            return self.push('post', self.url, json=self.data, headers=self.headers)
        else:
            return self.push('post', self.url, data=self.data, headers=self.headers)
