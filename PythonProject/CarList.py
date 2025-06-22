class carList:
    def __init__(self):
        self.first = None
        self.last = None

    def addCar(self, xOrigin, yOrigin, xDestination, yDestination):
        if self.first == None:
            self.first = car(xOrigin, yOrigin, xDestination, yDestination)
            self.last = self.first

        else:
            current = self.first
            while current.next != self.last:
                current = current.next

            newCar = car(xOrigin, yOrigin, xDestination, yDestination)
            newCar.prev = current
            self.last = newCar

    def deleteCars(self):
        pass
        #current = self.first

       # while current != None:
            #if current.x == current.xf:



class car:
    def __init__(self, xOrigin, yOrigin, xDestination, yDestination):
        self.x0 = xOrigin
        self.y0 = yOrigin
        self.xf = xDestination
        self.yf = yDestination

        self.x = self.x0
        self.y = self.y0

        self.m = (self.yf - self.y0) / (self.xf - self.x0)
        self.b = self.y0 - (self.m * self.x0)

        #Funcionamiento de nodo
        self.next = None
        self.prev = None

    def updatePos(self):
        self.x = self.x + 1
        self.y = self.m * self.x + self.b