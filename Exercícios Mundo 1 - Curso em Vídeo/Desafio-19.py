import random
import sys

print('Programa para escolha aleatória de aluno')

turma = ['João', 'Lucas', 'Fiaspo', "Wilson"]

while True:
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