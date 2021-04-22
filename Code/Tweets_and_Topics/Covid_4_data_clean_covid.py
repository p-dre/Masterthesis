# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:08:12 2020

Zusammenfassung:
Die Tweets werden bereingt 

env: py38

Auführen mit:
Das Skript muss über cmd

Eingabe: Die Ausgabe von 3_Covid_data_splitt.py

Ausgabe:
Die Ausgabe sind jsons beringten Tweets für das Suchwort Covid

@author: Paul Drecker

@author: Paul
"""



#Laden der Pakete
import os
import json
import time
import multiprocessing as mp
import re
from num2words import num2words

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')


# Definieren der text_cleaner Funktion
def text_cleaner(text, remove_digits=True):
    string = str(text)
    #Umlate werden ersetzt
    string = re.sub('ä', 'ae', string)
    string = re.sub('ö', 'oe', string )
    string = re.sub('ü', 'ue', string )
    string = re.sub('ß', 'ss', string )
    # Hastags werden bereingt
    string = re.sub(r"#","",string)
    # Der in den Daten enthaltende Tweet Nutzer wird gelöscht
    string = re.sub(r"Name: .* object$","", string)
    # Überflüssige Satzzeichen werden entfernt
    string = re.sub(r"@.*?\s+","",string) 
    # Absätze werden glöscht
    string = re.sub(r'\n', ' ',string) 
    string = re.sub(r'\\n', ' ',string) 
    # URLs werden gelöscht
    string = re.sub(r"http\S+","", string)
    string = re.sub(r'\-', ' ',string) 
    string = re.sub(r'\b[a-zA-Z]{1,3}\b', '',string) 
    string = re.sub(r'\.', '',string) 
    string = re.sub(r'\,', '',string) 
    # Rauschen welches sich in vorherigen Durchläufen herausstellte wird bereingt
    string = re.sub('ellqmycze', '',string)  
    string = re.sub('ellqmhg', '',string)  
    string = re.sub('ffne', '',string) 
    string = re.sub('www', '',string)  
    string = re.sub('emic', '',string)  
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

# Der Bereinigungsprozess wird definiert    
def clean(file_list):
 
    # Tweets werden geladen
    with open(os.getcwd() + r'\Datengewinnung\final_tweets_de_splitted\covid.json'+'\\'+ file_list, 'r', encoding='utf-8') as f:
            tweets = json.load(f)
    # Für jeden Tweet wird die text_clean funktion verwendet
    for i in range(len(tweets)):
        tweets[i]["text"] = text_cleaner(tweets[i]["text"])
  
    #Tweets werden gespeichert   - Ordner zum Speicher muss hier festgelegt werden
    with open(os.getcwd() + r"\Datengewinnung\final_tweets_de_clean\\covid.json\\"+ re.sub(r'json',"",file_list), 'w', encoding='utf-8') as f:
            json.dump( tweets, f, ensure_ascii=False, indent=4)
    
    
    
    
# Anzahl an Kernen die genutzt werden soll            
NUM_CPUS = 4

# Definieren des multiprocessing
def mp_handler(file_list):
    pool = mp.Pool(NUM_CPUS) 
    pool.map(clean, file_list)

start = time.time()
# Die Prozesse werden in der Ausführung priorisiert - in Windows notwendig da Ansonsten andere Prozesse den Ablauf unterbrechen
if __name__ == "__main__":

    # Festlegend des Inputs
   
    directory = os.getcwd() + r'\Datengewinnung\final_tweets_de_splitted\covid.json'
    path= os.getcwd() + r'\Datengewinnung\final_tweets_de_splitted\\covid.json'
  
    # Laden der files 
    file_list =[]
    for file in os.listdir(directory):
        fh = open(os.path.join(path, file),'r')
        file_list.append(file)
    
    # Files werden aufgteilt und den Kernen zugewiesen
    mp_handler(file_list)
        
end = time.time()
print(end - start)
time = end - start
#Speichern der der Zeit
with open(os.getcwd() + r"\Datengewinnung\final_tweets_de_clean\time_corona", 'w', encoding='utf-8') as f:
            json.dump( time, f, ensure_ascii=False, indent=4)
    

        
        
        