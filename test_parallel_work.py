from datetime import datetime, timedelta
import sys
import os
from time import sleep

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import logging
import asyncio
from utils import run_sync
#from db.tasks.volume import backup

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)



def backup():
    print("!!!")
    #sleep(20)
    for i in range(20):
        sleep(1)
        print(i)

if __name__ == '__main__':
    jobstores = {
    'default': SQLAlchemyJobStore(url=f"mysql+mysqldb://user:password@10.100.178.23:3306/cloudapi",
                                  tablename="backup_cron_jobs")
    }
    scheduler = BackgroundScheduler(jobstores=jobstores)
    alarm_time = datetime.now() + timedelta(seconds=5)
    hour = alarm_time.hour

    scheduler.add_job(backup, id='my_job_4id5', trigger='cron', day_of_week=alarm_time.strftime("%a").lower(),
                      hour=hour, minute=alarm_time.minute, second=alarm_time.second, replace_existing=True)
    # print(scheduler.get_jobs(jobstore='default'))
    #
    #
    # #scheduler.add_job(alarm, 'interval', minutes=3)#, args=[datetime.now()]
    # print('To clear the alarms, delete the example.sqlite file.')
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    # print(scheduler.get_jobs())
   # try:
    scheduler.start()
    print(scheduler.get_jobs())
    #     # f = r[-1]
    #     #
    #     # # t = f.trigger.fields
    #     # # for i in t[4:-1]:
    #     # #     tt,mm=i.name, str(i.expressions[0])
    #     # #     print(mm)
    #     # time = BackupTime()
    #     # cron_scheduler = scheduler.get_job(f.id)
    #     # cron_time = cron_scheduler.trigger.fields
    #     # time.week_day = cron_time[4].expressions[0]
    #     # time.hour = cron_time[5].expressions[0]
    #     # time.minutes = cron_time[6].expressions[0]
    #     # a = [time]
    #     # time = BackupTime()
    #     # a = 20
    sleep(30)
    while datetime.now() < alarm_time + timedelta(seconds=30):
        sleep(3)
        print(f"main function works")
    print(scheduler.get_jobs())
