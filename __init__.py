import json

from twitter import Twitter
from twitter.search import Search

if __name__ == '__main__':
    with open('secrets.json') as f:
        config = json.load(f)

    CONSUMER_KEY = config['consumer_key']
    CONSUMER_SECRET = config['consumer_secret']
    OAUTH_TOKEN = config['oauth_token']
    OAUTH_TOKEN_SECRET = config['oauth_token_secret']

    twitter_object = Twitter(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    tweet = Search(twitter_object).tweet(q='%23freebandnames')

    print(tweet)
