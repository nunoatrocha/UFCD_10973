import pandas as pd

d = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'Idade': [25, 31, 18, 42, 36],
    'Cidade': ['Porto', 'Lisboa', 'Braga', 'Coimbra', 'Guimarães']
}

df = pd.DataFrame(d)

print(df.head())

print('Nuno Rocha')