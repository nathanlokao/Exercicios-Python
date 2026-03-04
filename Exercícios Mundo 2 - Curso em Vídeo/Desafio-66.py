import sys

contador = 0
total = 0

while True:
    numero = int(input('Digite um Número Inteiro (999 para Encerrar o Programa): '))
    if numero == 999:
        break
    contador += 1
    total += numero

print(f'\nNÚMEROS DIGITADOS = {contador}')
print(f'SOMA DOS NÚMEROS = {total}')
sys.exit('Encerrando Programa...')