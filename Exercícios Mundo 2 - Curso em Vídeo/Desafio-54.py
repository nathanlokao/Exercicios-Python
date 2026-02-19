import datetime

while True:
    maior_idade = 0
    menor_idade = 0
    viajante_tempo = 0

    for i in range(1, 8):
        while True:
            try:
                ano_de_nascimento = int(input(f'Digite o Ano de Nascimento, da {i}° Pessoa: '))
                break
            except ValueError:
                print('Digite apenas números!!!\n')

        idade = (datetime.date.today().year) - ano_de_nascimento
        
        if idade < 0:
            print('Você é um Viajante do Tempo?\n')
            viajante_tempo += 1
        elif idade >= 21:
            print(f'Você tem {idade} anos')
            print('Você é Maior de Idade\n')
            maior_idade += 1
        else:
            print(f'Você tem {idade} anos')
            print('Você é Menor de Idade\n')
            menor_idade += 1
    
    print(f'Total de Pessoas Maiores de Idade: {maior_idade}\nTotal de Pessoas Menores de Idade: {menor_idade}\nTotal de Viajantes do Tempo: {viajante_tempo}\n')
    