
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
        timeOfDay =  str(datetime.now())[11:16:1]     
        if timeOfDay == '23:00':
            bucksGame = get_Bucks_game()
            send_tweet(bucksGame)
            time.sleep(45)
        since_id = check_mentions(since_id) 
        time.sleep(2)
   
if __name__ == "__main__":
    main()