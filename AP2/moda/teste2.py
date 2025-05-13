import moda as md
lista2 = [i//10 for i in range(100, -10, -1)] + [10,11,12,13,14,5,16,17,18,19]
print(md.moda(lista2))

# 1.Importa o módulo:
#   Importa a função moda do arquivo moda.py e referenciá-la como md.moda.

# 2.Define a lista:
#   Cria uma lista chamada lista2 contendo os valores [i//10 for i in range(100, -10, -1)] + [10,11,12,13,14,5,16,17,18,19].
# 3.Calcula a moda:
#   Chama a função md.moda passando lista2 como argumento.
#   A função moda calcula o(s) valor(es) que mais se repetem na lista.

# 4.Exibe o resultado:
#   Imprimie o valor retornado pela função moda, que representa o(s) número(s) mais frequente(s) na lista.