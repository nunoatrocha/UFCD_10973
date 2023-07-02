import pandas as pd

def soma_coluna(dict, nome):
    df = pd.DataFrame(dict)
    return df[nome].sum()

dic = {
    'Nome': ['João', 'Maria', 'José', 'Lucas', 'Ana'], 
    'Idade': [25, 30, 35, 40, 45], 
    'Salário': [1000, 2000, 3000, 4000, 5000]
    }

#Assume que o dicionário 'dic' já existe. Cria uma função soma_coluna() que aceita um dataframe e nome da coluna. A função retorna a soma da coluna.


print(soma_coluna(dic, 'Salário'))  # 15000
print(soma_coluna(dic, 'Idade'))    # 175