import freeman as fm
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt
from funcoes import *
from gera_genero import *
from scipy.stats.stats import pearsonr
import csv
from scipy import stats
import pandas as pd



def calcula_densidade(g):
    n_of_edges = len(g.edges())
    n_of_nodes = len(g.nodes())
    den = (n_of_edges)/(n_of_nodes*(n_of_nodes-1))
    return den

#Globais
counter_geral = 0
generos = ["Sertanejo", "Axé", "Pop Rock e MPB", "Eletrônico", "Funk","Samba e Pagode","Hip Hop e Reggae"]

lista_geral_id , lista_geral_caches, todos_artistas , todos_caches, minn , maxx , caches_norm = gera_genero()

 


# Loop Scatter Indegree x Cache
def cache_x_indegree_geral(todos_artistas,todos_caches):
    lista_indegree = []
    for id_artista in todos_artistas:
        artista = get_name(api, id_artista)
        print(artista)
        try:
            g = fm.load('GMLS/{0}.gml'.format(artista))
            indegrees = g.in_degree()
            for x in indegrees:
                if (id_artista in x):
                    indegree = x[1]
                    print(indegree)
                    lista_indegree.append(indegree)
        except:
            print("{0} FAIL".format(artista))
    
    #PLOTS

    colors = (0,0,0)
    area = np.pi*3
    ppv = pearsonr(lista_indegree,todos_caches)

    plt.scatter(lista_indegree,todos_caches, s=area, alpha=0.5)
    plt.suptitle('Scatter Indegree x Cache ')
    plt.title('Pvalue: {0} and Coeficiente de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
    plt.xlabel('Indegree')
    plt.ylabel('Cache')
    plt.show()

    return lista_indegree

def cache_x_indegree_genero(lista_geral_id,lista_geral_caches):
    counter_geral = 0
    for lista_genero in lista_geral_id:
        lista_indegree = []
        node = nx.DiGraph()
        for id_artista in lista_genero:
            artista = get_name(api, id_artista)
            print(artista)
            try:
                g = fm.load('GMLS/{0}.gml'.format(artista))
                indegrees = g.in_degree()
                for x in indegrees:
                    if (id_artista in x):
                        indegree = x[1]
                        print(indegree)
                        lista_indegree.append(indegree)
            except:
                print("{0} FAIL".format(artista))

        #PLOTS

        colors = (0,0,0)
        area = np.pi*3

        ppv = pearsonr(lista_indegree,lista_geral_caches[counter_geral])

        # Plot Scatter Indegree x Cache
        lista_caches = lista_geral_caches[counter_geral]
        plt.scatter(lista_indegree,lista_caches, s=area, alpha=0.5)
        plt.suptitle('Scatter Indegree x Cache- '+ generos[counter_geral])
        plt.title('Pvalue: {0} and Coeficiente de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
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

    ppv = pearsonr(lista_popularidade,todos_caches)
    
        
    plt.scatter(lista_popularidade,todos_caches, s=area, alpha=0.5)
    plt.suptitle('Scatter Popularidade x Cache')
    plt.title('Pvalue: {0} and Coeficiente de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
    plt.xlabel('Popularidade')
    plt.ylabel('Cache')
    plt.show()

    return lista_popularidade



def popularidade_cache_genero(lista_geral_id,lista_geral_caches):
    counter_geral = 0
    for lista_genero in lista_geral_id:
        lista_popularidade = []
        for id_artista in lista_genero:
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
        ppv = pearsonr(lista_popularidade,lista_geral_caches[counter_geral])
        

        plt.scatter( lista_popularidade,lista_geral_caches[counter_geral], s=area, alpha=0.5)
        plt.suptitle('Scatter Popularidade x Cache - '+ generos[counter_geral])
        plt.title('Pvalue: {0} and Coeficiente de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
        plt.xlabel('Popularidade')
        plt.ylabel('Cache')
        plt.show()

        counter_geral += 1


# Scatter Cachê x Densidade 


def cache_x_densidade_geral(todos_artistas,todos_caches):
    #counter_geral = 0
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

    ppv = pearsonr(lista_densidade,todos_caches)
        
        # Plot Scatter Densidade x Cache
    plt.scatter(lista_densidade,todos_caches, s=area, alpha=0.5)
    plt.suptitle('Scatter Densidade x Cache')
    plt.title('Pvalue: {0} / Cf de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
    plt.xlabel('Densidade')
    plt.ylabel('Cache')
    plt.show()

    return lista_densidade


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
            clustering = nx.average_clustering(g)
            lista_clustering.append(clustering)
        except:
            print("{0} FAIL".format(artista))

    #PLOTS

    colors = (0,0,0)
    area = np.pi*3

    ppv = pearsonr(lista_clustering,todos_caches)
        
    # Plot Scatter Clustering x Cache
    plt.scatter(lista_clustering,todos_caches, s=area, alpha=0.5)
    plt.suptitle('Scatter Clustering x Cache')
    plt.title('Pvalue: {0} / Cf de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
    plt.xlabel('Clustering')
    plt.ylabel('Cache')
    plt.show()

    return lista_clustering


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
        plt.scatter(lista_clustering,lista_geral_caches[counter_geral], s=area, alpha=0.5)
        plt.suptitle('Scatter Clustering Coefficient x Cache - '+ generos[counter_geral])
        plt.title('Pvalue: {0} / Cf de Correlação de Pearson: {1}'.format(ppv[1],ppv[0]))
        plt.xlabel('Clustering Coefficient')
        plt.ylabel('Cache')
        plt.show()

        counter_geral += 1



#cache_x_indegree_geral(todos_artistas,todos_caches)
#cache_x_indegree_geral(todos_artistas,caches_norm)
#cache_x_indegree_genero(lista_geral_id,lista_geral_caches)

#populariade_cache_geral(todos_artistas,todos_caches)
#populariade_cache_geral(todos_artistas,caches_norm)
#popularidade_cache_genero(lista_geral_id,lista_geral_caches)

#cache_x_densidade_geral(todos_artistas,todos_caches)
#cache_x_densidade_geral(todos_artistas,caches_norm)
#cache_x_densidade_genero(lista_geral_id,lista_geral_caches)

#cache_x_clustering_geral(todos_artistas,todos_caches)
cache_x_clustering_geral(todos_artistas,caches_norm)
#cache_x_clustering_genero(lista_geral_id,lista_geral_caches)


#regress = pd.read_csv('regressao.csv')
#rrr = fm.logregress(regress,['Popularidade','Clustering Coefficient'],'Cache')
