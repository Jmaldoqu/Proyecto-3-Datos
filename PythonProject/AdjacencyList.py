# Aristas - arcos:
class DirectedEdge:
    def __init__(self):
        self.end = None
        self.start = None
        self.next = None
        self.kilometers = None
        self.traffic_load = None

class AdjacencyList:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first is None

    def adjacent(self, data):
        current = self.first
        while current is not None:
            if current.end == data:
                return True
            current = current.next
        return False

    def addEdge(self, end, kilometers):
        if not self.adjacent(end):
            node = DirectedEdge()
            node.end = end
            node.kilometers = kilometers
            self.__insert(node)

    def __insert(self, node):
        if self.isEmpty():
            self.first = node
            self.last = node
        elif node.end <= self.first.end:
            node.next = self.first
            self.first = node
        elif node.end >= self.last.end:
            self.last.next = node
            self.last = node
        else:
            current = self.first
            previous = None
            while current is not None and node.end > current.end:
                previous = current
                current = current.next
            node.next = current
            previous.next = node

    def printList(self):
        listString = ""
        temp = self.first
        while temp is not None:
            listString += f"{temp.end}({temp.kilometers}) -> "
            temp = temp.next
        return listString + "None"

    def deleteEdge(self, data):
        if not self.isEmpty() and self.adjacent(data):
            current = self.first
            previous = None

            while current is not None and current.end != data:
                previous = current
                current = current.next

            if current == self.first:
                self.first = self.first.next
                if self.first is None:
                    self.last = None
            elif current == self.last:
                previous.next = None
                self.last = previous
            else:
                previous.next = current.next

    def getAdjacencies(self):
        list = []
        node = self.first

        while node != None:
            token = []
            token.append(node.end)
            token.append(node.kilometers)
            list.append(token)
            node = node.next
        return list
