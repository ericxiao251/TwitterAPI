from twitter import TwitterRestApiBaseClass


class Search(TwitterRestApiBaseClass):
    resource = 'search/'

    def tweets(self, **kwargs):
        resource = self.resource + 'tweets'
        required = ['q']
        response = self.__get__(resource, required, kwargs)  # use metadata for something else.
        return response['statuses']
