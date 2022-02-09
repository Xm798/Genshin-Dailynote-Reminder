from dailynotehelper import run_once, __banner__

def main_handler(event, context):
    print(__banner__)
    run_once()
    return