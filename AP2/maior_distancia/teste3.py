import maior_distancia as md 
grafo_matriz3 = [[0, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1, 0]]

print(md.maior_distancia(grafo_matriz3))
# 1. Importa o módulo:
#   Importa a função maior_distancia do arquivo maior_distancia.py e referencia ela como md.maior_distancia.

# 2.Define o grafo:
#   Cria uma matriz de adjacência chamada grafo_matriz3, que representa o grafo.
#   Cada elemento grafo_matriz3[i][j] indica se existe uma aresta entre os vértices i e j:
#       1 significa que existe uma aresta.
#       0 significa que não existe uma aresta.

# 3.Calcular a maior distância:
#   Chama a função md.maior_distancia passando grafo_matriz3 como argumento.
#   A função maior_distancia calcula a maior distância entre dois vértices no grafo (conforme implementado no arquivo maior_distancia.py).

# 4.Exibe o resultado:
#  Imprime o valor retornado pela função maior_distancia, que representa a maior distância entre dois vértices no grafo.
