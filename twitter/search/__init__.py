from twitter import TwitterRestApiBaseClass


class Search(TwitterRestApiBaseClass):
    resource = 'search/'

    def tweets(self, **kwargs):
        resource = self.resource + 'tweets'
        required = ['q']
        return self.__get__(resource, required, kwargs)
