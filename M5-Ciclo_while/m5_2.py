while True:
    try:
        idade = int(input('Qual a sua idade? '))
        if idade < 3:
            print('O bilhete é gratuito')
        elif idade <= 12:
            print('O preço do bilhete é: 10€')
        else:
            print('O preço do bilhete é: 15€')
        sair = input('Se desejar sair digite [sim] - senão prima qualquer tecla.  ')
        if sair.lower() == 'sim':  # converte sempre para letra pequena
            break
    except ValueError:   # caso não digite um numero imprime esta mensagem
        print('Tem que digitar um número inteiro.')

print('\n\tNuno Rocha\n')