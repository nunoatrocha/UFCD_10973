def fazer_tshirt(tamanho, frase):
    print(f'Vamos fazer a sua tshirt no tamanho {tamanho} com a seguinte frase: {frase}')

fazer_tshirt("S", "Python é fixe")  # argumentos posicionais
fazer_tshirt(tamanho="S", frase="Python é fixe") # argumentos nomeados

def fazer_tshirt(tamanho="XL", frase="Eu amo Python"):
    print(f'Vamos fazer a sua tshirt no tamanho {tamanho} com a seguinte frase: {frase}')

fazer_tshirt(tamanho="XL")
fazer_tshirt(tamanho="M")
fazer_tshirt(tamanho="S", frase="Python é top")

print('Nuno Rocha')


