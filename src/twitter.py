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


def send_tweet(bucksGame):
  api = twitter_authentication()
  tweet = ''
  if(bucksGame['hTeam'] == ''):
    tweet = 'The Bucks were not in action today'
  elif bucksGame['hTeam'] == 'Bucks':
    if bucksGame['hScore'] > bucksGame['vScore'] and bucksGame['status'] == 'Finished':
      tweet = 'The Bucks came away with a nice win home against ' + bucksGame['vTeam'] + ' with a score of '+bucksGame['hScore']+' to ' +bucksGame['vScore'] + ' #FearTheDeer'
    elif bucksGame['hScore'] < bucksGame['vScore'] and bucksGame['status'] == 'Finished':
      tweet = 'The Bucks had a dissapointing loss home against ' + bucksGame['vTeam'] + ' with a score of '+bucksGame['hScore']+' to ' +bucksGame['vScore'] + ' #FearTheDeer'
  elif bucksGame['status'] == 'Finished':
    if bucksGame['vScore'] > bucksGame['hScore'] and bucksGame['status'] == 'Finished':
      tweet = 'The Bucks came away with a nice win away against ' + bucksGame['hTeam'] + ' with a score of '+bucksGame['vScore']+' to ' +bucksGame['hScore'] + ' #FearTheDeer'
    elif bucksGame['hScore'] < bucksGame['vScore'] and bucksGame['status'] == 'Finished':
      tweet = 'The Bucks had a dissapointing loss away against ' + bucksGame['hTeam'] + ' with a score of '+bucksGame['vScore']+' to ' +bucksGame['hScore'] + ' #FearTheDeer'
  else:
    tweet = "Bucks are currently playing, I will update the score when the game ends" 
 
  api.update_status(tweet)


	

