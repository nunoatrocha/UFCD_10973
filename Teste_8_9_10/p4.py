import numpy as np

def ordenar_soma(matriz):
    somas = np.sum(matriz, axis=1)
    matriz_ordenada = matriz[np.argsort(somas)]
    return matriz_ordenada


#Cria uma função ordenar_soma() que aceita uma matriz e ordena pela soma de cada linha
print(ordenar_soma(np.array([[7, 8],[2, 3], [3, 1]])))


"""
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""