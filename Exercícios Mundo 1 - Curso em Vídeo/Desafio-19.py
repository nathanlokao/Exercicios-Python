import random
import sys

print('Programa para escolha aleatória de aluno')

while True:
    turma = ['João', 'Lucas', 'Fiaspo', "Wilson"]
    escolhido = random.choice(turma)
    print(escolhido)

    while True:
        continuar = str(input('Deseja refazer a escolha? (S/N): '))

        if continuar == 'S':
            break
        elif continuar == 'N':
            sys.exit('Encerrando programa...')
        else:
            print('Digite um valor válido!!!\n')

sys.exit('Encerrando programa...')