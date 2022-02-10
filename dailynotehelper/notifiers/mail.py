from .basenotifier import BaseNotifier as Base
from ..config import config
import smtplib
from email.mime.text import MIMEText
from .utils import log
from .exceptions import NotificationError

class Mail(Base):
    def __init__(self):
        self.name = 'Mail'
        self.token = config.MAIL_HOST and config.MAIL_USERNAME and config.MAIL_PASSWORD and config.MAIL_TO

    def send(self, text, status, desp):
        if not self.token:
            return
        message = MIMEText(desp,'plain','utf-8')
        message['From'] = config.MAIL_USERNAME
        message['To'] = config.MAIL_TO
        message['Subject'] = f'{text} {status}'
        try:
            smtp = smtplib.SMTP_SSL(host=config.MAIL_HOST,port=config.MAIL_PORT,timeout=10)
        except Exception as e:
            log.error(f'{self.name} 😳\n{e}')
            raise NotificationError(f"邮箱服务器连接失败")
        else:
            if config.MAIL_STARTTLS:
                smtp.starttls()
            try:
                smtp.login(config.MAIL_USERNAME,config.MAIL_PASSWORD)
                smtp.sendmail(config.MAIL_USERNAME,config.MAIL_TO,message.as_string())
                smtp.quit()
                log.info(f'{self.name} 🥳')
            except smtplib.SMTPException as e:
                log.error(f'{self.name} 😳\n{e}')
                raise NotificationError(f"邮件发送失败")
        return