def ordenamiento_seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]  # Intercambia los elementos

# Uso
mi_lista = [64, 25, 12, 22, 11]
ordenamiento_seleccion(mi_lista)
print(mi_lista)  # Salida: [11, 12, 22, 25, 64]
