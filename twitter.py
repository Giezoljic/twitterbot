import tweepy
import time

auth = tweepy.OAuthHandler('cnab5P79PWmBud6D36idavDAh','CV0h5SicEFiFMSCwVGhsC8A94IV12UbQibTvftDuu3kjH0Wrd6')
auth.set_access_token('1280437755349045248-NScA1PdqjrqtTgw6M9pFaoiSLyiF4Y','tJwQDIn2bh9NE5xj806F4YJUt5HjWR9wKubd3F6qwVQmh')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#programmingmemes'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet retweet')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break