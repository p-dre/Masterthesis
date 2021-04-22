# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:17:16 2021

Zusammenfassung:
Berechnung der Wordcloud und extrahiern der wirtschaft, schliessung und hilfe themen

env: top2vec_final

Auführen mit:
Das Skript muss über spyder laufen

Eingabe: Die Ausgabe von Covid_6_top2vec.py

Ausgabe: Wordclouds


@author: Paul Drecker

"""
#Laden der Pakete
import top2vec as top
import os

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

#Top2vec laden
model = top.Top2Vec.load(os.getcwd() + r'\Topicmodelfinal\\top2vec_300_30')

#  Übersicht über das Modell erlangen
topic_words, word_scores, topic_nums = model.get_topics()

#for i in range(0, len(topic_nums)):
#    model.generate_topic_wordcloud(i,background_color= 'white')



# Themen nach Abstand zum Wortvektor bestimmen und Wordclouds erstellen
topic_words, word_scores, topic_scores, topic_nums = model.search_topics(keywords=["wirtschaft"], num_topics=5)
for i in range(0,5):
    model.generate_topic_wordcloud(topic_nums[i],background_color= 'white')
    
topic_words, word_scores, topic_scores, topic_nums = model.search_topics(keywords=["schliessungen"], num_topics=5)
for i in range(0,5):
    model.generate_topic_wordcloud(topic_nums[i],background_color= 'white')
    
topic_words, word_scores, topic_scores, topic_nums = model.search_topics(keywords=["hilfen"], num_topics=5)
for i in range(0,5):
    model.generate_topic_wordcloud(topic_nums[i],background_color= 'white')