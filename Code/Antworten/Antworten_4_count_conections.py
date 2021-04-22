# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:04:44 2020

Zusammenfassung:
Für das Ausgewählte Thema werden die ANzahl der Verbindugen aufgelistet und gezählt. 
Für jede mögliche Verbindung werden somit die Gewichte für das spätere Netzwerk definiert

env: py38

Auführen mit:
Das Skript muss über Spyder laufen

Eingabe: Die Ausgabe von Antworten_3_get_antworten.py

Ausgabe: Ausgabe sind alle Antworten in einem Thema


@author: Paul Drecker

"""
#Laden der Pakete
import os
import pandas as pd
import numpy as np
import json


# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

# Thema definieren 
topic = 'Topic_76'

# Ordner der Inputdaten festlegen
directory =os.getcwd() + r'\Datengewinnung\Antworten_nach_topic_tweets\\'+topic
path= os.getcwd() + r'\Datengewinnung\Antworten_nach_topic_tweets\\'+topic

#Leeres Dataframe definieren
connections = pd.DataFrame ( columns = ['From_To','num'])
#Antwort öffnen und in dem Dataframe speichern
for file in os.listdir(directory):
    with open( os.getcwd() + r'\Datengewinnung\Antworten_nach_topic_tweets\\'+topic + '\\' + file, 'r', encoding='utf-8') as f:
        tweet = json.load(f)
        # Speicher von wenn die Antwort an wenn ging
        connections = connections.append( {'From_To': str(tweet['user_screen_name']) + '_split' +str( tweet['in_reply_to_screen_name']),'text': tweet['text']},ignore_index=True)

#Datenbearbeitungschritte
text = connections['text']
connections = pd.DataFrame(connections['From_To'].str.split('_split',1).tolist(),
                         columns = ['Source','Target'])        
connections['text'] = text
connections['label'] = 0
connections['Weight'] = ''
# Gewichte und Label für alle Verbindungen auf eins setzen
for i in range(0,len(connections)):
    connections['Label'] = 1
    connections['Weight'] = 1

# Anzahl der Verbindugen zählen
Count = connections.groupby(['Source','Target'], as_index=False).agg({"Label": "mean", "Weight":"sum"})
Source = pd.DataFrame(set(Count['Source'].append(Count['Target'], ignore_index=True)),columns = ['Source'])

# Regierungssaccounts festlegen
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
               'AnjaKarliczek','osterki']

# Source Labeln wenn es ein Regierungsaccount ist
Source['Label'] = ''
for i in range(0,len(Source)):
    if Source['Source'][i] in Reg_account:
        Source['Label'][i] =1
    else:
        Source['Label'][i] =0
        
# Speicher von Knoten und Verbindugen als csv
Count.to_csv(os.getcwd() + r'\Datengewinnung\Netzwerke\\Edges_'+ topic +'.csv', index=False)
Source.to_csv(os.getcwd() + r'\Datengewinnung\Netzwerke\Source.csv_'+ topic +'.csv', index=False)





