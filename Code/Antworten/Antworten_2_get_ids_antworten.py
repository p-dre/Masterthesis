# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:49:46 2020
Zusammenfassung:
Ids der Antworten werden gewonnen. Alle Antworten auf einen User werden fünf Tage nach einem Tweet geladen.
Ordner path muss unter os.system angepasst werden
env: py38

Auführen mit:
Das Skript muss über cmd laufen

Eingabe: Die Ausgabe von Antworten_1_tweet_to_topic.py

Ausgabe: Für jeden Tweet eine liste von möglichen Antworten als Link


@author: Paul Drecker

"""

import multiprocessing as mp
import os
import json
import datetime
from dateutil.relativedelta import relativedelta
import re
import time
import pickle
import random


# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

# Topic eintragen welches gescraped werden soll
Topics_wanted = ['Topic_76']

with open(os.getcwd() + r'\Topicmodelfinal\\'+ 'doc_id_by_top2vec_300_30', 'rb') as fp:
    documents_ids = pickle.load(fp)
    
# Definieren von Funktion zum scrapen der ID fünf Tage nach Veröffentlichung von Tweets
def get_id(file_list):
    # Wenn sleep stopper in den Daten 60 Sekunden Pause
    if file_list == 'sleep':
        time.sleep(60)
        print('sleep')
    else:
        # Wenn keine Pause dann Twee Link laden
        with open(file_list, 'rb') as fp:
            tweet = pickle.load(fp)
         

        try:
            # Accountname zu suche festlegen
            account = tweet['user_screen_name']
            # Zeit festlegen in der gesucht werden soll - hier fünf Tage noch Tweet Veröffentlichung
            created = datetime.datetime.strptime(tweet['date'], '%Y-%m-%d').date()
            until = created + relativedelta(days=5)
            id = tweet['id']
            # Topic aus file Namen speichern
            topic = re.search(r'Tweets_by_topic\\(.*)\\',file_list).group(1) 
            filename = 'tweet_id_' +str(id)+ '_' + 'user_id_' + str(tweet['user_id'])+'_' + 'user_screen_name' + str(tweet['user_screen_name'])
            # Antworten auf User im festgelegten Zeitraum scrapen
            os.system('snscrape twitter-search "(to:'+account+') since:'+created.strftime("%Y-%m-%d")+' until:'+until.strftime("%Y-%m-%d")+' filter:replies" >C:\\Users\\Paul\\Documents\\Uni\\Masterarbeit\\Final_Code\\Masterarbeit\\Datengewinnung\\Antworten_nach_Topic\\'+topic+'\\'+filename)
            
        except:
            # Wenn Fehler dann Meldung ausgeben
            Exception:logging.exception("f(%r) failed" % (args,))
            
# Multiprocessing - 3-4 Kerne werden nicht geblockt
NUM_CPUS = 1
def mp_handler(file_list):
    pool = mp.Pool(NUM_CPUS) 
    pool.map(get_id, file_list)

if __name__ == "__main__":
    # Tweets werden geladen und IDs auf die Kerne aufgeteilt
    directory_folder = os.getcwd() + r'\Datengewinnung\Tweets_by_topic'
    folder_list = [x[0] for x in os.walk(directory_folder)]
    del(folder_list[0])
    count = 0
    file_list = []
    for folder in folder_list:
        # Nur speichern wenn im ausgewählten Topic
        if re.search(r'Tweets_by_topic\\(.*)',folder).group(1) in Topics_wanted:
            # Sleep stopper in die Daten einbauen
            for file in os.listdir(folder):
                count=count+1
                if (count/300).is_integer():
                   file_list.append('sleep')
                else:
                    file_list.append(os.path.join(folder, file))
    print('finish folder')
    # Multiprocessing starten
    start = time.time() 
    mp_handler(file_list)
    end = time.time()
    print(end - start)
        