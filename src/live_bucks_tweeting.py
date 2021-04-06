import tweepy
import logging
from twitter import twitter_authentication
import time
import json 
import requests
from datetime import datetime
from basketball_scores import get_Bucks_game, get_credentials




players = ["giannis","jrue","khris", "thanasis", "brooke", "bobby", "p.j.", "pj", "p.j", "bryn", "pat", "jeff", "sam" ]
playerIdPairing = {'giannis': '20','jrue': '242','thanasis': '2408', 'brooke':'323', 'bobby': '431','p.j.': '520','p.j':'520', 'pj':'520' ,'bryn': '176', 'pat':'115', 'jeff': '505','sam': '2623', 'khris':'361'}

def get_player_data(playId, gameId):
    url = "https://api-nba-v1.p.rapidapi.com/statistics/players/gameId/" + gameId
    params = get_credentials()
    headers = {
        'x-rapidapi-key': params['key'],
        'x-rapidapi-host': params['host']
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    playerData = {'points': '','rebounds': '','assists': '', 'blocks':'', 'steals': ''}
    numPlayers = data['api']['results']
    for i in range(numPlayers):
        if playId == data['api']['statistics'][i]['playerId']:
           playerData['points'] =data['api']['statistics'][i]['points']
           playerData['blocks'] =data['api']['statistics'][i]['blocks']
           playerData['steals'] =data['api']['statistics'][i]['steals']
           playerData['assists'] =data['api']['statistics'][i]['assists']
           playerData['rebounds'] =data['api']['statistics'][i]['totReb']

    return playerData



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
                    bucksData = get_Bucks_game()
                    status = player + ' was not in action today'
                    if(bucksData != ''):
                        playerData = get_player_data(playerIdPairing[player],'8973')
                        status = player + " so far in todays game has "+ playerData['points']+' points, '+ playerData['blocks'] + ' blocks, '+playerData['steals']+' steals, '+playerData['assists'] +' assists, and '+playerData['rebounds']+' rebounds'
                    api.update_status(status=status, in_reply_to_status_id=tweet.id,auto_populate_reply_metadata=True)    
    return new_since_id


