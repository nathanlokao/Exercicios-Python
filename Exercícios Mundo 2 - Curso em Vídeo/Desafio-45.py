import random
import sys

# 31 Vermelho
# 32 Verde
# 33 Amarelo

mao = ['PEDRA', 'PAPEL', 'TESOURA']
bot = ['PEDRA', 'PAPEL', 'TESOURA']

print('^_^ ' * 10)
while True:
    print('\033[33mJogo de Pedra, Papel ou Tesoura\033[m\n')
    
    while True:
        try:
            escolha = int(input('Qual a sua escolha?\n1- PEDRA\n2- PAPEL\n3- TESOURA\n\nDigite a Opção: '))
            if escolha == 1 or escolha == 2 or escolha == 3:
                break
            else:
                print('\n\033[34mDigite uma opção válida\033[m')
                print('^_^ ' * 10)
                print('\033[33mJogo de Pedra, Papel ou Tesoura\033[m\n')
        except ValueError:
            print('\n\033[31mErro: Apenas números\033[m')
            print('^_^ ' * 10)
            print('\033[33mJogo de Pedra, Papel ou Tesoura\033[m\n')

    escolha_mao = mao[escolha - 1]
    escolha_bot = random.choice(bot)

    print(f'\nJOGADOR = {escolha_mao}\nBOT = {escolha_bot}\n')

    if escolha_mao == escolha_bot:
        print('\033[34mEMPATE\033[m')
    elif escolha_mao == 'PEDRA' and escolha_bot == 'TESOURA':
        print('\033[32mVocê ganhou\033[m')
    elif escolha_mao == 'PEDRA' and escolha_bot == 'PAPEL':
        print('\033[31mVocê perdeu\033[m')
    elif escolha_mao == 'PAPEL' and escolha_bot == 'PEDRA':
        print('\033[32mVocê ganhou\033[m')
    elif escolha_mao == 'PAPEL' and escolha_bot == 'TESOURA':
        print('\033[31mVocê perdeu\033[m')
    elif escolha_mao == 'TESOURA' and escolha_bot == 'PEDRA':
        print('\033[31mVocê perdeu\033[m')
    elif escolha_mao == 'TESOURA' and escolha_bot == 'PAPEL':
        print('\033[32mVocê ganhou\033[m')

    while True:
        print('^_^ ' * 10)
        print('')
        pergunta = str(input('\033[34mDeseja continuar jogando? (S/N):\033[m '))

        if pergunta == 'S':
            print('')
            print('^_^ ' * 10)
            break
        elif pergunta == 'N':
            sys.exit('\033[35mEncerrando Programa...\033[m')
        else:
            print('\033[34mCê decida aê!!!\033[m\n')