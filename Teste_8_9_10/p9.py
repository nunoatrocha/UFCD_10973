import numpy as np

def soma_array(array, condicao):
    elementos_selecionados = array[condicao]
    soma = np.sum(elementos_selecionados)
    return soma

#Cria uma função soma_array() que aceita um array e uma condição, retorna a soma do array consuante a condição
arr = np.array([1, 2, 3, 4, 5])
print(soma_array(arr,arr>2))