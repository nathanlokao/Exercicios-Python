# Jogo de advinhação

import sys
import random

while True:
    try:
        bot = random.randint(0, 5)

        escolha = int(input('Advinhe o número entre, 0 e 5, que o computador escolheu: '))

        if escolha >= 0 and escolha <= 5 and escolha == bot:
            print('Você acertou o número correto!!!')
        elif escolha < 0 or escolha > 5:
            print('Digite um número entre 0 e 5 apenas')    
        else:
            print('Você não adivinhou o número certo, tente novamente')
    except ValueError:
        print('Digite um número entre 0 e 5 apenas')

    while True:
        pergunta = input('Deseja continuar? S/N ')

        if pergunta == 'S':
            break
        elif pergunta == 'N':
            sys.exit('Encerrando o programa...')
        else:
            print('Digite corretamente')