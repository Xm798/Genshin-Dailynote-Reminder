from dailynotehelper.__banner__ import banner
from dailynotehelper import run_once

def main_handler(event, context):
    print(banner)
    run_once()
    return