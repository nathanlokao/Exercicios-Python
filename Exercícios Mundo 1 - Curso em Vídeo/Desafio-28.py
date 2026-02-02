# Jogo de advinhação

import random

bot = random.randint(0, 5)

escolha = int(input('Advinhe o número entre, 0 e 5, que o computador escolheu: '))

if escolha == bot:
    print('Voc')
