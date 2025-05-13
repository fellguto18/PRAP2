def moda(lista):
    frequencias = []
    valores_unicos = []
    for i in range(len(lista)):
        encontrado = False
        for j in range(len(valores_unicos)):
            if lista[i] == valores_unicos[j]:
                frequencias[j] += 1
                encontrado = True
                break
        if not encontrado:
            valores_unicos.append(lista[i])
            frequencias.append(1)
    max_frequencia = 0
    for i in range(len(frequencias)):
        if frequencias[i] > max_frequencia:
            max_frequencia = frequencias[i]
    modas = []
    for i in range(len(frequencias)):
        if frequencias[i] == max_frequencia:
            modas.append(valores_unicos[i])
    if len(modas) == len(valores_unicos):
        return None
    return modas