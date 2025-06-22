from AdjacencyList import AdjacencyList

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.list = AdjacencyList()
        self.next = None
        self.x = 0
        self.y = 0

class Graph:
    def __init__(self):
        self.first = None
        self.last = None

    def GraphIsEmpty(self):
        return self.first is None

    def NodeExists(self, element):
        temp = self.first
        while temp is not None:
            if temp.data == element:
                return True
            temp = temp.next
        return False

    def DirectedEdge(self, origin, destination, weight):
        if self.NodeExists(origin) and self.NodeExists(destination):
            position = self.first

            while position.data != origin:
                position = position.next
            position.list.addEdge(destination, weight)

    def deleteEdge(self, origin, destination):

        if self.NodeExists(origin) and self.NodeExists(destination):
            position = self.first

            while position.data != origin:
                position = position.next

            position.list.deleteEdge(destination)

    def newNode(self, element, px, py):
        if not self.NodeExists(element):
            node = GraphNode(element)
            node.data = element
            node.x = px
            node.y = py
            node.list = AdjacencyList()

            if self.GraphIsEmpty():
                self.first = node
                self.last = node
            elif element <= self.first.data:
                node.next = self.first
                self.first = node
            elif element > self.last.data:
                self.last.next = node
                self.last = node
            else:
                current = self.first
                last = None

                while current is not None and element > current.data:
                    last = current
                    current = current.next
                node.next = current
                last.next = node

    def printGraph(self):
        cadena = ""
        temporal = self.first
        while temporal is not None:
            cadena += str(temporal.data) + " -> " + temporal.list.printList() + "\n"
            temporal = temporal.next
        return cadena


    def deleteVertex(self, vertex):
        if self.NodeExists(vertex):
            temp = self.first

            while temp.next is not None:
                self.deleteEdge(temp.data, vertex)
                temp = temp.next

            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                current = self.first
                previous = None

                while current != None and not vertex.next.data != current.data:
                    previous = current
                    current = current.next

                if current == self.first:
                    delete_node = self.first
                    self.first = self.first.next
                    delete_node.next = None

                elif current == self.last:
                    previous.next = None
                    self.last = previous

                else:
                    previous.next = current.next
                    current.next = None



    def getVertices(self):
        list = []
        node = self.first

        while node != None:
            token = []
            token.append(node.data)
            token.append(node.x)
            token.append(node.y)
            token.append(node.list.getAdjacencies())
            list.append(token)
            node = node.next
        return list

    def dijkstra(self, start, end):
        dist = {}
        prev = {}
        unvisited = []

        node = self.first
        while node:
            dist[node.data] = float("inf")
            prev[node.data] = None
            unvisited.append(node.data)
            node = node.next

        dist[start] = 0

        while unvisited:
            current = min(unvisited, key=lambda n: dist[n])
            unvisited.remove(current)

            if current == end:
                break

            node = self.first
            while node and node.data != current:
                node = node.next

            for adj in node.list.getAdjacencies():
                alt = dist[current] + float(adj[1])
                if alt < dist[adj[0]]:
                    dist[adj[0]] = alt
                    prev[adj[0]] = current

        path = []
        step = end
        while step:
            path.insert(0, step)
            step = prev[step]

        return path
