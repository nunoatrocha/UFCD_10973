import json
def quantidade_total_vendas(nome_do_ficheiro_json):
    with open(nome_do_ficheiro_json) as j:
        reader = json.load(j)
    total = 0
    for linha in reader:
        total += linha['Quantidade Vendida']
    return total


q_total = quantidade_total_vendas("vendas.json")         
print(q_total)