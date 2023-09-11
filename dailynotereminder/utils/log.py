import logging
import sys

from colorama import Back, Fore, Style


class Log:
    def __init__(self, log_filename=None):
        self.logger = logging.getLogger('Converter')
        self.logger.setLevel(logging.DEBUG)

        self.logger.handlers = []

        console_handler = self.ColoredConsoleHandler(stream=sys.stdout)
        self.logger.addHandler(console_handler)

        if log_filename:
            file_handler = logging.FileHandler(log_filename)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    class ColoredConsoleHandler(logging.StreamHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S'
            )
            self.setFormatter(formatter)

        def emit(self, record):
            if record.levelno == logging.DEBUG:
                color = Fore.CYAN
            elif record.levelno == logging.INFO:
                color = Fore.GREEN
            elif record.levelno == logging.WARNING:
                color = Fore.YELLOW
            elif record.levelno == logging.ERROR:
                color = Fore.RED
            elif record.levelno == logging.CRITICAL:
                color = Back.RED + Fore.WHITE
            else:
                color = Fore.WHITE

            record.msg = color + str(record.msg) + Style.RESET_ALL

            super().emit(record)
