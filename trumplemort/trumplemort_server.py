import tweepy

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from trumplemortify import trumplemortify
import trumplemap

import secrets

class TrumplmortListener(StreamListener):

#    trump_id = "25073877"
    trump_id = 1449793027

    def __init__(self):
        super().__init__()
        self.auth = OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
        self.auth.set_access_token(secrets.access_token, secrets.access_token_secret)


    def on_status(self, status):
        if status.author.id == self.trump_id:
            trumpled_status = trumplemortify(status.text, trumplemap.terms)
            self.tweet(trumpled_status)
        return(True)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        if status_code == 406:
            #returning False in on_data disconnects the stream
            return False

    def tweet(self, status):
        api = tweepy.API(self.auth)
        api.update_status(status)


def main():
    
    listener = TrumplmortListener()

    twitterStream = Stream(auth=listener.auth, listener=listener)
    twitterStream.filter(follow=[str(listener.trump_id)], async=True)


if __name__ == '__main__':
    main()

