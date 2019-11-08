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
    reggae = []
    cachereggae = []
    forro = []
    cacheforro = []
    hiphop = []
    cachehiphop = []
    pagode = []
    cachepagode = []

    with open('caches_spotify.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            if (row[1]== "Sertanejo"):
                sertanejo.append(row[3])
                cachesertanejo.append(row[2])
            if (row[1]=="Axe"):
                axe.append(row[3]) 
                cacheaxe.append(row[2])
            if (row[1]=="Pop Rock"):
                poprock.append(row[3])
                cachepoprock.append(row[2])
            if (row[1]=="Eletronico"):
                eletronico.append(row[3])
                cacheeletronico.append(row[2])
            if (row[1]=="Funk"):
                funk.append(row[3])
                cachefunk.append(row[2])
            if (row[1]=="Samba"):
                samba.append(row[3])
                cachesamba.append(row[2])
            if (row[1]=="Reggae"):
                reggae.append(row[3])    
                cachereggae.append(row[2])            
            if (row[1]=="Forró"):
                forro.append(row[3])
                cacheforro.append(row[2])
            if (row[1]=="Hip Hop"):
                hiphop.append(row[3])
                cachehiphop.append(row[2])
            if (row[1]=="Pagode"):
                pagode.append(row[3])
                cachepagode.append(row[2])




    lista_geral_id = []

    lista_geral_id.append(sertanejo)
    lista_geral_id.append(axe)
    lista_geral_id.append(poprock)
    lista_geral_id.append(eletronico)
    lista_geral_id.append(funk)
    lista_geral_id.append(samba)
    lista_geral_id.append(reggae)
    lista_geral_id.append(hiphop)
    lista_geral_id.append(forro)
    lista_geral_id.append(pagode)

    lista_geral_caches = []
    lista_geral_caches.append(cachesertanejo)
    lista_geral_caches.append(cacheaxe)
    lista_geral_caches.append(cachepoprock)
    lista_geral_caches.append(cacheeletronico)
    lista_geral_caches.append(cachefunk)
    lista_geral_caches.append(cachesamba)
    lista_geral_caches.append(cachereggae)
    lista_geral_caches.append(cachehiphop)
    lista_geral_caches.append(cacheforro)
    lista_geral_caches.append(cachepagode)

    return lista_geral_id, lista_geral_caches


