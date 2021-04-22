# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:09:59 2020

Zusammenfassung:
Die Covid-19 Tweets werden den Themen zugeordnet
Für jedes Thema wird ein ordner erstellt un ddie Tweets darin gespeichert

env: py38

Auführen mit:
Das Skript muss über spyder laufen

Eingabe: Die Ausgabe von Covid_6_top2vec.py

Ausgabe: Alle Tweets werden in Ordner pro Thema geordnet


@author: Paul Drecker

"""
import os
import pickle
import json

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

with open(os.getcwd() + r'\Topicmodelfinal\\'+ 'doc_id_by_top2vec_300_30', 'rb') as fp:
    documents_ids = pickle.load(fp)
    
# Ordner zum speichern der Tweets erstellt
#os.chdir(os.getcwd() + r'\Datengewinnung\Tweets_by_topic')
#for j in range(len(documents_ids)):
#    os.makedirs("Topic_"+str(j))
    

# Directory wird gesetzt
directory =os.getcwd() + r'\Datengewinnung\final_tweets_de'
path=  os.getcwd() + r'\Datengewinnung\final_tweets_de'
    

# Für jedes Suchwort wird die Datei mit allen Tweets geladen
for file in os.listdir(directory):
   

    fh = open(os.path.join(path, file),'r')
    print(file)
    
    
    # Tweets werden geladen
    with open(os.getcwd() + r'\Datengewinnung\final_tweets_de\\' + file, 'r', encoding='utf-8') as json_file:
        data_tweets = json.load(json_file)
    # Tweets werden gesplitted und nach und nach bearbeitet
    id_list = [data_tweets[x:x+1000] for x in range(0, len(data_tweets), 1000)]
    for i in range(len(id_list)):
        # Jede Tweet zu Thema kombination wird betrachtet
        for tweet in id_list[i]:
            for j in range(len(documents_ids)):
                #Es wird kontrolliert ob Tweet in dem Thema ist, wenn ja dann wird er in dem Ordner gespeichert
                if (tweet['id'] in documents_ids[j]):
                    #Tweets werden gespeichert
                    with open(os.getcwd() + r'\\Datengewinnung\\Tweets_by_topic\\'+"Topic_"+str(j) + "\\" +str(+tweet['id']), 'wb') as fp:
                        pickle.dump(tweet, fp)
                    
                    
                    
            