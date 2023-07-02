import pandas as pd

d = {
    'Nome': ['João', 'Maria', 'José', 'Lucas', 'Ana'], 
    'Idade': [25, 30, 35, 40, 45], 
    'Salário':[1000, 2000, 3000, 4000, 5000]
    }

df = pd.DataFrame(d)

col_selecionadas = ['Nome', 'Salário']
df_selecionado = df[col_selecionadas]
print(df_selecionado.head(3))

print('Nuno Rocha')