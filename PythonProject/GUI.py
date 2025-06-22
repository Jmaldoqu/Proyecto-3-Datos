import random

from Graph import Graph
from CarList import carList, car


from tkinter import *
import tkinter as tk
import tkinter.font as font

def newVertex(name, x, y):
    graph_1.newNode(name, x, y)
    drawVertices()

def newEdge():
    origin = entry_origin.get()
    destination = entry_destination.get()
    weight = entry_weight.get()

    graph_1.DirectedEdge(origin, destination, weight)
    drawVertices()
    #print(graph_1.printGraph())

def deleteVertex():
    origin = entry_origin.get()
    graph_1.deleteVertex(origin)
    drawVertices()
    #print(graph_1.printGraph())

def deleteEdge():
    origin = entry_origin.get()
    destination = entry_destination.get()
    graph_1.deleteEdge(origin, destination)
    drawVertices()

def drawVertices():
    outputCanva.delete("all")
    verticesList= graph_1.getVertices()

    for vertex in verticesList:
        drawEdges(vertex,verticesList)
        outputCanva.create_oval(vertex[1] - 25, vertex[2] - 25, vertex[1] + 25, vertex[2] + 25, fill="blue")
        outputCanva.create_text(vertex[1], vertex[2], text=vertex[0], fill="white", font="arial")


