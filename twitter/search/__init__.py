from twitter import TwitterRestApiBaseClass
from twitter.utils import flatten_dict

class Search(TwitterRestApiBaseClass):
    resource = 'search/'

    def tweets(self, **kwargs):
        resource = self.resource + 'tweets'
        required = ['q']
        metadata, response = self.__get__(resource, required, kwargs)  # use metadata for something else.
        return [flatten_dict(tweet) for tweet in response['statuses']]
