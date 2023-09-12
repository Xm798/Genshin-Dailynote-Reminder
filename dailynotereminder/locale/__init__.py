import gettext
from pathlib import Path

from ..config import config

_localedir = Path(__file__).parent.resolve()
_translate = gettext.translation(
    'dailynotereminder', _localedir, languages=[config.LANGUAGE], fallback=True
)
_ = _translate.gettext
