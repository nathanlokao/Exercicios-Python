import random
import sys

print('Programa que sorteia a ordem de Apresentação dos Trabalhos')

turma = ['João', 'Lucas', 'Fiaspo', "Wilson"]

while True:
    ordem_definida = random.sample(turma, k=4)
    print(ordem_definida)

    while True:
        escolha = str(input('Deseja continuar? (S/N)'))

        if escolha == 'S':
            break
        elif escolha == 'N':
            sys.exit('Encerrando Programa...')
        else:
            print('Digite corretamente!!!')