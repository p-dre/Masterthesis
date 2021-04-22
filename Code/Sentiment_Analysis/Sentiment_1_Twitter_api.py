# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:40:37 2020

Zusammenfassung: Der Trainingsdatensatz wird als Kombination von Tweet-IDs und Labeln bereitgestellt
Über die IDs werden die Tweets geladen

env: py38

Auführen mit:
Das Skript muss über Spyder gestartet werden

Eingabe: German_Twitter_sentiment.csv

Ausgabe:
Die Ausgabe ist eine json mit den zur ID gehörigen Tweets

@author: Paul Drecker
"""
#Laden der Pakete
import csv
import tweepy
import pandas as pd
import numpy as np
import time

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

# Daten laden und nur ID und Text auswählen
search_info = pd.read_csv(os.getcwd() + r'\Datenbereitstellung\German_Twitter_sentiment.csv',encoding='utf-8-sig', header=None)
sentiment_id = search_info.loc[:,0]

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

# Leeren  Pandas Dataframe erstellen
Tweets = pd.DataFrame(columns=['ID', 'Text'])

# ID Liste erstellen
id_list = list(sentiment_id)

# ID Liste in 100 IDs pro Liste splitten 
id_list = np.array_split(id_list, len(id_list)/100)

# Tweets von Twitter abfragen
for i in range(0, len(id_list))  :
     tweets = api.statuses_lookup(list(id_list[i]),  tweet_mode='extended')
     for tweet in tweets:
         # Tweet ID und Text runterladen
         Tweets = Tweets.append({'ID': tweet.id, 'Text': tweet.full_text}, ignore_index=True)
     print(i)
     # Pasuieren anch 300 Abfragen für 900 Sekunden
     if ((i)/300).is_integer() and i > 1:
         time.sleep(900)
 
    
 # Daten zusammenführen und Spalten umbenenen
search_info = search_info.loc[1:]   
search_info[[0]] = search_info[[0]].astype(str)
Tweets["ID"] = Tweets["ID"].astype(str)
Tweets = pd.merge(Tweets, search_info[[0,1]], how='left', left_on='ID', right_on=0)
Tweets = Tweets[["ID", "Text", 1]]

# Daten als Json speichern
Tweets.to_json(os.getcwd() + r"\Datengewinnung\Trainingsdaten\Tweets_corpus_sentiment.json")

