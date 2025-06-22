from Graph import Graph

g = Graph()
g.newNode("San José")
g.newNode("Cartago")
g.newNode("Alajuela")

g.DirectedEdge("Alajuela", "Cartago", 5)
g.DirectedEdge("San José", "Alajuela", 3)

print(g.printGraph())
