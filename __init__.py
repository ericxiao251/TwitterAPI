import oauth2 as oauth

class Twitter(object):
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret

        if not all([isinstance(self.consumer_key, str), isinstance(self.consumer_secret, str),
                    isinstance(self.access_token_key, str), isinstance(self.access_token_secret, str)]):
            raise TypeError("Keys are not strings")
        try:
            consumer = oauth.Consumer(self.consumer_key, self.consumer_secret)
            access_token = oauth.Token(1, self.access_token_secret)

            self.client = oauth.Client(consumer, access_token)
            self.base_url = 'https://api.twitter.com/1.1/'
        except:
            print('Error, invalid keys')

    def __get__(self, url):
        try:
            response, data = self.client.request(url)
            return response
        except:
            raise KeyError("invalid parameters passed to request.")

class TwitterRestApiBaseClass(object):
    def __init__(self, twitter):
        if isinstance(twitter, Twitter):
            self.twitter = Twitter(twitter.consumer_key, twitter.consumer_secret,
                                   twitter.access_token_key, twitter.access_token_secret)
        else:
            raise TypeError("a twitter object was not passed in.")


class TwitterGetRequest(TwitterRestApiBaseClass):
    def __get__(self, url):
        return self.twitter.__get__(url)


class Search(TwitterGetRequest):
    def tweet(self, q, **kwargs):
        if not q:
            raise ValueError('No parameter q passed in.')

        request = str(self.twitter.base_url + '/search/tweets.json?q=' + q)
        for key, value in kwargs.items():
            request = str('&' + request + key + '=' + value)

        return self.__get__(request)


if __name__ == '__main__':
    CONSUMER_KEY = 'i6osYlAMvLyiSFYV56eHEcA50'
    CONSUMER_SECRET = 'A67oLT5d2NzTZc6xTbYGoJI8GDecRHRpJ8hFJenMM8lfbqLOBA'
    OAUTH_TOKEN = '843826210820055041-w0uUuj1xNGp9kdu4pwsLKHHc4pwZd5z'
    OAUTH_TOKEN_SECRET = 'p7PV5i3Gdz5mEXsbBSJG1PzJ1rU6woKe8359r1cCWaecD'

    twitter_object = Twitter(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    tweet = Search(twitter_object).tweet('%23freebandnames')

    print(tweet)
