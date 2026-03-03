while True:
    print('Calculadora Fatorial')
    while True:
        try:
            fatorial = int(input('Digite o Valor Fatorial: '))
            break
        except ValueError:
            print('Digite corretamente\n')
    
    if fatorial < 0:
        print('Não aceitamos Valores Negativos\n')
        continue

    n1 = fatorial
    n2 = fatorial - 1

    while n2 > 0:    

        r = n1 * n2
        print(f'{n1} X {n2} = {r:.2f}')
        
        while True:
            n1 = r
            n2 -= 1
            break
        
    print('')







































    #contador = fatorial
    #resultado_final = 0
    #while contador != 0:
    #    contador -= 1
    #    resultado = fatorial * contador
    #    resultado_final += resultado
    #    print(f'{fatorial} X {contador} = {resultado_final}')
    #    fatorial -= 1