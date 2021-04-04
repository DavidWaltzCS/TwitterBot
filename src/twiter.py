#File used to connect twitter api

import os
import re
import sys
import json
import tweepy
import requests
import configparser

def getCredentials():
    config = configparser.ConfigParser()
    config.read(os.path.abspath("../config.ini"))
    params = {'consKey': '','consSecret': '','accToken': '', 'accSecret':''}
    params['consKey'] = config.get('authTwitter', 'consKey')
    params['consSecret'] = config.get('authTwitter', 'consSecret')
    params['accToken'] = config.get('authTwitter', 'accToken')
    params['accSecret'] = config.get('authTwitter', 'accSecret')
    return params
    
def twitter_authentication():
  params = getCredentials()
  auth = tweepy.OAuthHandler(params['consKey'], params['consSecret'])
  auth.set_access_token(params['accToken'], params['accSecret'])
  return tweepy.API(auth)

def main():
  api = twitter_authentication()
  status = "Hello World. #FearTheDeer"
  api.update_status(status)

  

if __name__ == "__main__":
    main()
	

