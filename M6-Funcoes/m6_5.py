def criar_carro(marca, modelo, **kargs):
    carro = {}
    carro['marca'] = marca
    carro['modelo'] = modelo
    for key, value in kargs.items():
        carro[key] = value
    return carro

carro = criar_carro("mercedes","a200",cor="cinzento", desportivo=True)
print(carro)

print('Nuno Rocha')