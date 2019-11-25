import os


def build(path):
    names = {}
    edges = set()
    for filename in os.listdir(path):
        n = filename[:]

        with open(os.path.join(path, filename), encoding='iso-8859-1') as file:
            name = file.readline().strip()
            names[n] = name

            for line in file:
                m = line.strip()
                edges.add((n, m))

    edges = [(n, m) for (n, m) in edges if n in names and m in names]

    return names, edges
