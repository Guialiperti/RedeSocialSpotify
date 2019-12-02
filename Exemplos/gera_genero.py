from save import Saver
import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics

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

# Forma 1 de Normalizar

    normser = [float(i)/max(cachesertanejo) for i in cachesertanejo]
    normaxe = [float(i)/max(cacheaxe) for i in cacheaxe]
    normpr = [float(i)/max(cachepoprock) for i in cachepoprock]
    normelet = [float(i)/max(cacheeletronico) for i in cacheeletronico]
    normfunk = [float(i)/max(cachefunk) for i in cachefunk]
    normsamba = [float(i)/max(cachesamba) for i in cachesamba]
    normhiphop = [float(i)/max(cachehiphop) for i in cachehiphop]

# Forma 2 de Normalizar
#    normser = [(float(i) - min(cachesertanejo))/(max(cachesertanejo)-min(cachesertanejo)) for i in cachesertanejo]
#    normaxe = [(float(i) - min(cacheaxe))/(max(cacheaxe)-min(cacheaxe)) for i in cacheaxe]
#    normpr = [(float(i) - min(cachepoprock))/(max(cachepoprock)-min(cachepoprock)) for i in cachepoprock]
#    normelet = [(float(i) - min(cacheeletronico))/(max(cacheeletronico)-min(cacheeletronico)) for i in cacheeletronico]
#   normfunk = [(float(i) - min(cachefunk))/(max(cachefunk)-min(cachefunk)) for i in cachefunk]
#    normsamba = [(float(i) - min(cachesamba))/(max(cachesamba)-min(cachesamba)) for i in cachesamba]
#    normhiphop = [(float(i) - min(cachehiphop))/(max(cachehiphop)-min(cachehiphop)) for i in cachehiphop]

# Forma 3 de Normalizar

#    dvser = statistics.stdev(cachesertanejo)
#    dvaxe = statistics.stdev(cacheaxe)
#    dvpr = statistics.stdev(cachepoprock)
#    dvelet = statistics.stdev(cacheeletronico)
#    dvfunk = statistics.stdev(cachefunk)
#    dvsamba = statistics.stdev(cachesamba)
#    dvhp = statistics.stdev(cachehiphop)
#    normser = [(float(i) - min(cachesertanejo))/(max(cachesertanejo)-min(cachesertanejo)) for i in cachesertanejo]
#    normaxe = [(float(i) - min(cacheaxe))/(max(cacheaxe)-min(cacheaxe)) for i in cacheaxe]
#    normpr = [(float(i) - min(cachepoprock))/(max(cachepoprock)-min(cachepoprock)) for i in cachepoprock]
#    normelet = [(float(i) - min(cacheeletronico))/(max(cacheeletronico)-min(cacheeletronico)) for i in cacheeletronico]
#    normfunk = [(float(i) - min(cachefunk))/(max(cachefunk)-min(cachefunk)) for i in cachefunk]
#    normsamba = [(float(i) - min(cachesamba))/(max(cachesamba)-min(cachesamba)) for i in cachesamba]
#    normhiphop = [(float(i) - min(cachehiphop))/(max(cachehiphop)-min(cachehiphop)) for i in cachehiphop]

    cachesnorm = normser + normaxe + normpr + normelet + normfunk + normsamba + normhiphop
 
    minser = min(cachesertanejo)
    maxser = max(cachesertanejo)
    minaxe = min(cacheaxe)
    maxaxe = max(cacheaxe)
    minpr = min(cachepoprock)
    maxpr = max(cachepoprock)
    minelet = min(cacheeletronico)
    maxelet = max(cacheeletronico)
    minfunk = min(cachefunk)
    maxfunk = max(cachefunk)
    minsamba = min(cachesamba)
    maxsamba = max(cachesamba)
    minhiphop = min(cachehiphop)
    maxhiphop= max(cachehiphop)

    minimos = []
    maximos = []

    minimos.append(minser)
    maximos.append(maxser)
    minimos.append(minaxe)
    maximos.append(maxaxe)
    minimos.append(minpr)
    maximos.append(maxpr)  
    minimos.append(minelet)
    maximos.append(maxelet)
    minimos.append(minfunk)
    maximos.append(maxfunk)
    minimos.append(minsamba)
    maximos.append(maxsamba)
    minimos.append(minhiphop)
    maximos.append(maxhiphop)


    
    minvalue = int(sum(minimos)/len(minimos))
    maxvalue = int(sum(maximos)/len(maximos))

    
    return lista_geral_id, lista_geral_caches , td , tdcache , minvalue , maxvalue , cachesnorm


gera_genero()