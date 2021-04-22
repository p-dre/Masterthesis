# -*- coding: utf-8 -*-
"""

Zusammenfassung:
Die Trainingstweets werden bereinigt

env: py38

Auführen mit:
Das Skript muss über Spyder laufen

Eingabe: Die Ausgabe von Sentiment_1_Twitter_api.py

Ausgabe:
Die Ausgabe ist der bereinigte Trainings- und Testdatensatz

@author: Paul Drecker

@author: Paul
"""

#Laden der Pakete
import os
import json
from sklearn.model_selection import train_test_split
import re
import pandas as pd
from pandas.io.json import json_normalize
from num2words import num2words
import numpy as np
from pandas import DataFrame
import tensorflow as tf
pd.options.display.max_colwidth = 30000000

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

Tweets = pd.read_json(os.getcwd() + r"\Datengewinnung\Trainingsdaten\Tweets_corpus_sentiment.json")

# Clean Funktion definieren
def text_cleaner(text, remove_digits=True):
    string = str(text)
    string = re.sub('Text', '', string)
    # Umlaute ersetzten
    string = re.sub('ä', 'ae', string)
    string = re.sub('ö', 'oe', string )
    string = re.sub('ü', 'ue', string )
    string = re.sub('ß', 'ss', string )
    # Hashtags werden bereingt
    string = re.sub(r"#","",string)
    # Der in den Daten enthaltende Tweet Nutzer wird gelöscht
    string = re.sub(r"Name: .* object$","", string)
    string = re.sub(r"@.*?\s+","",string)  
    # Absätze werden glöscht
    string = re.sub(r'\n', ' ',string) 
    string = re.sub(r'\\n', ' ',string) 
    string = re.sub(r"http\S+","", string)
    string = re.sub(r'\-', '',string) 
    string = re.sub(r'\b[a-zA-Z]{1,3}\b', '',string) 
    string = re.sub(r'\.', '',string) 
    string = re.sub(r'\,', '',string) 
    string = re.sub('\\\\', ' ',string)  
    string = re.sub(' +', ' ',string)  
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    string = re.sub(pattern, '', string)
    string = string.split()
    text_num = []
    # Zahlen werden ersetzt
    for elm in string:
        if elm.isnumeric() == True:
            text_num.append(num2words(elm, lang='de'))
        else:
            text_num.append(elm)
    del string
    text = ' '.join(text_num)
    text = text.lower()
    return text

# Die Bereinigung wird durchgeführt
Tweets_clean  = []
for i in range(0, len(Tweets)):
     Tweets_clean.append(text_cleaner(Tweets.loc[i,["Text"]]).split()) 
     print(i)

# Tweet Format wird bearbeitet
Tweets_final = np.c_[Tweets["ID"],Tweets_clean, Tweets["1"]]
Tweets_final = DataFrame (Tweets_final)
#Spalten werden umbenannt
Tweets_final.columns =["ID", "Text", "Senti"]
# Duplikate werden entfernt
Tweets_final = Tweets_final.drop_duplicates(subset='ID')

# Der Datensatz wird gemischt
Tweets_final = Tweets_final.sample(frac=1).reset_index(drop=True)
Tweets_final = Tweets_final[Tweets_final['Senti']!='Neutral'] 

# Der Datensatz wird in Trainings und Testdatensatz unterschieden - per zufall gezogen 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(Tweets_final['Text'],Tweets_final['Senti'], test_size=0.2, random_state=123,stratify=Tweets_final['Senti'], shuffle=True)
Tweets_clean_train =  pd.DataFrame({'y_train': y_train, 'x_train': X_train})
Tweets_clean_test =  pd.DataFrame({'y_test': y_test, 'x_test': X_test})

Daten werden als json gespeichert
Tweets_clean_train.to_json(os.getcwd() + r"\Datengewinnung\Trainingsdaten\Tweets_final_corpus_sentiment_clean_train.json")
Tweets_clean_test.to_json(os.getcwd() + r"\Datengewinnung\Trainingsdaten\Tweets_final_corpus_sentiment_clean_test.json")




