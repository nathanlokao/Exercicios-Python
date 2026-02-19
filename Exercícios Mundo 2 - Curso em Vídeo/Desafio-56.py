# ATIVIDADE EM PROCESSO DE DESENVOLVIMENTO

pessoas = {}
id = 1

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

# Listagem das Pessoas:
for id, pessoa in pessoas.items():
    print(f'Identificador: {id}, Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}')

print('')

# Média de Idade do Grupo:
media_idade = ((pessoas[1]['idade']) + (pessoas[2]['idade']) + (pessoas[3]['idade']) + (pessoas[4]['idade'])) / 4
print(f'Média das Idades = {media_idade:.2f}')

# Nome do Homem mais Velho:
lista_idades = []

for x in range(1, 5):
    if pessoa[x]['sexo'] == 'H':
        lista_idades.append(pessoa[x]['idade'])
    else:
        print('Não há homens no Grupo')
    