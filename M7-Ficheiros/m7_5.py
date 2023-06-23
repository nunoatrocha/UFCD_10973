import json

filename = 'produtos.json'

with open(filename, encoding='utf-8') as p:
    pop_data = json.load(p)

for item in pop_data:
    total = item['Preço'] * item['Quantidade Vendida']
    print(f"A venda de {item['Produto']} foi: {total}€")

print('Nuno Rocha')