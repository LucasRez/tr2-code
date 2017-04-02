import sys
from grafo import Grafo
from heap import Heap

def dijkstra(grafo, comeco, fim):
    h = Heap()
    lista = []

    #inicializa valores de distancia e cria a fila de prioridade
    for v in grafo.vertDict.keys():
        if v == comeco:
            lista.append((v, 0))
        else:
            lista.append((v, sys.maxint))
    h.buildHeap(lista)
    predecessores = {h.heapList[1][0]: None}
    visitados = []
    atual = (None,0)

    #calcula as distancias e guarda de onde foi calculada a menor distancia
    while not h.isEmpty():
        atual = h.delMin()
        visitados.append(atual[0])
        vAtual = grafo.getVertice(atual[0])
        for vProximo in vAtual.getConexoes():
            if vProximo.getId() not in visitados:
                novaDist = atual[1] + vAtual.getPeso(vProximo)
                proximo = [x for j, x in enumerate(h.heapList) if x[0] == vProximo.getId()][0]
                if novaDist < proximo[1]:
                    j = h.heapList.index(proximo)
                    h.heapList[j] = (proximo[0],novaDist)
                    h.percolaAcima(j)
                    predecessores[proximo[0]] = atual[0]

    #backtracking para achar o menor caminho
    a = fim
    caminho = []

    while a:
        if a not in predecessores:
            return []
        caminho = [a] + caminho
        a = predecessores[a]
    return caminho


def kpaths(grafo, comeco, fim, k):
    g = grafo
    caminhos = []
    while k > 0:
        arestas = []
        naoRemover = []
        minAresta = None
        caminho = dijkstra(g, comeco, fim)
        for i in range(0, len(caminho) - 1):
            arestas.append(g.getAresta(caminho[i], caminho[i+1]))
        if arestas:
            caminhos.append(caminho)
            #seleciona candidatas de arestas a serem removidas
            # while minAresta is None:
            #     minAresta = min(arestas, key = lambda t: t[2])
            #     if len(arestas) == 1:
            #         print minAresta, "pq sobrou"
            #         g.removeAresta(minAresta[0], minAresta[1])
            #     elif minAresta[1] is fim and len(grafo.getVertice(minAresta[1]).getConexoes()) <= 1:
            #         arestas.remove(minAresta)
            #         minAresta = None
            #     elif len(grafo.getVertice(minAresta[1]).getConexoes()) <= 2:
            #         arestas.remove(minAresta)
            #         minAresta = None
            #     elif minAresta[0] is comeco and len(grafo.getVertice(minAresta[1]).getConexoes()) <= 1:
            #         arestas.remove(minAresta)
            #         minAresta = None
            #     else:
            #         print minAresta, "pq foi essa msm"
            #         g.removeAresta(minAresta[0], minAresta[1])
            print "antes", arestas
            for aresta in arestas:
                if len(arestas) == 1:
                    break
                elif (aresta[0] != comeco and len(g.getVertice(aresta[0]).getConexoes()) <= 2) or (aresta[1] != fim and len(g.getVertice(aresta[1]).getConexoes()) <= 2):
                    naoRemover.append(aresta)
                elif aresta[0] == comeco and len(g.getVertice(comeco).getConexoes()) <= 1:
                    naoRemover.append(aresta)
                elif aresta[1] == fim and len(g.getVertice(fim).getConexoes()) <= 1:
                    naoRemover.append(aresta)
                else:
                    pass
            for aresta in naoRemover:
                if len(arestas) > 1:
                    arestas.remove(aresta)
            print "depois" ,arestas
            print "aresta removida:", arestas[0]
            print  "---------------------"
            grafo.removeAresta(arestas[0][0], arestas[0][1])


        else:
            minAresta = None
        k = k - 1
        if caminho == []:
            break
    return caminhos


if __name__ == '__main__':

    g = Grafo()

    g.addVertice('a')
    g.addVertice('b')
    g.addVertice('c')
    g.addVertice('d')
    g.addVertice('e')
    g.addVertice('f')

    g.addAresta('a', 'b', 1)
    g.addAresta('a', 'c', 1)
    g.addAresta('a', 'f', 1)
    g.addAresta('b', 'c', 1)
    g.addAresta('b', 'd', 1)
    g.addAresta('c', 'd', 1)
    g.addAresta('c', 'f', 1)
    g.addAresta('d', 'e', 1)
    g.addAresta('e', 'f', 1)

    for path in kpaths(g, 'a', 'f', 7):
        print path
