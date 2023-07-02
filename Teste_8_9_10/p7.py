import pandas as pd

dic = {
    'Nome': ['João', 'Maria', 'José', 'Lucas', 'Ana'], 
    'Idade': [25, 30, 35, 40, 45], 
    'Salário': [1000, 2000, 3000, 4000, 5000]
    }

df = pd.DataFrame(dic)




#Assume que o dicionário 'dic' já existe, cria uma variavel 'df' que é conversão do dicionário para pandas dataframe.


print(df[["Idade","Salário"]])