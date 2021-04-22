# -*- coding: utf-8 -*-
"""


Zusammenfassung:
Die Regierungstweets werden über die Nutzernamen aus den Tweets extrahiert und einen Thema zugeordnet

env: py38

Auführen mit:
Das Skript muss über Spyder laufen

Eingabe: Alle Tweets aus final_tweets_de_clean und die ID zu TOpic zuordnung aus doc_id_by_topic

Ausgabe:
Die Ausgabe sind die Regierungstweets des gesamten Datensatzes

@author: Paul Drecker

"""
#Laden der Pakete
import os
import json
import pickle
import top2vec as top
import numpy as np

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

#Accountnamen der ausgewählten Regierungsaccounts
Reg_account = ['RegSprecher',
               'UlrikeDemmer',
               'HBraun', 
               'BMF_Bund', 
               'AA_SicherReisen', 
               'AuswaertigesAmt', 
               'BMWi_Bund', 
               'BMI_Bund', 
               'BMJV_Bund',
               'BMAS_Bund',
               'BMFSFJ',
               'BMVI',
               'bmel',
               'BMG_Bund',
               'bmu',
               'BMBF_Bund',
               'BMZ_Bund', 
               'OlafScholz', 
               'HeikoMaas',
               'peteraltmaier',
               'hubertus_heil',
               'AndiScheuer',
               'JuliaKloeckner',
               'akk',
               'jensspahn',
               'SvenjaSchulze68',
               'AnjaKarliczek','BMVg_Bundeswehr','rki_de','PEI_Germany','KfW']

# Hilfvariable zu durchsuchen aller Tweets
keywords = ["SARS_CoV", "covid", "corona", "coronavirus"]

# IDs und Tweets werden gespeichert
reg_id = []
reg_tweets = []
for keyword in keywords:   
    search = keyword
    directory =os.getcwd() + r"\Datengewinnung\final_tweets_de_clean\\"+search+".json"
    path= os.getcwd() + r"\Datengewinnung\final_tweets_de_clean\\"+search+".json"
    os.chdir(os.getcwd() + r"\Datengewinnung\final_tweets_de_clean\\"+search+".json")

    # Daten öffnen
    for file in os.listdir(directory):
        fh = open(os.path.join(path, file),'r')

        
    'Daten laden'
        with open(file, 'r', encoding='utf-8') as json_file:
            data_tweets = json.load(json_file)
        #Tweet-ID und Tweet_Text in die Liste geben
        for tweet in data_tweets:
            if tweet['user_screen_name'] in Reg_account:
                reg_tweets.append(tweet)
                reg_id.append(tweet['id'])
            

  
# ID zu Topic Zuordnung laden
with open(os.getcwd() + r"\Topicmodelfinal\doc_id_by_top2vec_300_30', 'rb') as fp:
    doc_id_by_topic = pickle.load(fp)      

# Jedem Regierungstweet ein Thema zuordnen
for tweet in reg_tweets:
    for j in range(0,len(doc_id_by_topic)):
        if tweet['id'] in doc_id_by_topic[j]:
            tweet['topic'] = j

# Kontrollieren ob ein Topic exestiert oder nicht - Wenn niht Rauschen
reg_tweets_new = []
for tweet in reg_tweets:
    try:
        print(tweet['topic'])
        reg_tweets_new.append(tweet)
    except KeyError:
        print('error')

with open(reg_tweets', "wb") as fp:
    pickle.dump(reg_tweets_new, fp)


             
        
        