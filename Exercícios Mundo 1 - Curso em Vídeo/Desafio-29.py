# Calculadora de multa de excesso de velocidade
import sys

while True:
    try:
        velocidade = float(input('Qual foi a velocidade máxima atingida? '))
        velocidade_acima = velocidade - 80
        valor_multa = 7
        multa_final = velocidade_acima * valor_multa

        if velocidade > 80:
            print(f'Você excedeu o limite de velocidade (80 Km/H) em {velocidade_acima:.2f}Km/H')
            print(f'Velocidade Atingida: {velocidade:.2f}Km/H')
            print(f'Valor da multa: R${multa_final:.2f}')
        elif velocidade < 0:
            print('Valor negativo inválido')
        else:
            print('Você está no limite correto da via. Multa não aplicada')
    except ValueError:
        print('Digite um valor válido')

    while True:
        pergunta = input('Deseja continuar? S/N: ')

        if pergunta == 'S':
            break
        elif pergunta == 'N':
            sys.exit('Encerrando o programa...')
        else:
            print('Digite corretamente')