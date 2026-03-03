import sys

# Seria Bacana uma Opção de Resetar o Programa.

total = 0
numeros_digitados = 0

while True:
    try:
        numero = int(input('Digite um Valor Inteiro (999 para SAIR): '))
        
        if numero == 999:
            sys.exit('Encerrando Programa...')
        elif numero > 999:
            print('Não Aceitamos Entradas Acima de 998\n')
            continue
        elif numero < -998:
            print('Não Aceitamos Entradas Abaixo de -998\n')
            continue
        else:    
            total += numero
            print(f'Total = {total}')
            
            numeros_digitados += 1
            print(f'Números Digitados = {numeros_digitados}\n')

    except ValueError:
        print('Apenas Números Inteiros\n')
        continue
