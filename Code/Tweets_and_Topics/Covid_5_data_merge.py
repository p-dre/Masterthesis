# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 23:50:41 2020

Zusammenfassung:
Zusammenfassen aller bereingten Tweets und Ids - durch  nicht berücksichtige von anderen Daten deutlich kleiner

env: py38

Auführen mit:
Das Skript muss über spyder

Eingabe: Die Ausgabe von Covid_4_data_clean_corona.py, Covid_4_data_clean_covid.py, Covid_4_data_clean_coronavirus.py, Covid_4_data_clean_SARS_CoV.py

Ausgabe:
Die Ausgabe sind zwei .txt - Einmal mit den Texten und einmal mit IDs

@author: Paul Drecker

"""


import os
import json
import time
import multiprocessing as mp

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

# Leere Listen erstellen
documents_text = []
documents_id = []
documents= dict()
# Keyword erstellen um über iese zu Iterieren
keywords = ["SARS_CoV.json","covid.json","corona.json","coronavirus.json"]
# Funktion erstellen um doppelte ids zu löschen
def entries_remove(ids, tdict):
    for key in ids:
        if key in tdict:
            del tdict[key]

delete=[]
for keyword in keywords:    
    search = keyword
    directory = os.getcwd() + r'\Datengewinnung\final_tweets_de_clean\\' + search
    path= os.getcwd() + r'\Datengewinnung\final_tweets_de_clean\\' + search
    # Tweets öffnen und Text und Id speichern
    for file in os.listdir(directory):
        fh = open(os.path.join(path, file),'r')
         # Öffnen der Tweets
        with open(path + '\\' +file, 'r', encoding='utf-8') as f:
            tweets = json.load(f)
        # IDs,Text und Datum speichern
        for tweet in tweets:
            documents[tweet["id"]] = dict(id =tweet["id"], text = tweet["text"], date = tweet["date"])

# Löschen von Texten kleiner als drei Wörter - Filter auf  Daten    
for tweet in documents:
    if documents[tweet]["date"]  >= "2020-09-01" or len(documents[tweet]["text"].split()) <= 3:
        delete.append(tweet)

# Dopplungen löschen
entries_remove(delete, documents)
                        
# ID und Text speichern
for key in documents:
    documents_id.append(documents[key]["id"])
    documents_text.append(documents[key]["text"])
            


import pickle
with open(os.getcwd() + r'\Datengewinnung\final_tweets_de_clean\\documents_text.txt', "wb") as fp:
    pickle.dump(documents_text, fp)  
    
with open(os.getcwd() + r'\Datengewinnung\final_tweets_de_clean\\documents_id.txt', "wb") as fp:
    pickle.dump( documents_id, fp)  










