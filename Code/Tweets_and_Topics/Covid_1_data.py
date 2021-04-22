# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 12:17:54 2020

Anmerkung: Viele der Datenbearbeitungschritte werden gesplitted durchgeführt um den Arbeitsspeicher nicht zu überlassen.
Entsprechend liegen die Daten oft in getrennten Files und Ordner vor. 
Soll der Code ausgführt werden ist ein Anlegen der  entsprechenden Ordnern unerlässlich 



Zusammenfassung:
In diesem Skript werden alle Links zu Tweets von 01.01.2020 bis zum 31.08.2020 runterladen die Wörter oder Teilwörter Corona, Covid oder SARS-CoV-2 enthielten.
Das Wort Coronavirus wurde mit geladen aber wird anschließen aus den Daten ausgeschlossen um Dopplungen zu vermeiden.

env: py38

Auführen mit:
Das Skript muss über cmd gestartet werden

Eingabe: - 

Ausgabe:
Die Ausgabe ist für jeden Tag eine Datei, die die Links zu den extrahierten Tweets enthält.

@author: Paul Drecker
"""

#Laden der Pakete
import os
from datetime import timedelta, date

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')




#Definieren des Ordners in dem die Links gspeichert werden
path =  os.getcwd() + r'\\Datengewinnung\\Tweetsid_scraped\\'


#Definieren der Zeitspanne
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
start_dt = date(2020, 1, 1)
end_dt = date(2020, 9,1)        
dates = []
for dt in daterange(start_dt, end_dt):
    dates.append(dt.strftime("%Y-%m-%d"))

i=100


# Scrapen der Links aller Tweets nach Suchwörtern
for i in range(0, len(dates)-1):
    os.system('snscrape twitter-search "corona lang:de until:'+dates[i+1]+' since:'+dates[i]+' -filter:replies" >'+path+'twitter-corona-' + dates[i])
    print(i)
    
    os.system('snscrape twitter-search "coronavirus lang:de until:'+dates[i+1]+' since:'+dates[i]+' -filter:replies" >'+path+'twitter-coronavirus-' + dates[i])
    os.system('snscrape twitter-search "covid lang:de until:'+dates[i+1]+' since:'+dates[i]+' -filter:replies" >'+path+'twitter-covid-' + dates[i])
    os.system('snscrape twitter-search "SARS-CoV-2 lang:de until:'+dates[i+1]+' since:'+dates[i]+' -filter:replies" >'+path+'twitter-SARS-CoV-2-' + dates[i])
    

