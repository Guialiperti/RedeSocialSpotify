from unidecode import unidecode

from build import build
import csv


#NAME = 'spotify'

DIRECTED = True


def main():
    lista_ids = []
    lista_nomes = []
    with open('caches_spotify.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')

        for row in readCSV:
            id_artista = row[3]
            nome = row[0]
            print(nome)
            lista_ids.append(id_artista)
            lista_nomes.append(nome)

    #names, edges = build(NAME)
    for nomes in lista_nomes:
        NAME = nomes
        names, edges = build(nomes)

        with open("GMLs/" + NAME + '.gml', 'w', encoding='utf-8') as file:
            file.write('graph [\n')
            file.write('  directed {}\n'.format(int(DIRECTED)))

            for n in names:
                file.write('  node [\n')
                file.write('    id "{}"\n'.format(n))
                file.write('    name "{}"\n'.format(unidecode(names[n])))
                file.write('  ]\n')

            for n, m in edges:
                file.write('  edge [\n')
                file.write('    source "{}"\n'.format(n))
                file.write('    target "{}"\n'.format(m))
                file.write('  ]\n')

            file.write(']\n')


if __name__ == '__main__':
    main()
