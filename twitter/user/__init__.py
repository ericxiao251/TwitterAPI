from twitter import TwitterRestApiBaseClass


class User(TwitterRestApiBaseClass):
    resource = 'users/'

    def lookup(self, **kwargs):
        """
        Returns fully-hydrated user objects for up to 100 users per request, as specified by
        comma-separated values passed to the user_id and/or screen_name parameters.
        """
        resource = self.resource + 'lookup'
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response

    def profile_banner(self, **kwargs):
        """
        Returns a map of the available size variations of the specified user’s profile banner.
        If the user has not uploaded a profile banner, a HTTP 404 will be served instead. This
        method can be used instead of string manipulation on the profile_banner_url returned
        in user objects as described in Profile Images and Banners.
        """
        resource = self.resource + 'profile_banner'
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response

    def search(self, **kwargs):
        """
        Provides a simple, relevance-based search interface to public user accounts on Twitter.
        Try querying by topical interest, full name, company name, location, or other criteria.
        Exact match searches are not supported.
        """
        resource = self.resource + 'search'
        required = ['q']
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response

    def show(self, **kwargs):
        """
        Provides a simple, relevance-based search interface to public user accounts on Twitter.
        Try querying by topical interest, full name, company name, location, or other criteria.
        Exact match searches are not supported.
        """
        resource = self.resource + 'show'
        required = ['user_id', 'screen_name']
        metadata, response = self.__get__(resource, required, kwargs)  # use metadata for something else.
        return response
