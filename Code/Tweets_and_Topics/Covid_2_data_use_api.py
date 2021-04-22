# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:26:04 2020

Zusammenfassung:
In diesem Skript werden alle Tweets von 01.01.2020 bis zum 31.08.2020 runterladen. Auf Basis der voher gesamelten Links
Die Tweets werden Nach Suchwort zusammengefasst

env: py38

Auführen mit:
Das Skript muss über Spyder ausgeführt werden

Eingabe: Die Ausgabe von 1_Covid_data.py

Ausgabe:
Die Ausgabe sind vier .json die alle gesammelten Tweets und die zuzüglichen Informationen enthalten

@author: Paul Drecker

"""

#Laden der Pakete
import tweepy
import pandas as pd
import numpy as np
import time
import json
from datetime import datetime
from dateutil import tz
import pytz
import re
import os


# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')





# Fetslegen der Zugangsadaten zum Twitter API
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Verbinden mit dem API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Überpüfen ob eine Verbindung besteht
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")




#Festlegen des Ordners in dem er output aus 1_Covid_data.py liegt

os.chdir(os.getcwd() +  r'\Datengewinnung')
directory =os.getcwd() + r'\Tweetsid_scraped'
path= os.getcwd() + r'\Tweetsid_scraped'





# Festlegen der Zeitzone um später die Tweets erfassen zu können
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Europe/Berlin')

# Erstellen von Listen um die URLs in diesen zu Speichern
SARS_CoV = []
corona = []
covid = []
coronavirus = []




# Für jedes File im Ordner überprüfen welches Suchwort verwendet wurde und anschließend in der entsprechend Liste speichern
# Gleichzeitig wird aus dem Tweet Link die Tweet-ID extrahiert
urls =[]
for file in os.listdir(directory):
    fh = open(os.path.join(path, file),'r')
    
   
    tweet_id = []
    for line in fh:
        urls.append(line)
        #Aus jedem Link wird nur die ID gespeichert
        if  re.search('twitter-(.*)-2020', file).group(1) == 'SARS-CoV-2':
            SARS_CoV.append(line.split('/')[-1].strip() ) 
        elif re.search('twitter-(.*)-2020', file).group(1) == 'corona':
            corona.append(line.split('/')[-1].strip() )
        elif re.search('twitter-(.*)-2020', file).group(1) == 'coronavirus':
            coronavirus.append(line.split('/')[-1].strip() )
        elif re.search('twitter-(.*)-2020', file).group(1) == 'covid':
            covid.append(line.split('/')[-1].strip() )
        tweet_id.append(line.split('/')[-1].strip() ) 
        
        

    
 
# Hier wird für jedes Suchwort die IDS in Listen von 100 unterteilt.
# ID-Listen können in tweepy deutlich schneller abgefragt werden als einzelne Tweets
for j in range(4):
    #Jedes Suchwort wird einzeln abgefragt
    if j == 0:
        id_list = [SARS_CoV[x:x+100] for x in range(0, len(SARS_CoV), 100)]
    elif j == 1:
        id_list = [corona[x:x+100] for x in range(0, len(corona), 100)]
    elif j == 2:
        id_list = [coronavirus[x:x+100] for x in range(0, len(coronavirus), 100)]
    elif j ==3:
        id_list = [covid[x:x+100] for x in range(0, len(covid), 100)]
        
        
    # Liste wird erstellt zum speichern der Tweets    
    all_tweets = []   
    for i in range(0, len(id_list)) :
            # 900 Sekunden Pause nach 300 Abfragen
            if ((i-1)/300).is_integer() and i > 1:
             time.sleep(900)
            
            
            # Id-Liste über das Twitter API abfragen
            tweets = api.statuses_lookup(list(id_list[i]))
            print(i)
            
            # Speichern der Informationen aller Tweets in der all_tweets Liste
            all_tweets.extend([dict(
                        # Zeit und Datum werden in Europäische Zeit umgewandelt und gespeichert
                        date = tweet.created_at.replace(tzinfo=from_zone).astimezone(to_zone).date().strftime("%Y-%m-%d"),
                        time = tweet.created_at.replace(tzinfo=from_zone).astimezone(to_zone).time().strftime("%H:%M:%S"),
                        id = tweet.id,
                        text = tweet.text,
                        in_reply_to_status_id = tweet.in_reply_to_status_id,
                        user_id = tweet.user.id, 
                        username = tweet.user.name,
                        user_screen_name =tweet.user.screen_name,
                        userlocation = tweet.user.location,
                        user_verified = tweet.user.verified,
                        user_followers = tweet.user.followers_count,
                        user_firends = tweet.user.friends_count,
                        user_likes_in_lifetime = tweet.user.favourites_count,
                        user_number_tweets = tweet.user.statuses_count,
                        user_created_at = tweet.user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                        retweet_count = tweet.retweet_count, 
                        favorite_count = tweet.favorite_count, 
                        # User Mention wir sondern muss mit regex aus den zusätlichen Information extrahiert werden
                        user_mentions = str(re.search("'user_mentions': \[(.*)\]\,",str(tweet.entities)).group(1)),
                        lang = tweet.lang) for tweet in tweets])
                    
            

    # Ordner in dem die Tweets Gespeichert werden
    os.chdir(os.getcwd() + r'\final_tweets_de')
    
    # Anderer Ordnername für jedes Suchwort
    if j == 0:
        with open('SARS_CoV.json', 'w', encoding='utf-8') as f:
            json.dump(all_tweets, f, ensure_ascii=False, indent=4)
    elif j == 1:
        with open('corona.json', 'w', encoding='utf-8') as f:
            json.dump(all_tweets, f, ensure_ascii=False, indent=4)
    elif j == 2:
        with open('coronavirus.json', 'w', encoding='utf-8') as f:
            json.dump(all_tweets, f, ensure_ascii=False, indent=4)
    elif j ==3:
        with open('covid.json', 'w', encoding='utf-8') as f:
            json.dump(all_tweets, f, ensure_ascii=False, indent=4)
        

    









    
    
    
    
    
    
    
    
    
    
    
    
    
    