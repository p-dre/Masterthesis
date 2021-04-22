# -*- coding: utf-8 -*-
"""
Created on Wen Nov 25 22:53:41 2020

Zusammenfassung:
Die vier Top2vec Modelle werden geladen und jeweils der silhouette_score berechnet

env: top2vec_final

Auführen mit:
Das Skript muss über spyder laufen

Eingabe: Die Ausgabe von Covid_6_top2vec.py

Ausgabe:


@author: Paul Drecker

"""
#Laden der Pakete
import pickle
import pandas as pd
import top2vec as top
import sklearn
import numpy as np
import pickle
import random
import os
from sklearn import metrics
from sklearn.metrics import pairwise_distances


# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')



#model = top.Top2Vec.load(r'D:\Uni\Masterarbeit\Topicmodelfinal\Top2vec_model_min_count30_cluster_300')
model_300_30 = top.Top2Vec.load(os.getcwd() + r'\Topicmodelfinal\\top2vec_300_30')
model_300_50 = top.Top2Vec.load(os.getcwd() + r'\Topicmodelfinal\\top2vec_300_50')
model_200_50 = top.Top2Vec.load(os.getcwd() + r'\Topicmodelfinal\\top2vec_200_50')
model_200_30 = top.Top2Vec.load(os.getcwd() + r'\Topicmodelfinal\\top2vec_200_30')



metric_300_30 = metrics.silhouette_score(model_300_30._get_document_vectors(False),  model_300_30.get_documents_topics(model_300_30.document_ids)[0], metric='euclidean')

metric_300_50 = metrics.silhouette_score(model_300_50._get_document_vectors(False),  model_300_50.get_documents_topics(model_300_50.document_ids)[0], metric='euclidean')

metric_200_50 = metrics.silhouette_score(model_200_50._get_document_vectors(False),  model_200_50.get_documents_topics(model_200_50.document_ids)[0], metric='euclidean')

metric_200_30 = metrics.silhouette_score(model_200_30._get_document_vectors(False),  model_200_30.get_documents_topics(model_200_30.document_ids)[0], metric='euclidean')




