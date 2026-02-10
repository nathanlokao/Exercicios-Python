# Calculadora de aumento

while True: 
    try:
        salario = float(input('Digite seu salário: '))

        if salario > 1250:
            aumento = salario * 0.10
            salario_final = salario + aumento

            print(f'Salário Atual: R${salario}\nAumento: R${aumento}\nSalario Pós Aumento: R${salario_final}\n')

        elif salario <= 1250:
            aumento = salario * 0.15
            salario_final = salario + aumento

            print(f'Salário Atual: R${salario}\nAumento: R${aumento}\nSalario Pós Aumento: R${salario_final}\n')

        else:
            print('Digite um valor válido\n')
    
    except ValueError:
        print('Digite um valor válido\n')