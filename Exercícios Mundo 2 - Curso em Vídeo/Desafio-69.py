import sys

maiores_idade = 0
contador_masculino = 0
contador_feminino = 0
menor_20_anos_feminino = 0

while True:

    while True:
        try:
            idade = int(input('Qual é a sua IDADE: '))
            if idade > 18:
                maiores_idade += 1
            
            if idade < 0:
                print('Não Existe Idade Negativa\n')
                continue
            break
        except ValueError:
            print('Digite Corretamente\n')

    while True:
        sexo = str(input('Qual é o seu SEXO? (M/F): ').upper())

        if sexo == 'M':
            contador_masculino += 1
            break
       
        elif sexo == 'F':
            contador_feminino += 1
            break
        
        else:
            print('Digite uma Opção Válida\n')

    if idade < 20 and sexo == 'F':
        menor_20_anos_feminino += 1

    pergunta = 'placeholder'

    while pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('Deseja Continuar o Programa? (S/N): ').upper())
        if pergunta != 'S' and pergunta != 'N':
            print('Digite uma Opção Válida\n')
            continue

    if pergunta == 'S':
        print('')
        continue

    elif pergunta == 'N':
        print(f'\nPessoa(s) com IDADE acima de 18 Anos = {maiores_idade} Pessoa(s)')
        print(f'Pessoa(s) do SEXO MASCULINO = {contador_masculino} Pessoa(s)')
        print(f'Pessoa(s) do SEXO FEMININO abaixo de 20 Anos = {menor_20_anos_feminino} Pessoa(s)\n')

        sys.exit('Encerrando Programa...')