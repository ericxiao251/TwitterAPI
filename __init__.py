from twitter import Twitter
from twitter.search import Search

if __name__ == '__main__':
    CONSUMER_KEY = 'i6osYlAMvLyiSFYV56eHEcA50'
    CONSUMER_SECRET = 'A67oLT5d2NzTZc6xTbYGoJI8GDecRHRpJ8hFJenMM8lfbqLOBA'
    OAUTH_TOKEN = '843826210820055041-w0uUuj1xNGp9kdu4pwsLKHHc4pwZd5z'
    OAUTH_TOKEN_SECRET = 'p7PV5i3Gdz5mEXsbBSJG1PzJ1rU6woKe8359r1cCWaecD'

    twitter_object = Twitter(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    tweet = Search(twitter_object).tweet(q='%23freebandnames')

    print(tweet)
