import os

from dailynotereminder import run_once
from dailynotereminder.__banner__ import banner


# Tencent SCF
def main_handler(event, context):
    print(banner)
    os.environ['SERVERLESS'] = 'true'
    run_once()
    return


# Aliyun FC
def handler(event, context):
    print(banner)
    os.environ['SERVERLESS'] = 'true'
    run_once()
    return
