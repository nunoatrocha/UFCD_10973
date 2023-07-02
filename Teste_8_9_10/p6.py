import pandas as pd

def remover_coluna(dataframe, coluna):
    df = pd.DataFrame(dataframe)
    return df.drop(coluna, axis=1)

dic = {
    'Nome': ['João', 'Maria', 'José', 'Lucas', 'Ana'], 
    'Idade': [25, 30, 35, 40, 45], 
    'Salário': [1000, 2000, 3000, 4000, 5000]
}

#Assume que o dicionário 'dic' já existe. Cria uma função remover_coluna() que aceita um dataframe e nome da coluna. A função retorna o dataframe sem a coluna.


print(remover_coluna(dic, 'Salário'))
print(remover_coluna(dic, 'Idade'))

