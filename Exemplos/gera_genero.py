from save import Saver
import csv
import numpy as np
import matplotlib.pyplot as plt

def gera_genero():
    sertanejo = []
    cachesertanejo = []
    axe = []
    cacheaxe = []
    poprock = []
    cachepoprock = []
    eletronico = []
    cacheeletronico = []
    funk = []
    cachefunk = []
    samba = []
    cachesamba = []
    hiphop = []
    cachehiphop = []

    td = []
    tdcache = []


    with open('caches_spotify.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            td.append(row[3])
            tdcache.append(int(row[2]))
            if (row[1]== "Sertanejo"):
                sertanejo.append(row[3])
                cachesertanejo.append(int(row[2]))
            if (row[1]=="Axe"):
                axe.append(row[3]) 
                cacheaxe.append(int(row[2]))
            if (row[1]=="Pop Rock"):
                poprock.append(row[3])
                cachepoprock.append(int(row[2]))
            if (row[1]=="Eletronico"):
                eletronico.append(row[3])
                cacheeletronico.append(int(row[2]))
            if (row[1]=="Funk"):
                funk.append(row[3])
                cachefunk.append(int(row[2]))
            if (row[1]=="Samba"):
                samba.append(row[3])
                cachesamba.append(int(row[2]))        
            if (row[1]=="Hip Hop"):
                hiphop.append(row[3])
                cachehiphop.append(int(row[2]))





    lista_geral_id = []

    lista_geral_id.append(sertanejo)
    lista_geral_id.append(axe)
    lista_geral_id.append(poprock)
    lista_geral_id.append(eletronico)
    lista_geral_id.append(funk)
    lista_geral_id.append(samba)
    lista_geral_id.append(hiphop)


    lista_geral_caches = []
    lista_geral_caches.append(cachesertanejo)
    lista_geral_caches.append(cacheaxe)
    lista_geral_caches.append(cachepoprock)
    lista_geral_caches.append(cacheeletronico)
    lista_geral_caches.append(cachefunk)
    lista_geral_caches.append(cachesamba)
    lista_geral_caches.append(cachehiphop)



    return lista_geral_id, lista_geral_caches , td , tdcache


