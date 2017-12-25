import twitter as twitter_api_client


class TwitterClient(object):
    """Class to handle communication with the Twitter API."""

    def __init__(self, config):
        """Class constructor."""
        self.CONSUMER_KEY = config['consumer_key']
        self.CONSUMER_SECRET = config['consumer_secret']
        self.ACCESS_TOKEN_KEY = config['access_token_key']
        self.ACCESS_TOKEN_SECRET = config['access_token_secret']

        self.api = twitter_api_client.Api(
            consumer_key=self.CONSUMER_KEY,
            consumer_secret=self.CONSUMER_SECRET,
            access_token_key=self.ACCESS_TOKEN_KEY,
            access_token_secret=self.ACCESS_TOKEN_SECRET
        )

    def get_friends(self, screen_name=None):
        """
        Get user's friends.

        Args:
            screen_name -- If defined, friends are returned for the specific
                           user. If not defined, the authenticated user's
                           friends are returned.
        """
        return self.api.GetFriends(screen_name=screen_name)

    def get_followers(self, screen_name=None):
        """
        Get user's followers.

        Args:
            screen_name -- If defined, followers are returned for the specific
                           user. If not defined, the authenticated user's
                           followers are returned.
        """
        return self.api.GetFollowers(screen_name=screen_name)
