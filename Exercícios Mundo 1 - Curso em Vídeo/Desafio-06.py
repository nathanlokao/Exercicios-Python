# Dobro, Triplo e Raiz Quadrada
import sys

print(5 * '#','Dobro, Triplo e Raiz Quadrada', 5 * '#')
print('-' * 25)

while True:

    try:
        numero = float(input('Digite um número: '))

        dobro = numero * 2
        triplo = numero * 3
        raiz_quadrada = numero ** (1/2)

        print(f'O dobro de {numero} é: {dobro}')
        print(f'O triplo de {numero} é: {triplo}')
        print(f'A raiz quadrada de {numero} é: {raiz_quadrada:.8}')
        
        break

    except ValueError:
        print('Valor Inválido!!!')
        print('-' * 25)

print('-' * 25)
print('Fim da Execução do Programa')

sys.exit(0)