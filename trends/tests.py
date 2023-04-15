import praw
from django.test import TestCase
from django.core.management import call_command
from unittest.mock import patch
from trends.models import TickerHits, Tickers, Version, Twitter
import requests
import base64
from django.test import TestCase

class RedditTest(TestCase):

    def setUp(self):
        Tickers.objects.create(symbol='AAPL')
        Version.objects.create(id=1)

    @patch('praw.Reddit')
    def test_reddit_command(self, mock_reddit):
        # Mocking the reddit API call
        mock_submission = mock_reddit.return_value.submission.return_value
        mock_submission.title = 'Apple stock analysis'
        mock_submission.comments.replace_more.return_value = []
        mock_submission.comments.__iter__.return_value = []
        mock_submission.id = '1234'

        # Calling the command
        call_command('reddit')

        # Assertions
        tickers = Tickers.objects.all()
        self.assertEqual(TickerHits.objects.count(), 1)
        self.assertEqual(TickerHits.objects.first().hits, 1)
        self.assertEqual(TickerHits.objects.first().tickers_id, tickers.first().id)
        self.assertEqual(TickerHits.objects.first().version, 2)
        self.assertEqual(Version.objects.first().version, 2)

class TwitterTest(TestCase):

    def setUp(self):
        Tickers.objects.create(symbol='AAPL')

    @patch('requests.post')
    @patch('requests.get')
    def test_twitter_command(self, mock_get, mock_post):
        # Mocking the Twitter API calls
        mock_access_token = 'mock_access_token'
        mock_post.return_value.json.return_value = {'access_token': mock_access_token}
        mock_get.return_value.json.return_value = [{'trends': [{'name': '#AAPL'}, {'name': '#NFLX'}, {'name': '#TSLA'}]}]

        # Calling the command
        call_command('twitter')

        # Assertions
        self.assertEqual(Twitter.objects.count(), 1)
        self.assertEqual(Twitter.objects.first().tickers_id, Tickers.objects.first().id)