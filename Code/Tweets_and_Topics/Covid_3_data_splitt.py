# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:08:05 2020

Zusammenfassung:
Die Daten werden in neue files in Größe von 100 tweets gespllited und gespeichert
Das Vorgehen wurde gewählt, da es in späteren Bearbeitungsschritten zu einer Überlastung eines Arbeitsspeichers <= 16 GB kommt.

env: py38

Auführen mit:
Das Skript muss über Spyder ausgeführt werden

Eingabe: Die Ausgabe von 2_Covid_data_use_api.py

Ausgabe:
Die Ausgabe sind jsons mit jeweils 1000 Tweets

@author: Paul Drecker
"""
#Laden der Pakete
import os
import json
import re



# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')



# Input path festlegen

directory =os.getcwd() + r'\Datengewinnung\final_tweets_de'
path= os.getcwd() +r'\Datengewinnung\final_tweets_de'
    

# Die vier files werden einzelen geladen, gesplitted und wieder gespeichert
for file in os.listdir(directory):
    #os.chdir(os.getcwd() + r'\Datengewinnung\final_tweets_de')
    
   
    fh = open(os.path.join(path, file),'r')
    print(file)
    
    
    # Laden des files
    with open(os.getcwd() + r'\Datengewinnung\final_tweets_de\\'+ file, 'r', encoding='utf-8') as json_file:
        data_tweets = json.load(json_file)
    
    # Splitten in kleinere files
    id_list = [data_tweets[x:x+1000] for x in range(0, len(data_tweets), 1000)]
    
    # File für file Speichern - ordner wo gespeichert werden soll muss hier angepasst werden
    for i in range(len(id_list)):
        
        with open(os.getcwd() + r'\Datengewinnung\final_tweets_de_splitted\\'+ file +'\\' + file + '_' + str(i) + '.json', 'w', encoding='utf-8') as f:
                json.dump(id_list[i], f, ensure_ascii=False, indent=4)
    
    