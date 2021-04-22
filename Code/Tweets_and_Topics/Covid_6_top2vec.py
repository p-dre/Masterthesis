# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:40:55 2020

Zusammenfassung:
Topic Model schätzen - jedes Modell  muss einzelen geschätzt werden aufgrund des hohen Verbrauch des Arbeitsspeichers
Zum Durchlaufen des Modells sollte wenigstens 120 GB Arbeitsspeicher zu verfügung stehen
Die Mindesclustergröße muss manuell im package angepasst werden.

env: top2vec_final

Auführen mit:
Das Skript muss über spyder laufen

Eingabe: Die Ausgabe von Covid_5_data_merge

Ausgabe:
Die Ausgabe ist ein top2vec-modell undd eine Liste mit ID zu Topic Zuordnung

@author: Paul Drecker

"""


#Laden der Pakete
import pickle
import pandas as pd
import top2vec as top
import sklearn
import numpy as np
import pickle
import os

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

# Hier ändern wie oft ein Wort mindestens vorkommen muss um berücksichtigt zu werden - In der Masterarbeit wurden 30 und 50 verwendet
# Mindestclustergröße muss in Top2vec.py des package angepasst werden
min_count = 30
modelname = 'top2vec_300' +'_'+ str(min_count)

with open(os.getcwd() +   r"\Datengewinnung\final_tweets_de_clean\documents_text.txt", "rb") as fp:
    documents_text = pickle.load( fp)  
    
with open(os.getcwd() + r"\Datengewinnung\final_tweets_de_clean\documents_id.txt", "rb") as fp:
    documents_id = pickle.load(  fp)  
    
document = pd.DataFrame({'id': documents_id, 'text': documents_text})

document = document.drop_duplicates(subset='text')



model = top.Top2Vec(documents=document['text'], 
            speed="learn", workers=6,
            min_count=min_count,
            keep_documents=False, 
            document_ids=document['id'])

model.save(os.getcwd() + r'\Topicmodelfinal\\' + modelname)



# Extrahieren der IDs und zugehörigen Themen
topic_words, word_scores, topic_nums = model.get_topics()
doc_by_topic = pd.DataFrame({'id': model.document_ids, 'topic': model.get_documents_topics(model.document_ids)[0]})

# Ids nach Themen auftrennen
doc_topic =[]
for j in range(0, model.get_num_topics()):
    print(j)
    topic =  np.array(doc_by_topic[doc_by_topic['topic']== j]['id'] )
    doc_topic.append(topic)
    
# Liste von den ID listen pro Thema speichern    
with open(os.getcwd() + r'\Topicmodelfinal\\'+ 'doc_id_by_' + modelname, "wb") as fp:
    pickle.dump(doc_topic, fp)      


    
    
    