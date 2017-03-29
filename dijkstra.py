from grafo import *


def dijkstra(grafo, comeco, fim):
    tabela = []
    i = 0
    anterior = comeco
    # inicializa distancias
    linha = {}
    for w in grafo:
        if w is grafo.getVertice(comeco):
            linha[w.getId()] = 0
        else:
            linha[w.getId()] = sys.maxint
    newlinha = linha
    tabela.append(linha.copy())
    i = i + 1
    marcados = [min(linha, key=linha.get)]
    naoMarcados = []
    a = min(linha, key=linha.get)
    anterior = a
    for w in grafo:
        if w not in marcados:
            naoMarcados.append(w.getId())

    # laco principal
    # preenche tabela de distancias
    while naoMarcados:
        aux = {}
        for w in naoMarcados:
            if grafo.getVertice(w) in grafo.getVertice(anterior).getConexoes():
                novaDist = linha[anterior] + grafo.getVertice(anterior).getPeso(grafo.getVertice(w))
                linha[w] = min(novaDist, tabela[i-1][w])
                aux[w] = linha[w]
        a = min(aux, key=aux.get)
        anterior = a
        marcados.append(a)
        naoMarcados.remove(a)
        tabela.append(linha.copy())
        i = i + 1

    # backtracking para fazer o caminho mais curto
    i = marcados.index(fim)
    j = i
    caminho = [fim]

    while i > 0:
        i = i - 1

        if tabela[i][marcados[j]] != tabela[i+1][marcados[j]]:
            j = i
            caminho = [marcados[j]] + caminho
    return caminho






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

    dijkstra(g, 'a', 'f')
