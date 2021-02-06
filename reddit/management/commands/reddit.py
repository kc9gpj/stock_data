import praw

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db.models import F

from reddit.models import TickerHits, Tickers, Version
import keys

class Command(BaseCommand):

    def handle(self, *args, **options):
        reddit = praw.Reddit(client_id=keys.client_id, client_secret=keys.client_secret, user_agent=keys.user_agent)
        subreddits = ['investing', 'stocks', 'StockMarket']
        try:
            body = ''
            for sub in subreddits:
                posts = reddit.subreddit(sub).hot(limit=50)
                for post in posts:
                    submission = reddit.submission(id=post)
                    body += ' {} '.format(submission.title)
                    submission.comments.replace_more(limit=0)
                    for top_level_comment in submission.comments:
                        body += ' {} '.format(top_level_comment.body)
            print(body)
        except Exception as e:
            print(e)

        tickers = Tickers.objects.all()
        # body = 'i like this. GME. AMC BB GME GME i like this'
        body = body.replace('.', ' ').replace(',', ' ')
        # version, created = Version.objects.get_or_create(
        #     id=1,
        #     version=1
        # )
        # print(version.version)
        TickerHits.objects.all().delete()
        for word in body.split():
            for ticker in tickers:
                if word == ticker.symbol or word == '${}'.format(ticker.symbol):
                    print(ticker.symbol)

                    hits, created = TickerHits.objects.get_or_create(
                        tickers_id=ticker.id,
                        version=1,
                    )
                    print(hits.id)
                    TickerHits.objects.filter(id=hits.id).update(hits=F("hits") + 1)
                    h = TickerHits.objects.filter(id=hits.id).first()
                    print(h.hits)
                    # P.objects.filter(username="John Smith").update(accvalue=F("accvalue") + 50)
        # Version.objects.filter(id=version.id).update(version=F("version") + 1)
        self.stdout.write(self.style.SUCCESS('Successfully exexuted reddit'))
