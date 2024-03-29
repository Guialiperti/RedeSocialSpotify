import freeman as fm
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
from funcoes import *
from gera_genero import *

lista_geral_id, lista_geral_caches = gera_genero()

# Loop Scatter Indegree x Cache
# counter_geral = 0
# for lista_genero in lista_geral_id:
#     print(len(lista_genero))
#     print(len(lista_geral_caches[counter_geral]))
#     lista_indegree = []
#     counter = 0
#     node = nx.DiGraph()
#     for id_artista in lista_genero:
#         artista = get_name(api, id_artista)
#         try:
#             g = fm.load('{0}.gml'.format(artista))
#             indegree = g.in_degree(id_artista[counter])
#             lista_indegree.append(indegree)
#         except:
#             print("{0} FAIL".format(artista))

#         counter += 1
#     #PLOTS

#     colors = (0,0,0)
#     area = np.pi*3

#     # Plot Scatter Indegree x Cache
#     lista_caches = lista_geral_caches[counter_geral]
#     print(lista_caches)
#     print(lista_indegree)
#     plt.scatter(lista_caches, lista_indegree, s=area, alpha=0.5)
#     plt.title('Scatter Indegree x Cache')
#     plt.xlabel('Indegree')
#     plt.ylabel('Cache')
#     plt.show()

#     counter_geral += 1



#Loop Scatter Popularidade x Cache
#counter_geral = 0
#for lista_genero in lista_geral_id:
#
 #   lista_popularidade = []
 #   counter = 0
 #   for id_artista in lista_genero:
 #       artista = get_name(api, id_artista)
 #       try:
 #           popularidade = get_popularity_artist(api, id_artista)
 #           lista_popularidade.append(popularidade)
 #       except:
 #           print("{0} FAIL".format(artista))
#
 #       counter += 1
    #PLOTS

  #  colors = (0,0,0)
  #  area = np.pi*3

    # Plot Scatter Indegree x Cache
   # plt.scatter(lista_geral_caches[counter_geral], lista_popularidade, s=area, alpha=0.5)
   # plt.title('Scatter Popularidade x Cache')
   # plt.xlabel('Popularidade')
   # plt.ylabel('Cache')
   # plt.show()

   # counter_geral += 1

#Loop Scatter Densidade x Cache 

#def calcula_densidade(g):
#    n_of_edges = len(g.edges())
#    n_of_nodes = len(g.nodes())
#    den = (2*n_of_edges)/(n_of_nodes*(n_of_nodes-1))
#    return den
#
#counter_geral = 0
#for lista_genero in lista_geral_id:
#    lista_densidade = []
#    counter = 0
#    node = nx.DiGraph()   
#    for id_artista in lista_genero:
#        artista = get_name(api, id_artista)
#        try:
#            g = fm.load('{0}.gml'.format(artista))
#            densidade = calcula_densidade(g) - 1
#            lista_densidade.append(densidade)
#        except:
#
#            print("{0} FAIL".format(artista))
#
#        counter += 1
    #PLOTS

 #   colors = (0,0,0)
 #   area = np.pi*3
    
    # Plot Scatter Densidade x Cache
 #   plt.scatter(lista_geral_caches[counter_geral], lista_densidade, s=area, alpha=0.5)
 #   plt.title('Scatter Densidade x Cache')
 #   plt.xlabel('Densidade')
 #   plt.ylabel('Cache')
 #   plt.show()

 #   counter_geral += 1






#Globais
counter_geral = 0
generos = ["Sertanejo", "Axé", "Pop Rock e MPB", "Eletrônico", "Funk","Samba e Pagode","Hip Hop e Reggae"]

#Loop Scatter Popularidade x Cache
for lista_genero in lista_geral_id:

    lista_popularidade = []
    counter = 0
    for id_artista in lista_genero:
        artista = get_name(api, id_artista)
        try:
            popularidade = get_popularity_artist(api, id_artista)
            lista_popularidade.append(popularidade)
        except:
            print("{0} FAIL".format(artista))

        counter += 1
    #PLOTS

    colors = (0,0,0)
    area = np.pi*3

    print(lista_geral_caches)

    # Plot Scatter Indegree x Cache
    plt.scatter(lista_geral_caches[counter_geral], lista_popularidade, s=area, alpha=0.5)
    plt.title('Scatter Popularidade x Cache - '+ generos[counter_geral])
    plt.ylabel('Popularidade')
    plt.xlabel('Cache')
    plt.show()

    counter_geral += 1


#Loop Scatter Densidade x Cache 

def calcula_densidade(g):
    n_of_edges = len(g.edges())
    n_of_nodes = len(g.nodes())
    den = (2*n_of_edges)/(n_of_nodes*(n_of_nodes-1))
    return den

counter_geral = 0
for lista_genero in lista_geral_id:
    lista_densidade = []
    counter = 0
    node = nx.DiGraph()   
    for id_artista in lista_genero:
        artista = get_name(api, id_artista)
        try:
            g = fm.load('{0}.gml'.format(artista))
            densidade = nx.density(g)
            lista_densidade.append(densidade)
        except:

            print("{0} FAIL".format(artista))

        counter += 1
    #PLOTS

    colors = (0,0,0)
    area = np.pi*3
    
    # Plot Scatter Densidade x Cache
    plt.scatter(lista_geral_caches[counter_geral], lista_densidade, s=area, alpha=0.5)
    plt.title('Scatter Densidade x Cache'+ generos[counter_geral])
    plt.ylabel('Popularidade')
    plt.xlabel('Cache')
    plt.show()

    counter_geral += 1



#Loop Scatter Clustering coefficient x Cache 
counter_geral = 0
for lista_genero in lista_geral_id:

    lista_clustering = []
    counter = 0
    node = nx.DiGraph()
    for id_artista in lista_genero:
        artista = get_name(api, id_artista)
        try:
            g = fm.load('{0}.gml'.format(artista))
            clustering = nx.average_clustering(g)
            lista_clustering.append(clustering)
        except:
            print("{0} FAIL".format(artista))

        counter += 1
    #PLOTS

    colors = (0,0,0)
    area = np.pi*3

    # Plot Scatter Densidade x Cache
    plt.scatter(lista_geral_caches[counter_geral], lista_clustering, s=area, alpha=0.5)
    plt.title('Scatter Clustering Coefficient x Cache'+ generos[counter_geral])
    plt.ylabel('Popularidade')
    plt.xlabel('Cache')
    plt.show()

    counter_geral += 1



