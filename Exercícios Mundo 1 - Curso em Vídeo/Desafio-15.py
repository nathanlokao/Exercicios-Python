# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

while True:
    try:
        kilometragem = float(input('Digite a quantidade de Kilometros, percorridos: '))
        if kilometragem < 0:
            print('Kilometragem negativo, inválido\n')
            continue
        
        valor_kilometragem = kilometragem * 0.15

        dias_alugado = int(input('Quantos dias o carro está alugado?: '))
        if dias_alugado < 0:
            print('Não existe dia negativo\n')
            continue
        else:
            print('')
        
        valor_aluguel = dias_alugado * 60

        valor_total = valor_kilometragem + valor_aluguel

        print(f'Kilometragem Percorrida: \033[34m{kilometragem:.2f}KM\033[m\nTempo do Aluguel: \033[32m{dias_alugado} dias\033[m\nValor a Pagar: \033[33mR${valor_total:.2f}\033[m\n')

    except ValueError:
        print('Digite um valor válido\n')