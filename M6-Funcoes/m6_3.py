def funcao_cidade(nome_cidade, nome_pais='portugal'):
    localizacao = f'{nome_cidade.title()}  é localizado em {nome_pais.title()}'
    return localizacao

chamada_1 = funcao_cidade('porto')
print(chamada_1)
chamada_2 = funcao_cidade('roma', 'itália')
print(chamada_2)
chamada_3 = funcao_cidade('kiev', 'ucrânia')
print(chamada_3)

print('Nuno Rocha')