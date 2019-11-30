import freeman as fm
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
from funcoes import *
from gera_genero import *
from scipy.stats.stats import pearsonr

def calcula_densidade(g):
    n_of_edges = len(g.edges())
    n_of_nodes = len(g.nodes())
    den = (n_of_edges)/(n_of_nodes*(n_of_nodes-1))
    return den

#Globais
counter_geral = 0
generos = ["Sertanejo", "Axé", "Pop Rock e MPB", "Eletrônico", "Funk","Samba e Pagode","Hip Hop e Reggae"]



# Loop Scatter Indegree x Cache
def cache_x_indegree_genero(lista_geral_id,lista_geral_caches):
    counter_geral = 0
    for lista_genero in lista_geral_id:
        print(len(lista_genero))
        print(len(lista_geral_caches[counter_geral]))
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
        lista_caches = lista_geral_caches[counter_geral]
        print(lista_caches)
        print(lista_indegree)
        plt.scatter(lista_caches, lista_indegree, s=area, alpha=0.5)
        plt.title('Scatter Indegree x Cache')
        plt.xlabel('Indegree')
        plt.ylabel('Cache')
        plt.show()

        counter_geral += 1


#Scatter Popularidade x Cache
def populariade_cache_geral(todos_artistas,todos_caches):
    lista_popularidade = []
    for id_artista in todos_artistas:
        artista = get_name(api, id_artista)
        print(artista)
        try:
            popularidade = get_popularity_artist(api, id_artista)
            lista_popularidade.append(popularidade)
        except:
            print("{0} FAIL".format(artista))

        #PLOTS

    colors = (0,0,0)
    area = np.pi*3

    ppv = pearsonr(todos_caches,lista_popularidade)
        
        # Plot Scatter Indegree x Cache
    plt.scatter(lista_popularidade,todos_caches, s=area, alpha=0.5)
    plt.suptitle('Scatter Popularidade x Cache - ')
    plt.title('Pvalue: {0} and Coeficiente de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
    plt.ylabel('Popularidade')
    plt.xlabel('Cache')
    plt.show()


def popularidade_cache_genero(lista_geral_id,lista_geral_caches):
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
        ppv = pearsonr(lista_geral_caches[counter_geral],lista_popularidade)
        

        print(lista_geral_caches)

        # Plot Scatter Indegree x Cache
        plt.scatter(lista_geral_caches[counter_geral], lista_popularidade, s=area, alpha=0.5)
        plt.suptitle('Scatter Popularidade x Cache - '+ generos[counter_geral])
        plt.title('Pvalue: {0} and Coeficiente de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
        plt.ylabel('Popularidade')
        plt.xlabel('Cache')
        plt.show()

        counter_geral += 1


# Scatter Cachê x Densidade 


def cache_x_densidade_geral(todos_artistas,todos_caches):
    counter_geral = 0
    lista_densidade = []
    node = nx.DiGraph()   

    for id_artista in todos_artistas:
        artista = get_name(api, id_artista)
        print(artista)
        try:
            g = fm.load('GMLS/{0}.gml'.format(artista))
            densidade = nx.density(g)
            lista_densidade.append(densidade)
        except:
            print("{0} FAIL".format(artista))

        #PLOTS

        colors = (0,0,0)
        area = np.pi*3

        #ppv = pearsonr(todos_caches, lista_densidade)
        
        # Plot Scatter Densidade x Cache
    plt.scatter(lista_densidade,todos_caches, s=area, alpha=0.5)
    plt.suptitle('Scatter Densidade x Cache')
    # plt.title('Pvalue: {0} / Cf de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
    plt.xlabel('Densidade')
    plt.ylabel('Cache')
    plt.show()


#Densidade x Cache por gênero

def cache_x_densidade_genero(lista_geral_id,lista_geral_caches):    
    counter_geral = 0
    for lista_genero in lista_geral_id:
        lista_densidade = []
        counter = 0
        node = nx.DiGraph()   
        for id_artista in lista_genero:
            artista = get_name(api, id_artista)
            print(artista)
            try:
                g = fm.load('GMLS/{0}.gml'.format(artista))
                densidade = nx.density(g)
                lista_densidade.append(densidade)
            except:

                print("{0} FAIL".format(artista))

            counter += 1
        #PLOTS

        colors = (0,0,0)
        area = np.pi*3
        ppv = pearsonr(lista_geral_caches[counter_geral], lista_densidade)
        
        # Plot Scatter Densidade x Cache
        plt.scatter(lista_densidade,lista_geral_caches[counter_geral], s=area, alpha=0.5)
        plt.suptitle('Scatter Densidade x Cache - '+ generos[counter_geral])
        plt.title('Pvalue: {0} / Cf de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
        plt.xlabel('Densidade')
        plt.ylabel('Cache')
        plt.show()

        counter_geral += 1

# Scattter Cachê x Clustering

def cache_x_clustering_geral(todos_artistas,todos_caches):
    counter_geral = 0
    lista_clustering = []
    node = nx.DiGraph()   

    for id_artista in todos_artistas:
        artista = get_name(api, id_artista)
        print(artista)
        try:
            g = fm.load('GMLS/{0}.gml'.format(artista))
            clustering = nx.density(g)
            lista_clustering.append(clustering)
        except:
            print("{0} FAIL".format(artista))

        #PLOTS

        colors = (0,0,0)
        area = np.pi*3

       # ppv = pearsonr(todos_caches, lista_clustering)
        
        # Plot Scatter Clustering x Cache
    plt.scatter(lista_clustering,todos_caches, s=area, alpha=0.5)
    plt.suptitle('Scatter Clustering x Cache')
 #   plt.title('Pvalue: {0} / Cf de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
    plt.xlabel('Clustering')
    plt.ylabel('Cache')
    plt.show()

# Clustering coefficient x Cache por gênero
def cache_x_clustering_genero(lista_geral_id,lista_geral_caches):    
    counter_geral = 0
    for lista_genero in lista_geral_id:

        lista_clustering = []
        counter = 0
        node = nx.DiGraph()
        for id_artista in lista_genero:
            artista = get_name(api, id_artista)
            try:
                g = fm.load('GMLS/{0}.gml'.format(artista))
                clustering = nx.average_clustering(g)
                lista_clustering.append(clustering)
            except:
                print("{0} FAIL".format(artista))

            counter += 1
        #PLOTS

        colors = (0,0,0)
        area = np.pi*3
        ppv = pearsonr(lista_geral_caches[counter_geral],  lista_clustering)

        # Plot Scatter Densidade x Cache
        plt.scatter(lista_geral_caches[counter_geral], lista_clustering, s=area, alpha=0.5)
        plt.suptitle('Scatter Clustering Coefficient x Cache - '+ generos[counter_geral])
        plt.title('Pvalue: {0} / Cf de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
        plt.ylabel('Clustering Coefficient')
        plt.xlabel('Cache')
        plt.show()

        counter_geral += 1


lista_geral_id , lista_geral_caches, todos_artistas , todos_caches = gera_genero()

cache_x_clustering_geral(todos_artistas,todos_caches)
