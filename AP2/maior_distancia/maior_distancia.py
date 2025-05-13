def maior_distancia(grafo):
    def bfs(inicio):
        visitado = []
        for i in range(len(grafo)):
            visitado.append(0)  # Inicializa todos os vértices como não visitados
        
        distancia = []
        for i in range(len(grafo)):
            distancia.append(-1)  # Inicializa todas as distâncias como -1
        
        fila = []
        fila.append(inicio)  # Adiciona o vértice inicial à fila
        visitado[inicio] = 1  # Marca o vértice inicial como visitado
        distancia[inicio] = 0  # A distância do vértice inicial para ele mesmo é 0

        while len(fila) > 0:
            atual = fila[0]
            nova_fila = []
            for i in range(1, len(fila)):
                nova_fila.append(fila[i])
            fila = nova_fila

            for i in range(len(grafo[atual])):
                if grafo[atual][i] != 0 and visitado[i] == 0:  # Verifica se há uma aresta e se o vértice não foi visitado
                    visitado[i] = 1  # Marca o vértice como visitado
                    distancia[i] = distancia[atual] + 1  # Atualiza a distância
                    fila.append(i)  # Adiciona o vértice à fila
        
        return distancia

    max_distancia = 0
    for vertice in range(len(grafo)):
        distancias = bfs(vertice)  # Realiza a BFS a partir de cada vértice
        for i in range(len(distancias)):
            if distancias[i] > max_distancia:
                max_distancia = distancias[i]

    return max_distancia