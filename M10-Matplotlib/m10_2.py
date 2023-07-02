import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('dados.csv')
sns.barplot(x='name', y='value', hue='type', data=data)
plt.show()

print('Nuno Rocha')