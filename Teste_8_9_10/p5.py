import numpy as np

def multi_colunas(arr):
    return  np.prod(arr, axis=0)

#Cria uma função multi_colunas() que aceita uma matriz numpy e retorna a multiplicação das colunas
print(multi_colunas(np.array([[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 5]])))