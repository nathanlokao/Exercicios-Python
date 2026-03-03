import sys

while True:

    total = 0
    numeros_digitados = 0
    maior = 0
    menor = 0
    
    while True:
        try:
            numero = int(input('Digite um Valor Inteiro: '))

            if numeros_digitados == 0:
                menor = numero
                maior = numero
                
                total += numero
                numeros_digitados += 1

            else:
                if numero < menor:
                    menor = numero
                
                if numero > maior:
                    maior = numero
                
                total += numero
                numeros_digitados += 1
            
            while True:
                continuar = str(input('Deseja Continuar (S/N)? ').upper())
                
                if continuar == 'N':
                    print(f'MAIOR = {maior}')
                    print(f'MENOR = {menor}')
                    print(f'MEDIA = {total / numeros_digitados:.2f}\n')

                    sys.exit('Encerrando Programa...')        

                elif continuar == 'S':
                    print('')
                    break

                else:
                    print('Digite uma Opção Válida\n')        

        except ValueError:
            print('Apenas Números Inteiros\n')
            continue

