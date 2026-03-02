# Similar ao Desafio 28, tentando realizar sem While True

import random

gambiarra = 0
palpites_certos = 0
palpites_errados = 0

while gambiarra == 0:
    gambiarra_2 = 0

    bot = random.randint(1, 10)

    try:
        escolha = int(input('Digite seu número, entre 0 e 10: '))

        while gambiarra_2 == 0:
            if escolha == bot:
                palpites_certos += 1
                print(f'VOCÊ GANHOU!!!\nEscolha = {escolha}\nBot = {bot}\nPalpites Certos = {palpites_certos}\nPalpites Errados = {palpites_errados}\n')
                gambiarra_2 = 1
            else:
                palpites_errados += 1
                print(f'VOCÊ PERDEU\nEscolha = {escolha}\nBot = {bot}\nPalpites Certos = {palpites_certos}\nPalpites Errados = {palpites_errados}\n')
                gambiarra_2 = 1
    except ValueError:
        print('Valor Inválido\n')