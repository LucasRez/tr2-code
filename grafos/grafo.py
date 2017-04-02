class Vertice:
    def __init__(self, nodo):
        self.id = nodo
        self.adjacentes = {}

    def __str__(self):
        return str(self.id) + ' adjacentes: ' + str([x.id for x in self.adjacentes])

    def addVizinho(self, vizinho, peso = 1):
        self.adjacentes[vizinho] = peso

    def removeVizinho(self, vizinho):
        del self.adjacentes[vizinho]

    def getConexoes(self):
        return self.adjacentes.keys()

    def getId(self):
        return self.id

    def getPeso(self, vizinho):
        return self.adjacentes[vizinho]


class Grafo:
    def __init__(self):
        self.vertDict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertDict.values())

    def addVertice(self, nodo):
        self.num_vertices = self.num_vertices + 1
        novoVertice = Vertice(nodo)
        self.vertDict[nodo] = novoVertice
        return novoVertice

    def getVertice(self, nodo):
        if nodo in self.vertDict:
            return self.vertDict[nodo]
        else:
            return None

    def addAresta(self, de, para, peso = 1):
        if de not in self.vertDict:
            self.addVertice(de)
        if para not in self.vertDict:
            self.addVertice(para)
        self.vertDict[de].addVizinho(self.vertDict[para], peso)
        self.vertDict[para].addVizinho(self.vertDict[de], peso)

    def removeAresta(self, de, para):
        if de in self.vertDict and para in self.vertDict:
            self.vertDict[de].removeVizinho(self.vertDict[para])
            self.vertDict[para].removeVizinho(self.vertDict[de])

    def getAresta(self, de, para):
        if de in self.vertDict and para in self.vertDict:
            return (de, para, self.getVertice(de).getPeso(self.vertDict[para]))
        else:
            return None

    def getVertices(self):
        return self.vertDict.keys()

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

    g.removeAresta('a','f')

    for v in g:
        for w in v.getConexoes():
            vid = v.getId()
            wid = w.getId()
            print '(%s, %s, %3d)' %(vid, wid, v.getPeso(w))

    for v in g:
        print 'g.vertDict[%s] = %s' %(v.getId(), g.vertDict[v.getId()])
