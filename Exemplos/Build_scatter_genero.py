import freeman as fm
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
from funcoes import *



#Loop Scatter Indegree x Cache
counter_geral = 0
for lista_genero in lista_geral_id:

    lista_indegree = []
    counter = 0
    node = nx.DiGraph()
    for id_artista in lista_genero:
        artista = get_name(api, id_artista)
        try:
            g = fm.load('{0}.gml'.format(artista))
            indegree = g.in_degree(id_artista[counter])
            lista_indegree.append(indegree)
        except:
            print("{0} FAIL".format(artista))

        counter += 1
    #PLOTS

    colors = (0,0,0)
    area = np.pi*3

    # Plot Scatter Indegree x Cache
    plt.scatter(lista_geral_caches[counter_geral], lista_indegree, s=area, alpha=0.5)
    plt.title('Scatter Indegree x Cache')
    plt.xlabel('Indegree')
    plt.ylabel('Cache')
    plt.show()

    counter_geral += 1



#Loop Scatter Popularidade x Cache
counter_geral = 0
for lista_genero in lista_geral_id:

    lista_popularidade = []
    counter = 0
    for id_artista in lista_genero:
        artista = get_name(api, id_artista)
        try:
            popularidade = get_popularity_artist(api, artista)
            lista_popularidade.append(popularidade)
        except:
            print("{0} FAIL".format(artista))

        counter += 1
    #PLOTS

    colors = (0,0,0)
    area = np.pi*3

    # Plot Scatter Indegree x Cache
    plt.scatter(lista_geral_caches[counter_geral], lista_popularidade, s=area, alpha=0.5)
    plt.title('Scatter Popularidade x Cache')
    plt.xlabel('Popularidade')
    plt.ylabel('Cache')
    plt.show()

    counter_geral += 1



