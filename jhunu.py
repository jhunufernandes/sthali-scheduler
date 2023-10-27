from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler


def myfunc():
    print('xxx')


scheduler = BackgroundScheduler()

job = scheduler.add_job(myfunc, 'interval', seconds=1)

scheduler.start()

while True:
    sleep(1)
