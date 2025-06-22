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

class car:
    def __init__(self, xOrigin, yOrigin, xDestination, yDestination):
        self.x0 = xOrigin
        self.y0 = yOrigin
        self.xf = xDestination
        self.yf = yDestination

        self.x = self.x0
        self.y = self.y0

        if xOrigin != xDestination:
            self.m = (self.yf - self.y0)/(self.xf - self.x0)
        else:
            self.m = 0

        self.b = self.y0 - (self.m * self.x0)

        self.next = None
        self.prev = None

    def updatePos(self):
        dx = self.xf - self.x
        dy = self.yf - self.y

        distancia = (dx ** 2 + dy ** 2) ** 0.5
        if distancia == 0:
            return

        velocidad = 3
        vx = velocidad * dx / distancia
        vy = velocidad * dy / distancia

        self.x += vx
        self.y += vy


