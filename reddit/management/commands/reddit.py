import praw

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from reddit.models import TickerHits, Tickers, Version


class Command(BaseCommand):

    def handle(self, *args, **options):
        reddit = praw.Reddit(client_id='', client_secret='', user_agent='praw')
        subreddits = ['investing', 'stocks', 'StockMarket']
        # try:
        #     body = ''
        #     for sub in subreddits:
        #         posts = reddit.subreddit(sub).hot(limit=50)
        #         for post in posts:
        #             submission = reddit.submission(id=post)
        #             body += ' {} '.format(submission.title)
        #             submission.comments.replace_more(limit=0)
        #             for top_level_comment in submission.comments:
        #                 body += ' {} '.format(top_level_comment.body)
        #     print(body)
        # except Exception as e:
        #     print(e)

        tickers = Tickers.objects.all()
        body = 'i like this. GME AMC BB i like this'
        body = body.replace('.', ' ').replace(',', ' ')
        body = body.lower()
        # version, created = Version.objects.get_or_create(
        #     id=1,
        #     version=1
        # )
        # print(version)
        # print(created)
        #     v.version += 1
        #     v.save()
        for ticker in tickers:
            if ' {} '.format(ticker.symbol.lower()) in body or ' ${} '.format(ticker.symbol.lower()) in body:
                print(ticker.symbol)
                ticker_hits, created = TickerHits.objects.get_or_create(
                    tickers_id=ticker.id,
                    hits=0,
                    created_at=timezone.localtime(timezone.now()),
                    # version_id=version.id
                )
                ticker_hits.hits += 1
                ticker_hits.save()

        self.stdout.write(self.style.SUCCESS('Successfully exexuted reddit'))
