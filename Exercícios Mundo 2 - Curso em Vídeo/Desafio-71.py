print('Banco do Monopoly\n')

dinheiro_conta = 5000

while True:
    try:
        dinheiro_sacar = int(input('Qual valor deseja sacar? R$'))

        if dinheiro_sacar > dinheiro_conta:
            print('Não é possível sacar valores ACIMA do Saldo Disponível\n')
            continue
        elif dinheiro_sacar < 0:
            print('Insira um Valor Válido\n')
            continue
        break
    except ValueError:
        print('Insira um Valor Válido\n')

cedula_50 = dinheiro_sacar // 50
dinheiro_sacar = dinheiro_sacar - (cedula_50 * 50)

cedula_20 = dinheiro_sacar // 20
dinheiro_sacar = dinheiro_sacar - (cedula_20 * 20)

cedula_10 = dinheiro_sacar // 10
dinheiro_sacar = dinheiro_sacar - (cedula_10 * 10)

cedula_01 = dinheiro_sacar // 1
dinheiro_sacar = dinheiro_sacar - (cedula_01 * 1)

print(f'Total de Cédulas de R$50, retiradas = {cedula_50} Cédulas')
print(f'Total de Cédulas de R$20, retiradas = {cedula_20} Cédulas')
print(f'Total de Cédulas de R$10, retiradas = {cedula_10} Cédulas')
print(f'Total de Cédulas de R$1, retiradas = {cedula_01} Cédulas\n')

print('Nós agradecemos pela confiança em nossa Instituição Financeira.\nVOLTE SEMPRE!!!')