def maior_distancia(grafo):
    def bfs(inicio):
        visitado = []
        for i in range(len(grafo)):
            visitado.append(0)  
        
        distancia = []
        for i in range(len(grafo)):
            distancia.append(-1) 
        
        fila = []
        fila.append(inicio)  
        visitado[inicio] = 1  
        distancia[inicio] = 0 
        while len(fila) > 0:
            atual = fila[0]
            nova_fila = []
            for i in range(1, len(fila)):
                nova_fila.append(fila[i])
            fila = nova_fila

            for i in range(len(grafo[atual])):
                if grafo[atual][i] != 0 and visitado[i] == 0:  
                    visitado[i] = 1  
                    distancia[i] = distancia[atual] + 1  
                    fila.append(i)  
        
        return distancia

    max_distancia = 0
    for vertice in range(len(grafo)):
        distancias = bfs(vertice)  
        for i in range(len(distancias)):
            if distancias[i] > max_distancia:
                max_distancia = distancias[i]

    return max_distancia