def drawArrow(x1, y1, x2, y2, weight):

    #No se está usando:
    if x1<x2:
        rdx = -30
    else:
        rdx = 30

    outputCanva.create_line([x1,y1], [x2, y2], arrow = tk.LAST, fill="white", width=3)
    outputCanva.create_text((x1 + x2)//2,((y1+y2)//2)-20, text=weight, fill="white", font="arial")

def drawEdges(vertex, verticesList):
    origin = vertex[0]
    x = vertex[1]
    y = vertex[2]
    end = vertex[3]

    for e in end:
        for n in verticesList:
            if e[0] == n[0]:
                drawArrow(x,y,n[1],n[2],e[1])



# Ventana - GUI
root = tk.Tk()
root.title("Proyecto III - ADS")
window = tk.Frame(root, width = 1200, height = 620)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

for i in range(60):
    window.grid_columnconfigure(i, weight=1, minsize=10)
    window.grid_rowconfigure(i, minsize=10)

#window.pack_propagate(False)
window.grid_propagate(False)
window.grid()

graph_1 = Graph()
#verticesConsecutive = 1

myfont = font.Font(family="Helvetica", size=8, weight="bold") #Cambiar después


# Botones --------------------------------------------------------------------------------------------------------------
b_createEdge = tk.Button(window, text = "Create Edge", command = newEdge, font = myfont)
b_createEdge.grid(row = 4, column = 1, padx = 5, pady = 5)

b_deleteVertex = tk.Button(window, text = "Delete Vertex", command = deleteVertex, font = myfont)
b_deleteVertex.grid(row = 6, column = 1, padx = 5, pady = 5)

b_deleteEdge = tk.Button(window, text = "Delete Edge", command = deleteEdge, font = myfont)
b_deleteEdge.grid(row = 8, column = 1, padx = 5, pady = 5)


#Labels

label_origin = tk.Label(window, text = "Origin", font = myfont)
label_origin.grid(row = 4, column = 3, padx = 0, pady = 0)

label_destination = tk.Label(window, text = "Destination", font = myfont)
label_destination.grid(row = 4, column = 7, padx = 0, pady = 0)

label_weight = tk.Label(window, text = "Kilometers", font = myfont)
label_weight.grid(row = 4, column = 12, padx = 0, pady = 0)


#Entries
entry_origin = tk.Entry(window, font = myfont, width = 10)
entry_origin.grid(row = 4, column = 4, padx = 5, pady = 5)

entry_destination = tk.Entry(window, font = myfont, width = 10)
entry_destination.grid(row = 4, column = 8, padx = 5, pady = 5)

entry_weight = tk.Entry(window, font = myfont, width = 10)
entry_weight.grid(row = 4, column = 13, padx = 5, pady = 5)

outputCanva = Canvas(window, width = 1000, height = 450, background = "grey")
outputCanva.grid(row = 6, column = 3, padx = 0, pady = 0, columnspan = 35, rowspan = 35)


#Crear nodo:
node_name_label = tk.Label(window, text = "Node Name:", font = myfont)
node_name_label.grid(row = 6, column = 43, padx = 5, pady = 5)

entry_node_name = tk.Entry(window, font = myfont, width = 15)
entry_node_name.grid(row = 6, column = 44, padx = 5, pady = 5)

node_x_label = tk.Label(window, text = "X:", font = myfont)
node_x_label.grid(row = 8, column = 43, padx = 5, pady = 5)
entry_node_x = tk.Entry(window, font = myfont, width = 15)
entry_node_x.grid(row = 8, column = 44, padx = 5, pady = 5)


node_y_label = tk.Label(window, text = "Y:", font = myfont)
node_y_label.grid(row =10, column = 43, padx = 5, pady = 5)
entry_node_y = tk.Entry(window, font = myfont, width = 15)
entry_node_y.grid(row = 10, column = 44, padx = 5, pady = 5)

b_create_node = tk.Button( window, text="Create node", command=lambda: newVertex( entry_node_name.get(), int(entry_node_x.get()) , int(entry_node_y.get())), font=myfont, width=37 )
b_create_node.grid(row = 11, column = 42, padx = 5, pady = 5, columnspan = 3, rowspan = 3)


#Simulación de carritos ------------------------------------------------------------------------------------------------

cars = carList()

cars = []

class CarState:
    def __init__(self, path):
        self.index = 1
        self.path = path
        x0, y0 = path[0]
        x1, y1 = path[1]
        self.car = car(x0, y0, x1, y1)

    def update(self):
        self.car.updatePos()

        if abs(self.car.x - self.car.xf) < 2 and abs(self.car.y - self.car.yf) < 2:
            self.index += 1
            if self.index < len(self.path):
                x0, y0 = self.path[self.index - 1]
                x1, y1 = self.path[self.index]
                self.car = car(x0, y0, x1, y1)
            else:
                return False
        return True

def getNodeByName(name):
    current = graph_1.first
    while current:
        if current.data == name:
            return current
        current = current.next
    return None

def getCoordsPath(path):
    coords = []
    for nodeName in path:
        node = getNodeByName(nodeName)
        if node:
            coords.append((node.x, node.y))
    return coords

def carSimulation():
    path = graph_1.dijkstra(entry_origin.get(), entry_destination.get())
    coords = getCoordsPath(path)
    if len(coords) >= 2:
        new_car = CarState(coords)
        cars.append(new_car)

def randomCarSimulation():
    nodeList = graph_1.getVertices()
    nodeNames = [n[0] for n in nodeList]

    origin = random.choice(nodeNames)
    destination = random.choice(nodeNames)

    while origin == destination:
        destination = random.choice(nodeNames)

    path = graph_1.dijkstra(origin, destination)
    coords = getCoordsPath(path)

    if len(coords) >= 2:
        new_car = CarState(coords)
        cars.append(new_car)


def spawnMultipleCars1(count=5):
    nodeList = graph_1.getVertices()
    nodeNames = [n[0] for n in nodeList]

    for _ in range(count):
        if len(nodeNames) < 2:
            return  # No hay suficientes nodos

        origin = random.choice(nodeNames)
        destination = random.choice(nodeNames)
        while destination == origin:
            destination = random.choice(nodeNames)

        path = graph_1.dijkstra(origin, destination)
        coords = getCoordsPath(path)

        if len(coords) >= 2:
            new_car = CarState(coords)
            cars.append(new_car)

def spawnMultipleCars(count=5):
    for i in range(0, count):
        randomCarSimulation()

def animateCars():
    outputCanva.delete("cars")
    for c in cars[:]:
        still_moving = c.update()
        outputCanva.create_oval(c.car.x - 5, c.car.y - 5,
                                c.car.x + 5, c.car.y + 5,
                                fill="red", tags="cars")
        if not still_moving:
            cars.remove(c)
    outputCanva.after(20, animateCars)

animateCars()


b_simulate = tk.Button(window, text="Simulate Cars", command=carSimulation, font=myfont)
b_simulate.grid(row=10, column=1, padx=5, pady=5)

b_simulate = tk.Button(window, text="Random Cars", command=randomCarSimulation, font=myfont)
b_simulate.grid(row=11, column=1, padx=5, pady=10)

b_multi = tk.Button(window, text="Multiple Cars", command=lambda: spawnMultipleCars(5), font=myfont)
b_multi.grid(row=12, column=1, padx=5, pady=5)


root.mainloop()

