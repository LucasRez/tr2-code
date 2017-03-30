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

g.addAresta("WA", "CA1", 4)
g.addAresta("WA", "CA2", 7)
g.addAresta("WA", "IL", 14)
g.addAresta("CA1", "UT", 3)
g.addAresta("CA1", "CA2", 4)
g.addAresta("CA2", "TX", 12)
g.addAresta("UT", "MI", 15)
g.addAresta("UT", "CO", 2)
g.addAresta("CO", "TX", 8)
g.addAresta("CO", "NE", 4)
g.addAresta("NE", "IL", 4)
g.addAresta("IL", "PA", 5)
g.addAresta("PA", "NY", 3)
g.addAresta("PA", "GA", 4)
g.addAresta("PA", "NJ", 2)
g.addAresta("NY", "MI", 1)
g.addAresta("NY", "DC", 3)
g.addAresta("NJ", "MI", 4)
g.addAresta("NJ", "DC", 2)
g.addAresta("GA", "TX", 10)
g.addAresta("DC", "TX", 12)

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
