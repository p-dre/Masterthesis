# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:02:27 2020

Zusammenfassung:
Es wird eine Darstellung zum besseren Verständis der Anpassung des Abstandsbegriffs entworfen
    

env: py38

Auführen mit:
Das Skript muss über Spyder laufen

Eingabe: -

Ausgabe: -


@author: Paul Drecker

"""
#Laden der Pakete
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy

# Punkte im Raum festlegen
X = np.array([0.5,2,3,-1,2,1, 1.4, 1, 1.9, 0.5])
Y = np.array([0,1,0,2,3, 1.9, 1.2, 0.5, 2, 0.5])
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)

# Kreise um die Punkte zeichnen
ax1.scatter(X, Y)
cir = plt.Circle((X[0], Y[0]), 0.5, color='black',fill=False)
cir1 = plt.Circle((X[1], Y[1]), 0.5, color='black',fill=False)
cir2 = plt.Circle((X[2], Y[2]), 0.5, color='black',fill=False)
cir3 = plt.Circle((X[3], Y[3]), 0.5, color='black',fill=False)
cir4 = plt.Circle((X[4], Y[4]), 0.5, color='black',fill=False)
cir5 = plt.Circle((X[5], Y[5]), 0.5, color='black',fill=False)
cir6 = plt.Circle((X[6], Y[6]), 0.5, color='black',fill=False)
cir7 = plt.Circle((X[7], Y[7]), 0.5, color='black',fill=False)
cir8 = plt.Circle((X[8], Y[8]), 0.5, color='black',fill=False)
cir9 = plt.Circle((X[9], Y[9]), 0.5, color='black',fill=False)

ax1.set_aspect('equal', adjustable='datalim')
ax1.add_patch(cir)
ax1.add_patch(cir1)
ax1.add_patch(cir2)
ax1.add_patch(cir3)
ax1.add_patch(cir4)
ax1.add_patch(cir5)
ax1.add_patch(cir6)
ax1.add_patch(cir7)
ax1.add_patch(cir8)
ax1.add_patch(cir9)
ax1.set_axis_off()
ax1.set_title('(1)', fontdict={'fontsize': 8, 'fontweight': 'medium'})




a = np.array([[X[0],Y[0]],
     [X[1],Y[1]],
     [X[2],Y[2]],
     [X[3],Y[3]],
     [X[4],Y[4]],
     [X[5],Y[5]],
     [X[6],Y[6]],
     [X[7],Y[7]],
     [X[8],Y[8]],
     [X[9],Y[9]]])
dis =np.linalg.norm(a - a[:,None], axis=-1)


# Kreise abhängig des Abstandes zu k-sten Nachbarn festlegen - k = 2
ax2.scatter(X, Y)
cir = plt.Circle((X[0], Y[0]), np.sort(dis[0])[2], color='black',fill=False)
cir1 = plt.Circle((X[1], Y[1]), np.sort(dis[1])[2], color='black',fill=False)
cir2 = plt.Circle((X[2], Y[2]), np.sort(dis[2])[2], color='black',fill=False)
cir3 = plt.Circle((X[3], Y[3]), np.sort(dis[3])[2], color='black',fill=False)
cir4 = plt.Circle((X[4], Y[4]), np.sort(dis[4])[2], color='black',fill=False)
cir5 = plt.Circle((X[5], Y[5]), np.sort(dis[5])[2], color='black',fill=False)
cir6 = plt.Circle((X[6], Y[6]), np.sort(dis[6])[2], color='black',fill=False)
cir7 = plt.Circle((X[7], Y[7]), np.sort(dis[7])[2], color='black',fill=False)
cir8 = plt.Circle((X[8], Y[8]), np.sort(dis[8])[2], color='black',fill=False)
cir9 = plt.Circle((X[9], Y[9]), np.sort(dis[9])[2], color='black',fill=False)

ax2.set_aspect('equal', adjustable='datalim')
ax2.add_patch(cir)
ax2.add_patch(cir1)
ax2.add_patch(cir2)
ax2.add_patch(cir3)
ax2.add_patch(cir4)
ax2.add_patch(cir5)
ax2.add_patch(cir6)
ax2.add_patch(cir7)
ax2.add_patch(cir8)
ax2.add_patch(cir9)
ax2.set_axis_off()
ax2.set_title('(2.)', fontdict={'fontsize': 8, 'fontweight': 'medium'})
#plt.savefig('explanation_umap.png', format='png', dpi=1200)
plt.show()





