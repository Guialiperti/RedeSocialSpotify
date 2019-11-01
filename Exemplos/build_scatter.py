import freeman as fm
import networkx as nx
import csv
import numpy as np
import matplotlib.pyplot as plt

lista_ids = []
lista_nomes = []
lista_caches = []
lista_indegree = []

with open('caches_spotify.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    for row in readCSV:
        id_artista = row[3]
        nome = row[0]
        cache = row[2]
        lista_ids.append(id_artista)
        lista_nomes.append(nome)
        lista_caches.append(cache)
    csvfile.close()

lista_nomes.pop(0)
lista_ids.pop(0)
lista_caches.pop(0)

counter = 0
node = nx.DiGraph()
print(lista_nomes)
for artista in lista_nomes:
    try:
        g = fm.load('{0}.gml'.format(artista))
        indegree = g.in_degree(lista_ids[counter])
        lista_indegree.append(indegree)
    except:
        print("{0} FAIL".format(artista))

    counter += 1

print(lista_indegree)


colors = (0,0,0)
area = np.pi*3

# Plot
plt.scatter(lista_caches, lista_indegree, s=area, alpha=0.5)
plt.title('Scatter Indegree x Cache')
plt.xlabel('Caches')
plt.ylabel('Indegree')
plt.show()







