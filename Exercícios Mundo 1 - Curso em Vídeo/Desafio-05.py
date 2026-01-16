# Número Antecessor,  Atual e Sucessor

import sys

print('{:=^50}'.format('Número Antecessor,  Atual e Sucessor'))

try:
    numero = int(input('Digite um número inteiro: '))
    print(f'{numero - 1}<=={numero}==>{numero + 1}')

except ValueError: 
    print('Valor Inválido!!!')

sys.exit(0)