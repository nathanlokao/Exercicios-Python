import sys

while True:
    sexo = ''

    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite teu sexo de nascença: ').upper())
        
        while sexo != 'M' and sexo != 'F':
            print('Digite uma opção válida no sistema\n')
            break
    
    if sexo == 'M':
        sexo = 'Masculino'
    elif sexo == 'F':
        sexo = 'Feminino'

    print(f'Sexo: {sexo}\n')
    
    escolha = ''

    while escolha != 'S' or 'N':
        escolha = str(input('Deseja continuar? (S/N): ').upper())

        if escolha == 'S':
            print('')
            break
        elif escolha == 'N':
            sys.exit('Encerrando Programa...')
        else:
            print('Digite uma opção válida no sistema\n')