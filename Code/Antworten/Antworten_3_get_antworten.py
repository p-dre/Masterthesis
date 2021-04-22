# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:09:09 2020

Zusammenfassung:
Für jeden Tweet wird die Liste der Antworten untersucht ob die Tweet reply_to_status_id der Tweet ID entspricht
Dafür werden die Antworten gescraped und dann überprüft - Stimmen reply_to_status_id mit Tweet ID bereinander dann wird er Tweet gespeichert

env: py38

Auführen mit:
Das Skript muss über cmd laufen

Eingabe: Die Ausgabe von Antworten_2_tweet_to_topic.py

Ausgabe: Ausgabe sind alle Antworten in einem Thema


@author: Paul Drecker

"""
#Laden der Pakete
import json
import os
import tweepy
from datetime import datetime
from dateutil import tz
import re
import time
import pickle


# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

# Topic eintragen welches gescraped werden soll
Topics_wanted = ['Topic_76']

# Ordner Erstellen in dem die Antworten gespeichert werden
#with open('doc_id_by_topic_300_30', 'rb') as fp:
#    documents_ids = pickle.load(fp)


#os.chdir(os.getcwd() + r'\Datengewinnung\Antworten_nach_topic_tweets')
#for j in range(len(documents_ids)):
#       os.makedirs("Topic_"+str(j))

# Festlegen der Zugangsadaten zum Twitter API
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

# Festlegen der Zeitzone um später die Tweets erfassen zu können
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Europe/Berlin')



count_request =[]
#count_request.append(6485)
for topic in Topics_wanted:

    directory =os.getcwd() + r'\Datengewinnung\Antworten_nach_Topic\\'+topic
    path= os.getcwd() + r'\Datengewinnung\Antworten_nach_Topic\\'+topic
    antwort_id = []
    org_tweet_id = []
    #Antworten-IDs werden in einer Liste gespeichert
    for file in os.listdir(directory):
        org_tweet_id.append(re.search(r'tweet_id_(.*)_user_id',str(file)).group(1))
        fh = open(os.path.join(path, file),'r')
        for line in fh:
            antwort_id.append(re.search(r'status/(.*)',str(line)).group(1) )
            
     # Liste wird in Listen mit jeweils 100 IDs unterteilt
    id_list = [antwort_id[x:x+100] for x in range(0, len(antwort_id), 100)]
    # Wenn Liste Leer dann nächste Liste
    if id_list == []:
        pass
    else:
        for i in range(0,len(id_list)):
            # Zähler 
            count_request.append(1)
            # Loop pausieren wenn 300 Listen von jeweils 100 IDs abgefragt wurden
            if ((sum(count_request))/300).is_integer():
                time.sleep(900)
                
            id_list[i]
            #Abfragen er ID Liste
            tweets = api.statuses_lookup(list(id_list[i]),  tweet_mode='extended')
            print(str(sum(count_request)) + "_"+ str(topic))
            for tweet in tweets:
                # Für jeden Tweet kontrollieren ob die reply_to_status_id der Tweet ID entspricht
               if str(tweet.in_reply_to_status_id) in org_tweet_id:
                   print(True)
                   Tweet_save= dict(
                           # Zeit und Datum werden in Europäische Zeit umgewandelt und gespeichert
                                date = tweet.created_at.replace(tzinfo=from_zone).astimezone(to_zone).date().strftime("%Y-%m-%d"),
                                time = tweet.created_at.replace(tzinfo=from_zone).astimezone(to_zone).time().strftime("%H:%M:%S"),
                                id = tweet.id,
                                text = tweet.full_text,
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
                                in_reply_to_screen_name = tweet.in_reply_to_screen_name,
                                # User Mention wir sondern muss mit regex aus den zusätlichen Information extrahiert werden
                                user_mentions = str(re.search("'user_mentions': \[(.*)\]\,",str(tweet.entities)).group(1)),
                                lang = tweet.lang) 
                   Speichern der Tweets
                   with open(os.getcwd() +r'\Datengewinnung\Antworten_nach_topic_tweets\\'+str(topic)+'\\'+ str(Tweet_save['id'])+'.json', 'w', encoding='utf-8') as f:
                        json.dump(Tweet_save, f, ensure_ascii=False, indent=4)
 
        
        
    
    






















