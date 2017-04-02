from grafo import Grafo
import dijkstra

g = Grafo()

g.addVertice("WA")
g.addVertice("CA1")
g.addVertice("CA2")
g.addVertice("UT")
g.addVertice("CO")
g.addVertice("NE")
g.addVertice("IL")
g.addVertice("TX")
g.addVertice("GA")
g.addVertice("PA")
g.addVertice("MI")
g.addVertice("NY")
g.addVertice("DC")
g.addVertice("NJ")

g.addAresta("WA", "CA1",1)
g.addAresta("WA", "CA2",1)
g.addAresta("WA", "IL", 1)
g.addAresta("CA1", "UT", 1)
g.addAresta("CA1", "CA2", 1)
g.addAresta("CA2", "TX", 1)
g.addAresta("UT", "MI", 1)
g.addAresta("UT", "CO", 1)
g.addAresta("CO", "TX", 1)
g.addAresta("CO", "NE", 1)
g.addAresta("NE", "IL", 1)
g.addAresta("IL", "PA", 1)
g.addAresta("PA", "NY", 1)
g.addAresta("PA", "GA", 1)
g.addAresta("PA", "NJ", 1)
g.addAresta("NY", "MI", 1)
g.addAresta("NY", "DC", 1)
g.addAresta("NJ", "MI", 1)
g.addAresta("NJ", "DC", 1)
g.addAresta("GA", "TX", 1)
g.addAresta("DC", "TX", 1)

print("Nos disponiveis: WA, CA1, CA2, UT, CO, NE, IL, TX, GA, PA, MI, NY, DC, NJ")
A = raw_input("Insira o no de partida:")
B = raw_input("Insira o no de destino:")
k = int(raw_input("Insira o numero de menores caminhos (1 para dijkstra): "))

if k == 1 or k == None:
    path = dijkstra.dijkstra(g, A, B)
    print "menor caminho:", path

elif k > 1:
    paths = dijkstra.kpaths(g, A, B, k)
    print "para k = %d foram encontrados os %d menores caminhos:" % (k, len(paths))
    for p in paths:
        print p

else:
    print ("Valor de caminhos invalido")
