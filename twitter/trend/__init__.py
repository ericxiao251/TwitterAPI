from twitter import TwitterRestApiBaseClass


class Trend(TwitterRestApiBaseClass):
    resource = 'trends/'

    def available(self, **kwargs):
        """
        Returns the locations that Twitter has trending topic information for.

        The response is an array of “locations” that encode the location’s WOEID and some other
        human-readable information such as a canonical name and country the location belongs in.
        """
        resource = self.resource + 'available'
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response

    def closest(self, **kwargs):
        """
        Returns the locations that Twitter has trending topic information for, closest to a
        specified location.

        The response is an array of “locations” that encode the location’s WOEID and some other
        human-readable information such as a canonical name and country the location belongs in.
        """
        resource = self.resource + 'closest'
        required = ['lat', 'long']
        metadata, response = self.__get__(resource, required, kwargs)  # use metadata for something else.
        return response

    def place(self, **kwargs):
        """
        Returns the top 50 trending topics for a specific WOEID, if trending information is
        available for it.

        The response is an array of trend objects that encode the name of the trending topic,
        the query parameter that can be used to search for the topic on Twitter Search, and the
        Twitter Search URL.
        """
        resource = self.resource + 'place'
        required = ['id']
        metadata, response = self.__get__(resource, kwargs)  # use metadata for something else.
        return response
