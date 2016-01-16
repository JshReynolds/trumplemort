
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from trumplemortify import Trumplemortifier

import json
import pprint

import secrets

class TrumplmortListener(StreamListener):

    trumplemortifier = Trumplemortifier()

    trump_id = "25073877"

    def on_status(self, status):
        
        if status.author.id == self.trump_id:
            trumpled_status = trumplemortifier.trumplemortify(status.text)
            print(trumpled_status)
            pass

        return(True)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        if status_code == 406:
            #returning False in on_data disconnects the stream
            return False


auth = OAuthHandler(secrets.ckey, secrets.csecret)
auth.set_access_token(secrets.atoken, secrets.asecret)

listener = TrumplmortListener()

twitterStream = Stream(auth=auth, listener=listener)
twitterStream.filter(follow=[listener.trump_id], async=True)