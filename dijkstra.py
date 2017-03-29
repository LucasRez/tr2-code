from grafo import *


def dijInit(grafo, comeco):
    visitados = [comeco]
    naoVisitados = []
    for j in grafo.vertDict:
        if j not in visitados:
            naoVisitados.append(j)

    print("visitados:",visitados)
    print("Nao visitados:",naoVisitados)

    while naoVisitados:
        g.getVertice(comeco).getDistancia(g.getVertice(naoVisitados[0]))
        visitados.append(naoVisitados[0])
        naoVisitados.remove(naoVisitados[0])
        print("visitados:",visitados)
        print("Nao visitados:",naoVisitados)

    for w in g.getVertice(comeco).distancias:
        print (w.id, g.getVertice(comeco).distancias[w])



if __name__ == '__main__':

    g = Grafo()

    g.addVertice('a')
    g.addVertice('b')
    g.addVertice('c')
    g.addVertice('d')
    g.addVertice('e')
    g.addVertice('f')

    g.addAresta('a', 'b', 7)
    g.addAresta('a', 'c', 9)
    g.addAresta('a', 'f', 14)
    g.addAresta('b', 'c', 10)
    g.addAresta('b', 'd', 15)
    g.addAresta('c', 'd', 11)
    g.addAresta('c', 'f', 2)
    g.addAresta('d', 'e', 6)
    g.addAresta('e', 'f', 9)

    dijInit(g, g.getVertice('a').getId())
