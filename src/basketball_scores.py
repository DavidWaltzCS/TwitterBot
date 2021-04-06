#File used to connect twitter api

import os
import re
import sys
import json
import requests
import configparser
from datetime import datetime
from twitter import send_tweet



def get_Bucks_game():
    games = get_games()
    games = games.json()
    gamesTonight = games['api']['results']
    gameData = {'hTeam': '','vTeam': '','hScore': '', 'vScore':'', 'status': '','arena': '', 'gameId' : ''}
    for i in range(gamesTonight):
        vTeam = games['api']['games'][i]['vTeam']['nickName']
        hTeam = games['api']['games'][i]['hTeam']['nickName']
        if(vTeam == 'Bucks' or hTeam == "Bucks"):
            gameData['hTeam'] = games['api']['games'][i]['hTeam']['nickName']
            gameData['vTeam'] = games['api']['games'][i]['vTeam']['nickName']
            gameData['hScore'] = games['api']['games'][i]['hTeam']['score']['points']
            gameData['vScore'] = games['api']['games'][i]['vTeam']['score']['points']
            gameData['status'] = games['api']['games'][i]['statusGame']
            gameData['arena'] = games['api']['games'][i]['arena']
            gameData['gameId'] = games['api']['games'][i]['gameId']
    return gameData
            
  
def get_credentials():
    config = configparser.ConfigParser()
    config.read(os.path.abspath("../config.ini"))
    params = {'key': '','host': ''}
    params['key'] = config.get('authBasketball', 'key')
    params['host'] = config.get('authBasketball', 'host')
    return params
    
def get_games():
  dateVar = datetime.today().strftime('%Y-%m-%d')
  url = "https://api-nba-v1.p.rapidapi.com/games/date/" + dateVar
  params = get_credentials()
  headers = {
    'x-rapidapi-key': params['key'],
    'x-rapidapi-host': params['host']
    }
  response = requests.request("GET", url, headers=headers)
  return response

