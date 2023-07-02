import csv

with open('file_vendas.csv', encoding='utf8') as c:
    conteudo = csv.reader(c)
    next(conteudo)
    for linha in conteudo:
        total = float(linha[1]) * int(linha[2])
        print(f'O valor da venda de {linha[0]} foi de: {total:.2f}€')

print('Nuno Rocha')