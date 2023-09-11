from .exceptions import NotificationError
from .utils import log, request


class BaseNotifier(object):
    def __init__(self):
        self.name = None
        self.token = None
        self.retcode_key = None
        self.retcode_value = None

    def send(self, text, status, desp):
        ...

    def push(
        self, method, url, params=None, data=None, json=None, headers=None, proxies=None
    ):
        """
        🚫: disabled
        🥳: success
        😳: failure
        """
        if not self.token:
            # log.info(f'{self.name} 🚫')
            return
        try:
            response = request(
                method, url, 2, params, data, json, headers, proxies=proxies
            )
        except Exception as e:
            log.error(f'{self.name} 😳\n{e}')
            raise NotificationError()
        else:
            if self.name == 'Server Chan Turbo':
                retcode = response.json().get('data', {}).get(self.retcode_key, -1)
            elif self.name == 'Discord' or self.name == 'gotify':
                retcode = response.status_code
            else:
                retcode = response.json().get(self.retcode_key, -1)
            if retcode == self.retcode_value:
                log.info(f'{self.name} 🥳')

            # Telegram Bot
            elif self.name == 'Telegram Bot' and retcode:
                log.info(f'{self.name} 🥳')
            elif (
                self.name == 'Telegram Bot'
                and response.json()[self.retcode_value] == 400
            ):
                log.error(f'{self.name} 😳\n请主动给 bot 发送一条消息并检查 TG_USER_ID 是否正确')
                log.error(response.json())
                raise NotificationError()
            elif (
                self.name == 'Telegram Bot'
                and response.json()[self.retcode_value] == 401
            ):
                log.error(f'{self.name} 😳\nTG_BOT_TOKEN 错误')
                log.error(response.json())
                raise NotificationError()
            # Chanify
            elif self.name == 'Chanify' and response.json().get('request-uid'):
                log.info(f'{self.name} 🥳')

            else:
                log.error(f'{self.name} 😳\n{response}')
                log.error(response.json())
                raise NotificationError()
        # 一个推送渠道失败后不会继续进行推送
        finally:
            return
