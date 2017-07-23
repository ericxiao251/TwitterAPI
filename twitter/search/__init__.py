from twitter import TwitterRestApiBaseClass


class Search(TwitterRestApiBaseClass):
    resource = 'search/'

    def tweets(self, **kwargs):
        """
        Returns a collection of relevant Tweets matching a specified query.
        """
        resource = self.resource + 'tweets'
        required = ['q']
        metadata, response = self.__get__(resource, required, kwargs)  # use metadata for something else.
        return response
