from grafo import Grafo
import dijkstra

g = Grafo()

pesos = True

print "O grafo utilizado para o programa a seguir segue em anexo na imagem nsfnet.jpg\n"

res = raw_input("Voce deseja o grafo com pesos?(S/n): ")

if res == 'n' or res == 'N':
    pesos = False

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

if pesos:
    print "Usando grafo com pesos"
    g.addAresta("WA", "CA1", 9)
    g.addAresta("WA", "CA2", 5)
    g.addAresta("WA", "IL", 15)
    g.addAresta("CA1", "UT", 4)
    g.addAresta("CA1", "CA2", 2)
    g.addAresta("CA2", "TX", 7)
    g.addAresta("UT", "MI", 5)
    g.addAresta("UT", "CO", 6)
    g.addAresta("CO", "TX", 4)
    g.addAresta("CO", "NE", 4)
    g.addAresta("NE", "IL", 5)
    g.addAresta("IL", "PA", 7)
    g.addAresta("PA", "NY", 2)
    g.addAresta("PA", "GA", 8)
    g.addAresta("PA", "NJ", 2)
    g.addAresta("NY", "MI", 4)
    g.addAresta("NY", "DC", 2)
    g.addAresta("NJ", "MI", 8)
    g.addAresta("NJ", "DC", 1)
    g.addAresta("GA", "TX", 5)
    g.addAresta("DC", "TX", 9)
else:
    print "Usando grafo sem pesos"
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
    print A, B
    path = dijkstra.dijkstra(g, A, B)
    print "\nMenor caminho:", path

elif k > 1:
    paths = dijkstra.kpaths(g, A, B, k)
    print "\nPara k = %d foram encontrados os %d menores caminhos:" % (k, len(paths))
    for p in paths:
        print p

else:
    print ("Valor de caminhos invalido")
