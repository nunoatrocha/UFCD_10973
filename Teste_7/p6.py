import csv
def quantidade_total_vendas(nome_do_arquivo_csv):
    with open(nome_do_arquivo_csv, 'r') as arquivo:
        reader = csv.DictReader(arquivo)
        quantidade_total = 0
        for linha in reader:
            quantidade_vendida = int(linha['Quantidade Vendida'])
            quantidade_total += quantidade_vendida
    return quantidade_total

q_total = quantidade_total_vendas("vendas.csv")         
print(q_total)


