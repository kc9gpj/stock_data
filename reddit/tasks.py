import praw
import csv 
import time

from background_task import background


# reddit = praw.Reddit(
#     client_id="my client id",
#     client_secret="my client secret",
#     user_agent="my user agent"
# )


def parse_csv():
    print('hi')


schedule.every(1).seconds.do(parse_csv)

while True:
    # run_pending
    schedule.run_pending()
    time.sleep(1)