# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:01:14 2020

Zusammenfassung:
Ausgabe der Bilder von UMAP und hdbscan
Mindestens 120 RAM benötigt

env: top2vec_final

Auführen mit:
Das Skript muss über spyder laufen

Eingabe: Die Ausgabe von Covid_6_top2vec.py

Ausgabe: Bilder der Dokumente im zweidimensionalen Raum 


@author: Paul Drecker

"""
#Laden der Pakete
import umap
import hdbscan
import os
import umap.plot

# working directory auf den Ordner Masterarbeit festlegen
os.chdir(r'C:\Users\Paul\Documents\Uni\Masterarbeit\Final_Code\Masterarbeit')

#Laden des Modells
model = top.Top2Vec.load(os.getcwd() + r'\Topicmodelfinal\\top2vec_300_30')

# Dokumentvektoren in 300 Dimension speichern
emb = model.model.docvecs.vectors_docs

# Löschen des Modells um RAM frei zu machen
model = None
del(model)

# Daten auf fünf Dimensionen reduzieren 
umap_model = umap.UMAP(n_neighbors=15,
                               n_components=5,
                               metric='cosine', low_memory=True).fit(emb)

# Cluster in fünf Dimensionen bilden
cluster = hdbscan.HDBSCAN(min_cluster_size=15,
                                  metric='euclidean',
                                  cluster_selection_method='eom').fit(umap_model.embedding_)

# Löschen des Modells um RAM frei zu machen
umap_model = None
del(umap_model)

# Daten auf zwei Dimensionen reduzieren
umap_model_plot = umap.UMAP(n_neighbors=15,
                               n_components=2,
                               metric='cosine').fit(emb)

# Umap Plot
umap.plot.points(umap_model_plot, theme='blue')


# Umap Plot mit Clustern
umap.plot.points(umap_model_plot, labels =cluster.labels_ )



