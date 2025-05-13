import moda as md
lista3 = [(i**3)//1000 for i in range(100, -10, -1)]
print(md.moda(lista3))

# 1.Importa o módulo:
#   Importa a função moda do arquivo moda.py e referenciá-la como md.moda.

# 2.Define a lista:
#   Cria uma lista chamada lista3 contendo os valores [(i**3)//1000 for i in range(100, -10, -1)].

# 3.Calcula a moda:
#   Chama a função md.moda passando lista3 como argumento.
#   A função moda calcula o(s) valor(es) que mais se repetem na lista.

# 4.Exibe o resultado:
#   Imprimie o valor retornado pela função moda, que representa o(s) número(s) mais frequente(s) na lista.