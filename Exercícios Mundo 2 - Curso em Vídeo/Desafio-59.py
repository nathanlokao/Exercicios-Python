import sys

while True:

    while True:
        try:
            n1 = float(input('Digite o Valor de N1: '))
            break
        except ValueError:
            print('\nDigite Apenas Números\n')

    while True:
        try:
            n2 = float(input('Digite o Valor de N2: '))
            print('')
            break
        except ValueError:
            print('\nDigite Apenas Números\n')

    while True:
            try:
                escolha = int(input('MENU DE OPERAÇÕES\n[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\n'))
                
                if escolha == 1:
                    print(f'N1 = {n1}\nN2 = {n2}\nResultado SOMA = {n1 + n2}\n')
                elif escolha == 2:
                    print(f'N1 = {n1}\nN2 = {n2}\nResultado MULTIPLICAÇÂO = {n1 * n2}\n')
                elif escolha == 3:
                    if n1 > n2:
                        print(f'N1 = {n1}\nN2 = {n2}\nResultado MAIOR = {n1}\n')
                    elif n1 < n2:
                        print(f'N1 = {n1}\nN2 = {n2}\nResultado MAIOR = {n2}\n')
                    elif n1 == n2:
                        print(f'N1 = {n1}\nN2 = {n2}\nResultado MAIOR = EMPATE\n')
                elif escolha == 4:
                    print('')
                    break
                elif escolha == 5:
                    sys.exit('Encerrando Programa...')
                else:
                    print('\nDigite uma opção válida\n')
            except ValueError:
                print('\nDigite Apenas Números\n')