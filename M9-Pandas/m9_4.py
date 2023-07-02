import pandas as pd

d = {
    'Nome': ['João', 'Maria', 'José', 'Lucas', 'Ana'], 
    'Idade': [25, 30, 35, 40, 45], 
    'Salário':[1000, 2000, 3000, 4000, 5000]
}

df = pd.DataFrame(d)

print(f"Média dos salários: {df['Salário'].mean()}")
print(f"Mediana dos salários: {df['Salário'].median()}")

print('Nuno Rocha')