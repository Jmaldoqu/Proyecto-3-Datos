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
root.title("Pryecto III - ADS")
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

myfont = font.Font(family="Times", size=10, weight="bold") #Cambiar después


# Botones --------------------------------------------------------------------------------------------------------------
b_createEdge = tk.Button(window, text = "Create Edge", command = newEdge, font = myfont)
b_createEdge.grid(row = 4, column = 0, padx = 5, pady = 5)

b_deleteVertex = tk.Button(window, text = "Delete Vertex", command = deleteVertex, font = myfont)
b_deleteVertex.grid(row = 6, column = 0, padx = 5, pady = 5)

b_deleteEdge = tk.Button(window, text = "Delete Edge", command = deleteEdge, font = myfont)
b_deleteEdge.grid(row = 8, column = 0, padx = 5, pady = 5)


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
node_y_label.grid(row = 11, column = 43, padx = 5, pady = 5)
entry_node_y = tk.Entry(window, font = myfont, width = 15)
entry_node_y.grid(row = 11, column = 44, padx = 5, pady = 5)

b_create_node = tk.Button( window, text="Create node", command=lambda: newVertex( entry_node_name.get(), int(entry_node_x.get()), int(entry_node_y.get())), font=myfont, width=37 )
b_create_node.grid(row = 13, column = 42, padx = 5, pady = 5, columnspan = 3, rowspan = 3)


#Simulación de carritos ------------------------------------------------------------------------------------------------

cars = carList()

cars = carList()
current_car = None  # Carrito actual que se está moviendo
car_path = []       # Lista de coordenadas [(x0, y0), (x1, y1), (x2, y2), ...]

def getNodeByName(name):
    current = graph_1.first
    while current:
        if current.data == name:
            return current
        current = current.next
    return None

def simulateCarPath(path):
    global car_path, current_car
    car_path = []

    for i in range(len(path)):
        node = getNodeByName(path[i])
        if node:
            car_path.append((node.x, node.y))

    if len(car_path) >= 2:
        x0, y0 = car_path[0]
        x1, y1 = car_path[1]
        current_car = car(x0, y0, x1, y1)
        current_car_index = 1
        moveCar(current_car_index)

def moveCar(index):
    global current_car, car_path

    if not current_car:
        return

    outputCanva.delete("cars")
    current_car.updatePos()
    outputCanva.create_oval(current_car.x - 5, current_car.y - 5,
                            current_car.x + 5, current_car.y + 5,
                            fill="red", tags="cars")

    # ¿Llegó al destino?
    if abs(current_car.x - current_car.xf) < 2 and abs(current_car.y - current_car.yf) < 2:
        if index + 1 < len(car_path):
            x0, y0 = car_path[index]
            x1, y1 = car_path[index + 1]
            current_car = car(x0, y0, x1, y1)
            outputCanva.after(50, lambda: moveCar(index + 1))
        else:
            current_car = None  # Terminó
    else:
        outputCanva.after(20, lambda: moveCar(index))

def carSimulation():
    path = graph_1.dijkstra(entry_origin.get(), entry_destination.get())
    if len(path) >= 2:
        simulateCarPath(path)

b_simulate = tk.Button(window, text="Simulate Cars", command=carSimulation, font=myfont)
b_simulate.grid(row=10, column=0, padx=5, pady=5)


root.mainloop()

