from twitter import TwitterRestApiBaseClass


class Status(TwitterRestApiBaseClass):
    resource = 'statuses/'

    def home_timeline(self, **kwargs):
        """
        Returns a collection of the most recent Tweets and retweets posted by the authenticating
        user and the users they follow. The home timeline is central to how most users interact
        with the Twitter service.
        """
        resource = self.resource + 'home_timeline'
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response

    def lookup(self, **kwargs):
        """
        Returns fully-hydrated Tweet objects for up to 100 Tweets per request, as specified by
        comma-separated values passed to the id parameter.
        """
        resource = self.resource + 'lookup'
        required = ['id']
        metadata, response = self.__get__(resource, required, kwargs)  # use metadata for something else.
        return response

    def mentions_timeline(self, **kwargs):
        """
        Returns the 20 most recent mentions (Tweets containing a users’s @screen_name) for
        the authenticating user.
        """
        resource = self.resource + 'mentions_timeline'
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response

    def oembed(self, **kwargs):
        """
        Returns a single Tweet, specified by either a Tweet web URL or the Tweet ID, in an
        oEmbed-compatible format. The returned HTML snippet will be automatically recognized
        as an Embedded Tweet when Twitter’s widget JavaScript is included on the page.
        """
        resource = self.resource + 'oembed'
        required = ['url']
        metadata, response = self.__get__(resource, required, kwargs)  # use metadata for something else.
        return response

    def user_timeline(self, **kwargs):
        """
        Returns a collection of the most recent Tweets posted by the user indicated by the
        screen_name or user_id parameters.
        """
        resource = self.resource + 'user_timeline'
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response
