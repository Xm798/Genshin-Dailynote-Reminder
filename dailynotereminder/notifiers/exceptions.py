class AlertException(Exception):
    """Base genshinhelper exception."""


class CookiesExpired(AlertException):
    """Cookies has expired."""


class NotificationError(AlertException):
    """
    A notification error. Raised after an issue with the sent notification.
    """


class NoSuchNotifierError(AlertException):
    """
    An unknown notifier was requests, one that was not registered.
    """
