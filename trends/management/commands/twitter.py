import requests
import base64

from django.core.management.base import BaseCommand, CommandError

from trends.models import Twitter, Tickers
import keys

class Command(BaseCommand):

    def handle(self, *args, **options):
        key_secret = '{}:{}'.format(keys.twitter_key, keys.twitter_secret).encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret)
        b64_encoded_key = b64_encoded_key.decode('ascii')
        base_url = 'https://api.twitter.com/'
        auth_url = '{}oauth2/token'.format(base_url)

        auth_headers = {
            'Authorization': 'Basic {}'.format(b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        auth_data = {
            'grant_type': 'client_credentials'
        }

        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
        access_token = auth_resp.json()['access_token']
                
        trend_headers = {
            'Authorization': 'Bearer {}'.format(access_token)    
        }

        trend_params = {
            'id': 23424977,
        }

        trend_url = 'https://api.twitter.com/1.1/trends/place.json'  
        trend_resp = requests.get(trend_url, headers=trend_headers, params=trend_params)
        data = trend_resp.json()
        tweet_data = []
        for data in data[0]['trends']:
            tweet_data.append(data['name'].replace('#',''))

        tickers = Tickers.objects.all()

        for word in tweet_data:
            for ticker in tickers:
                if word == ticker.symbol or word == '${}'.format(ticker.symbol):
                    if word not in keys.excluded_tickers:
                        Twitter.objects.get_or_create(
                            tickers_id=ticker.id
                        )
        self.stdout.write(self.style.SUCCESS('Successfully exexuted twitter'))
