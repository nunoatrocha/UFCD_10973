import csv

def lista_cabecalho_csv(nome_do_ficheiro_csv):
    with open(nome_do_ficheiro_csv) as f:
        reader = csv.reader(f)
        cabecalho = next(reader)
        return cabecalho


cabecalho = lista_cabecalho_csv("vendas.csv")
print(cabecalho)