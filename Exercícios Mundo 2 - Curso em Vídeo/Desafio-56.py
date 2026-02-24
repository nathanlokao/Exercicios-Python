# ATIVIDADE EM PROCESSO DE DESENVOLVIMENTO

import sys

pessoas = {}
id = 1

print('\033[33mPrograma de Lista de Pessoas\033[m\n')

# Repetição de entrada para até 4 Pessoas:
for pessoa in range(1, 5):
   
    while True:
        nome = input(('Digite seu Nome: ').strip())

        if nome.replace(' ', '').isalpha():
            break
        else:
            print('\nValor Inválido\n')

    while True:
        try:
            idade = int(input('Digite sua Idade: '))
            if idade < 0:
                print('Apenas Números Positivos\n')
            else:
                break
        except ValueError:
            print('\nValor Inválido\n')

    while True:
        sexo = input('Digite seu Sexo de Nascimento (H ou M)?: ')
        print('')
        
        if sexo == 'H' or sexo == 'M':
            break
        else:
            print('Valor Inválido\n')
            continue

    pessoas[id] = {
        'nome' : nome,
        'idade' : idade,
        'sexo' : sexo
    }

    id += 1

print('---' * 20)

# Listagem das Pessoas:
for id, pessoa in pessoas.items():
    print(f'Identificador: {id}, Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}')

print('')

# Média de Idade do Grupo:
media_idade = ((pessoas[1]['idade']) + (pessoas[2]['idade']) + (pessoas[3]['idade']) + (pessoas[4]['idade'])) / 4
print(f'Média das Idades = {media_idade:.2f}\n')

print('---' * 20)

# Nome do Homem mais Velho:

if all(pessoa['sexo'] != 'H' for pessoa in pessoas.values()):
    print('Não tem Homem na Lista\n')
else:
    variavel_seguradora_nome = 'Todos possuem a mesma Idade'
    variavel_seguradora_idade = 0

    for x in range(1, 5):
        if pessoas[x]['sexo'] == 'H':
            if pessoas[x]['idade'] > variavel_seguradora_idade:
                variavel_seguradora_nome = pessoas[x]['nome']
                variavel_seguradora_idade = pessoas[x]['idade']

    print(f'Nome do Homem mais Velho = {variavel_seguradora_nome}\nIdade = {variavel_seguradora_idade}\n')

print('---' * 20)

# Quantia de Mulheres Menores que 20 Anos

quantia_mulheres = 0

if all(pessoa['sexo'] != 'M' for pessoa in pessoas.values()):
    print('Não tem Mulher na Lista\n')
else:
    for x in range(1, 5):
        if pessoas[x]['sexo'] == 'M' and pessoas[x]['idade'] < 20:
            quantia_mulheres += 1

    print(f'Há {quantia_mulheres} Mulheres com Menos de 20 Anos\n')

sys.exit('Encerrando Programa...')