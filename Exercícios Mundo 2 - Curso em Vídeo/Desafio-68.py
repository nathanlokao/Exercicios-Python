import sys
import random

contador_vitórias = 0

while True:

    print('JOGO DE ÍMPAR OU PAR\n')

    while True:
        try:
            jogada_usuario = int(input('Faça uma jogada (Entre 0 até 10): '))

            if jogada_usuario > 10:
                print('APENAS NÚMEROS ENTRE 0 ATÈ 10\n')
            elif jogada_usuario < 0:
                print('APENAS NÚMEROS ENTRE 0 ATÈ 10\n')
            else:
                break
        
        except ValueError:
            print('Digite APENAS Números Inteiros\n')

    jogada_bot = random.randint(1, 10)

    total = jogada_usuario + jogada_bot


    while True:
        try:
            escolha = int(input('Escolha ÍMPAR(1) ou PAR(2) ? '))


            if escolha == 1:
                print(f'\nJOGADA DO USUÁRIO = {jogada_usuario}')
                print(f'JOGADA DO BOT = {jogada_bot}')
                print(f'SOMA DAS JOGADAS = {total}\n')

                if not (total % 2) == 0:
                    contador_vitórias +=1
                    print('VOCÊ GANHOU')
                    print(f'VITÓRIAS CONSECUTIVAS = {contador_vitórias}\n')
                    break
                else:
                    print('VOCÊ PERDEU')
                    print(f'VITÓRIAS CONSECUTIVAS = {contador_vitórias}\n')
                    sys.exit('Encerrando Programa...')


            elif escolha == 2:
                print(f'\nJOGADA DO USUÁRIO = {jogada_usuario}')
                print(f'JOGADA DO BOT = {jogada_bot}')
                print(f'SOMA DAS JOGADAS = {total}\n')

                if (total % 2) == 0:
                    contador_vitórias +=1
                    print('VOCÊ GANHOU')
                    print(f'VITÓRIAS CONSECUTIVAS = {contador_vitórias}\n')
                    break
                else:
                    print('VOCÊ PERDEU')
                    print(f'VITÓRIAS CONSECUTIVAS = {contador_vitórias}\n')
                    sys.exit('Encerrando Programa...')

            else:
                print('Digite um Opção Válida\n')

        except ValueError:
            print('Digite um Opção Válida\n')
        
