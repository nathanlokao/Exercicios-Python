# Impressão do número real, mas mostrando apenas o valor inteiro

import math

print('Programa removedor da parte decimal de números com virgula')

while True:
    try:
        numero = float (input ('Digite um número real: '))

        print(math.trunc(numero))
    
    except ValueError:
        print('\nDigite um valor válido!!!\n')