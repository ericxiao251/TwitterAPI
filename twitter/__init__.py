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

    def __get__(self, resource, required, parameters):
        url = self.build_response_query(resource, required, parameters)
        return self.twitter.__get__(url)

    def check_parameters(self, required, parameters):
        for key in required:
            if key not in parameters:
                raise KeyError("required parameter %s was not given." % (key))

        return True

    def build_response_query(self, resource, required, parameters):
        if self.check_parameters(required, parameters):
            request = self.twitter.base_url + resource + '.json?'
            for key, value in parameters.items():
                request = str(request + key + '=' + value + '&')

            return request[:-1]
