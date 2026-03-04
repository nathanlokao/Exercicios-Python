import sys

primeira_compra = True
total_compras = 0
produtos_acima_mil = 0
produto_mais_barato = [] 

while True:

    print('MERCADINHO DO BAIRRO')

    while True:
        nome_produto = str(input('Nome do Produto: ')).strip()
        
        if not nome_produto.replace(' ', '').isalpha():
            print('Digite o Nome do Produto, corretamente\n')
            continue
        else:
            break

    while True:
        try:
            preco_produto = float(input('Preço do Produto: '))

            if preco_produto < 0:
                print('Preço Negativo Inválido\n')
                continue
            
            if primeira_compra == True:
                preco_mais_barato = preco_produto
                produto_mais_barato = [nome_produto]
                primeira_compra = False

            elif preco_produto == preco_mais_barato:
                produto_mais_barato.append(nome_produto)

            elif preco_produto < preco_mais_barato:
                preco_mais_barato = preco_produto
                produto_mais_barato = [nome_produto]
                
            if preco_produto > 1000:
                produtos_acima_mil += 1

            total_compras += preco_produto
            break
        except ValueError:
            print('Valor Inválido\n')

    while True:
        continuar = str(input('Deseja Continuar? (S/N): ')).upper()

        if continuar == 'S':
            print('')
            print('-' * 20)
            break
        elif continuar == 'N':
            print(f'\nTOTAL DA COMPRA = R${total_compras}')
            print(f'QUANTIDADE DE PRODUTOS ACIMA DE R$1000 = {produtos_acima_mil}')
            print(f'PRODUTO(s) MAIS BARATO(s) = {produto_mais_barato}')
            print(f'PREÇO MAIS BARATO = {preco_mais_barato}\n')

            sys.exit('Encerrando Programa...')
        else:
            print('Digite uma Opção Válida\n')









 #if preco_produto < preco_mais_barato:
                #    preco_mais_barato = preco_produto
                #    produto_mais_barato = nome_produto

                #elif preco_produto == preco_mais_barato:
                #    produto_mais_barato.append(nome_produto)