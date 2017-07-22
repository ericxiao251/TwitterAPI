from twitter import TwitterRestApiBaseClass


class Search(TwitterRestApiBaseClass):
    def tweet(self, **kwargs):
        resource = 'home_timeline'
        required = ['q']
        return self.__get__(resource, required, kwargs)
