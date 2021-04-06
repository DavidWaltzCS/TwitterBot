
import os
import re
import sys
from datetime import datetime
import time
from twitter import send_tweet
from basketball_scores import get_games, get_Bucks_game
from live_bucks_tweeting import check_mentions

def main():
    since_id = 1
    while True:
        timeOfDay =  str(datetime.now())
        print(timeOfDay)
        timeOfDay = timeOfDay[11:16:1]      
        if timeOfDay == '23:00' and run == 0:
            games = get_games()
            bucksGame = get_Bucks_game(games)
            send_tweet(bucksGame)
            run = 1
            time.sleep(45)
        since_id = check_mentions(since_id) 
        time.sleep(15)
   
if __name__ == "__main__":
    main()