# coding_task.py
#celery -A celery_task worker --loglevel=info --concurrency=1

# coding_task.py
import sys

from celery import Celery
from spider_run import run_spider

app = Celery('coding.net', backend='redis', broker='redis://localhost:6379/0')
#app.config_from_object('celery_config')


@app.task
def period_task():
    print('init')
   # run_spider()