import praw
import pprint

from django.core.management.base import BaseCommand, CommandError

from reddit.models import TickerHits, Tickers


class Command(BaseCommand):

    def handle(self, *args, **options):
        reddit = praw.Reddit(client_id=, client_secret=', user_agent='praw')
        investing_posts = reddit.subreddit('investing').hot(limit=50)
        stocks_posts = reddit.subreddit('stocks').hot(limit=50)
        stock_market_posts = reddit.subreddit('StockMarket').hot(limit=50)
        try:
            body = ''
            for post in investing_posts:
                submission = reddit.submission(id=post)
                body += submission.title
                for top_level_comment in submission.comments:
                    print(top_level_comment.body)
                    body += top_level_comment.body

            for post in stocks_posts:
                submission = reddit.submission(id=post)
                body += submission.title
                for top_level_comment in submission.comments:
                    print(top_level_comment.body)
                    body += top_level_comment.body
            
            for post in stock_market_posts:
                submission = reddit.submission(id=post)
                body += submission.title
                for top_level_comment in submission.comments:
                    print(top_level_comment.body)
                    body += top_level_comment.body

            print(body)
                    
        except Exception as e:
            print(e)

        tickers = Tickers.objects.all()
        for ticker in tickers:
            if ticker.symbol in body:
                print(ticker.symbol)
                hits = TickerHits.get_or_create(
                    ticker_id = ticker.id,
                    hits
                )
                print(hits)
                hits += 1
                hits.save()
                print(hits)


        self.stdout.write(self.style.SUCCESS('Successfully exexuted reddit'))