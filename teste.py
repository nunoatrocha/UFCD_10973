"""

numero_favorito = {
    "jorge":[3,7],
    "tania":[4,6],
    "silvia":[10,20]
}



numero_favorito = {
    "jorge":[3,7],
    "silvia":[10,20]
}
for nome, numeros in numero_favorito.items():
    print(f'Os números favoritos {nome} são: ')
    for numero in numeros:
        print(f'{numero}')




numero_favorito = {
    "jorge":2,
    "tania":4,
    "silvia":88,
    "ricardo":2,
    "fatima":88
}


for numero in set(numero_favorito.values()):
    print(numero)



mensagem = input('Escreva a mensagem (para sair digite "sair"): ')
while mensagem != 'sair':
    print(mensagem)
    mensagem = input('Escreva a mensagem: ')


numero_favorito = {
    "jorge":3,
    "tania":4,
    "silvia":10
}


for nome in sorted(numero_favorito.keys()):
    print(nome)




numero = 16
numero_2 = 10
array_1 = [1, 4, 5]
array_2 = [1,2]

if numero > 15:
    print("1")

if array_1:
    print("2")

if len(array_2) == 2:
    print("3")

if len(array_1) + len(array_2) == 5:
    print("4")

if array_1 and array_1[0] == 1:
    print("5")



numero_favorito = {
    "jorge":3,
    "tania":4,
    "fatima":88
}

for nome,  numero in numero_favorito.items():
    print(f'Valor favorito do {nome} é {numero}')


idade = 80

if idade < 12:
        print('O bilhete custa 0€')
elif idade < 40:
        print('O bilhete custa 5€')
elif idade < 80:
        print('O bilhete custa 10€')
else:
    print('O bilhete custa 5€')

    


pessoa = {
    'nome': 'jorge',
    'apelido': 'santos',
    'idade': 31,
    'cidade': 'porto',

}

print(pessoa["nome"])

if pessoa["idade"]>30:
    print("trintão")

if "cidade" in pessoa.keys():
    print("cidade presente")


if "santos" in pessoa.values():
    print("santos presente")




alunos = ["joao","ana","rui","pedro","jorge"]


while "ana" in alunos:
    alunos.remove("ana")

print(alunos)



alunos = ["pedro","jorge","ana","rui"]


if len(alunos) == 0:
    print('A lista alunos não existe')
else:
    for aluno in alunos:
        if aluno == 'pedro':
            print(f'Adeus {aluno}')
        else:
            print(f'Olá {aluno}')


numero_favorito = {
    "jorge":3,
    "tania":4,
    "silvia":10
}

del numero_favorito['silvia']

print(numero_favorito)



mensagem = input('Escreva uma mensagem: ')
print(mensagem)




alunos = ["joao","pedro","jorge","ana","rui"]

for aluno in alunos:
        if aluno == 'pedro':
            print(f'Adeus {aluno}')
        else:
            print(f'Olá {aluno}')



def cidade_distrito(cidade, distrito):
    print(f'Eu sou de {cidade.title()}')
    print(f'A cidade de {cidade.title()} pretence ao distrito de {distrito.title()}')



def letras_grandes(lista):
    for i in range(0, len(lista)):
        lista[i] = lista[i].upper()



utilizadores = ["ana","raquel","admin"]
letras_grandes(utilizadores)
print(utilizadores)




def cidade_distrito(cidade, distrito='porto'):
    print(f'Eu sou de {cidade.title()}')
    print(f'A cidade de {cidade.title()} pretence ao distrito de {distrito.title()}')

cidade_distrito("figueira","coimbra")


def criar_lista(*alimento):
    return list(alimento)


pizza = criar_lista("tomate")
print(pizza)




def despedida(lista_nomes):
    for nome in lista_nomes:
        print(f'Adeus {nome}!')


utilizadores = ["ana","raquel","admin"]
despedida(utilizadores)



def amo_python():
    print('Eu amo python')

amo_python()




def obter_nome_todo(nome, sobre_nome, nome_do_meio=""):
    if nome_do_meio:
        nome = f'{nome.title()} {nome_do_meio.title()} {sobre_nome.title()}'
    else:
        nome = f'{nome.title()} {sobre_nome.title()}'
    return nome

valor = obter_nome_todo("simao","ribeiro")
print(valor)

valor = obter_nome_todo("simao","ribeiro","mendes")
print(valor)




def pessoa(nome, sobrenome, idade=''):
    dicionarario = {
        'nome': nome,
        'sobrenome': sobrenome, 
        }
    if idade:
        dicionarario['idade'] = idade
    return dicionarario


musico1 = pessoa('rui', 'veloso', idade=100)
print(musico1)

musico1 = pessoa('rui', 'veloso')
print(musico1)



def despedida(nome):
    print(f'Adeus {nome}!')

"""


def criar_dicionario(**kargs):
    return kargs

utilizador = criar_dicionario(nome="simao",sobernome="ribeiro",local="Porto",area="python")
print(utilizador)

	
{'nome': 'simao', 'sobernome': 'ribeiro', 'local': 'Porto', 'area': 'python'}
{'nome': 'simao', 'sobernome': 'ribeiro', 'local': 'Porto', 'area': 'python'}