# Aprovador de Empréstimo Bancário
print('\033[33mAprovador de Empréstimo Bancário\033[m')

while True:
    try:
        valor_casa = float(input('Qual é o valor avaliado do imóvel?: '))
        salario_comprador = float(input('Qual é o salário do comprador?: '))
        anos_financiamento = int(input('Por quantos anos o imóvel será financiado?: '))

        meses_financiamento = anos_financiamento * 12

        prestacao_mensal = valor_casa / meses_financiamento

        print('')

        print(f'Valor do Imóvel: R${valor_casa:.2f}\nSalário do Comprador: R${salario_comprador:.2f}\nDuração do Financiamento: {anos_financiamento} Anos')

        if prestacao_mensal > salario_comprador * 0.30:
            print('\033[31mInfelizmente o Empréstimo foi Negado\033[m\n')
        else:
            print('\033[32mParabéns o Empréstimo foi Aprovado\033[m\n')
    except ValueError:
        print('Digite um valor válido\n')