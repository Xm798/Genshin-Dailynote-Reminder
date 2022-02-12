from dailynotehelper.__banner__ import banner, run_once

def main_handler(event, context):
    print(banner)
    run_once()
    return