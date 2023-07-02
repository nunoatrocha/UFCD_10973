import numpy as np
def soma_linhas(arr):
    return np.sum(arr, axis=1)
    

#Cria uma função soma_linhas() que aceita uma matriz numpy e retorna a soma de linhas
print(soma_linhas(np.array([[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 5]])))
