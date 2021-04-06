import tweepy
import logging
from twitter import twitter_authentication
import time
from datetime import datetime




players = ["giannis","jrue","khris", "thanasis", "brooke", "bobby", "p.j.", "pj", "p.j", "bryn", "pat", "jeff", "sam" ]
playerIDPairing = {'giannis': '20','jrue': '242','thanasis': '2408', 'brooke':'323', 'bobby': '431','p.j.': '520', 'bryn': '176', 'pat':'115', 'jeff': '505','sam': '2623', 'khris':'361'}


def check_mentions(since_id):
    api = twitter_authentication()
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            
            continue
        for player in players:
            if (player in tweet.text.lower()):
                status = api.get_status(tweet.id)
                if ((str(status.created_at)[0:16:1])  == str(datetime.utcnow())[0:16:1] ):
                    api.update_status(status="will fetch stats about " + player+ " soon", in_reply_to_status_id=tweet.id,auto_populate_reply_metadata=True)    
    return new_since_id


