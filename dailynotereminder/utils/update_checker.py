import re

import requests

from dailynotereminder.__version__ import version as current_version
from dailynotereminder.config import config
from dailynotereminder.locale import _
from dailynotereminder.notifiers import send
from dailynotereminder.utils import log


def get_latest_version_github(repo):
    url = f'https://api.github.com/repos/{repo}/releases/latest'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            latest_version = data.get('tag_name', None)
            latest_url = data.get('html_url', None)
            latest_desc = data.get('body', "")
            latest = {'version': latest_version, 'url': latest_url, 'desc': latest_desc}
            return latest
        else:
            log.warning(
                f'Failed to check latest version from github: {response.status_code}'
            )
            return None
    except Exception as e:
        log.warning(f'Failed to check latest version from github: {e}')
        return None


def get_latest_version_jihulab(repo):
    url = f"https://jihulab.com/api/v4/projects/{repo.replace('/', '%2F')}/releases"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                latest_release = data[0]
                latest_version = latest_release.get('tag_name', None)
                latest_desc = latest_release.get('description', "")
                latest = {
                    'version': latest_version,
                    'url': f'https://jihulab.com/{repo}/-/releases/{latest_version}',
                    'desc': latest_desc,
                }
                return latest
            else:
                log.warning(
                    f'Failed to check latest version from jihulab: data is empty'
                )
        else:
            log.warning(
                f'Failed to check latest version from jihulab: {response.status_code}'
            )
        return None
    except Exception as e:
        log.warning(f'Failed to check latest version from jihulab: {e}')
        return None


def generate_update_message(latest_info):
    return _('当前版本：{}\n最新版本：{}\n更新地址：{}').format(
        current_version, latest_info['version'], latest_info['url']
    )


def notify_update(latest_info):
    message = generate_update_message(latest_info)
    send(text='🎉', status=_('Genshin-Dailynote-Reminder 有更新啦'), message=message)


def check_update():
    repo = 'Xm798/Genshin-Dailynote-Reminder'
    latest_info = get_latest_version_github(repo) or get_latest_version_jihulab(repo)

    if not latest_info:
        log.warning(_('⚠️ 检查版本更新失败'))
        return

    if has_new_version(current_version, latest_info['version']):
        log.info(_('🎉 检查到新版本 {}').format(latest_info['version']))
        should_notify = "#NOTIFY" in latest_info.get('desc', '')

        if config.CHECK_UPDATE in ['default', True]:
            if should_notify:
                notify_update(latest_info)
            else:
                log.info(_('⬆️ 不发送通知，请前往 {} 下载').format(latest_info['url']))
        else:
            notify_update(latest_info)
    else:
        log.info(_('🔄 当前已是最新版本，无需更新'))


def has_new_version(current, latest):
    return version_to_number(latest) > version_to_number(current)


def version_to_number(version):
    version = version.lstrip('v')
    version = re.split('[-+]', version)[0]
    version_list = [int(x) for x in version.split('.')]

    number = 0
    if len(version_list) > 0:
        number += version_list[0] * 10000
    if len(version_list) > 1:
        number += version_list[1] * 100
    if len(version_list) > 2:
        number += version_list[2]

    return number
