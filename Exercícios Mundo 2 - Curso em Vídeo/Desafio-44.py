while True:
    while True:
        try:
            valor_produto = float(input('Digite o Preço do Produto: R$'))
            if valor_produto < 0:
                print('\nDigite um valor positivo\n')
            else:
                break
        except ValueError:
            print('\nDigite um valor numérico\n')
    
    while True:
        try:
            escolha = int(input('\n1- À Vista Dinheiro/Cheque: 10% de Desconto\n2- À Vista no Cartão: 5% de Desconto\n3- Em até 2x no Cartão: Preço Normal\n4- 3x ou mais no Cartão: 20% de Juros\n\nQual opção deseja?: '))

            if escolha == 1:
                desconto_10 = valor_produto - (valor_produto * 0.10)
                print(f'Valor do Produto = R${valor_produto:.2f}\nValor do Produto (Desconto 10%) = R${desconto_10:.2f}\n')
            elif escolha == 2:
                desconto_5 = valor_produto - (valor_produto * 0.05)
                print(f'Valor do Produto = R${valor_produto:.2f}\nValor do Produto (Desconto 5%) = R${desconto_5:.2f}\n')
            elif escolha == 3:
                valor_parcelado2x = valor_produto / 2
                print(f'Valor do Produto = R${valor_produto:.2f}\nValor do Produto (Parcelado em 2x) = R${valor_parcelado2x:.2f}\n')
            elif escolha == 4:
                parcelas = int(input('Deseja quantas parcelas?: '))
                if parcelas >= 3:
                    juros_20 = valor_produto + (valor_produto * 0.20)
                    print(f'Valor do Produto = R${valor_produto:.2f}\nValor do Produto (Juros 20%) = R${juros_20:.2f}\nParcelado em {parcelas}x = R${juros_20 / parcelas:.2f}\n')
                else:
                    print('\nQuantidade de parcelas inválido')
            else:
                print('\nDigite uma Opção Válida')
        except ValueError:
            print('\nDigite um valor númerico')