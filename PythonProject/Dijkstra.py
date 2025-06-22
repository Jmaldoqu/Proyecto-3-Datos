def dijkstra(grafo, inicio):
    distancias = {}
    visitados = {}
    predecesores = {}

    # Inicializar distancias y visitados
    temporal = grafo.primero
    while temporal is not None:
        distancias[temporal.dato] = float('inf')
        visitados[temporal.dato] = False
        predecesores[temporal.dato] = None
        temporal = temporal.siguiente

    distancias[inicio] = 0

    for _ in range(len(distancias)):
        # Seleccionar el nodo no visitado con la menor distancia
        nodo_actual = None
        menor_distancia = float('inf')
        for nodo, distancia in distancias.items():
            if not visitados[nodo] and distancia < menor_distancia:
                menor_distancia = distancia
                nodo_actual = nodo

        if nodo_actual is None:
            break

        visitados[nodo_actual] = True

        # Actualizar las distancias de los nodos adyacentes
        temporal = grafo.primero
        while temporal.dato != nodo_actual:
            temporal = temporal.siguiente

        adyacente = temporal.lista.primero
        while adyacente is not None:
            if not visitados[adyacente.destino]:
                nueva_distancia = distancias[nodo_actual] + adyacente.peso
                if nueva_distancia < distancias[adyacente.destino]:
                    distancias[adyacente.destino] = nueva_distancia
                    predecesores[adyacente.destino] = nodo_actual
            adyacente = adyacente.siguiente

    return distancias, predecesores

def obtener_ruta(predecesores, inicio, destino):
    ruta = []
    actual = destino
    while actual is not None:
        ruta.insert(0, actual)
        actual = predecesores[actual]
    if ruta[0] == inicio:
        return ruta
    else:
        return None  # No hay ruta entre inicio y destino

