import sys

while True:
    print('PROGRAMA DE TABUADA')
    try:
        n1 = int(input('Digite um valor (NEGATIVO PARA ENCERRAR EXECUÇÃO): '))

        if n1 < 0:
            break

        for n2 in range(1, 11):
            print(f'{n1} X {n2} = {n1*n2}')
        print('')
    except ValueError:
        print('Valor Digitado Inválido\n')
sys.exit('Encerrando Programa...')