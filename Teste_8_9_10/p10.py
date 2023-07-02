import numpy as np

def tamanho_matriz(matriz):
    dimensoes = matriz.shape
    return dimensoes
    

#Cria uma função tamanho_matriz() que aceita uma matriz numpy e retorna uma tupla com o tamanho de cada dimensão

print(tamanho_matriz(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
print(tamanho_matriz(np.array([[1, 2], [4, 6], [7, 9]])))