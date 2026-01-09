'''
~~~~~ Primeira versão escrita. Achei ela meio crua, então quis deixar um pouco melhor. ~~~~~

print('##############<-Calculadora de Média das Notas do Bimestre->##############\n')

nota_1 = float(input('Digite a valor da Primeira Prova:\n'))
print(nota_1, '\n')

nota_2 = float(input('Digite a valor da Segunda Prova:\n'))
print(nota_2, '\n')

nota_3 = float(input('Digite a valor da Terceira Prova:\n'))
print(nota_3, '\n')

nota_4 = float(input('Digite a valor da Quarta Prova:\n'))
print(nota_4, '\n')

soma = nota_1 + nota_2 + nota_3 + nota_4

media = soma / 4

print(f'A média é: {media}')
'''


# Segunda versão do código, desta vez utilizando lista, for, try, except, if, else, elif e etc.
 
# Olhando em retrospecto daria para substituir o For por While para corrigir a limitação de 9999 notas
# E deixar ilimitado, para o infinito e além.

# Ótima tarefa para relembrar conceitos básicos de lógica de programação

print('##############<-Calculadora de Média das Notas do Bimestre->##############\n')

notas_bimestre = []

if not notas_bimestre:

    provas = 1

    for notas in range(1,9999):
        try:
            x = float(input(f'Digite a nota da {provas}°prova: '))
            notas_bimestre.append(x)
            provas += 1
        
        except ValueError:
            print('Digite um valor válido!')

        pergunta = input('Deseja adicionar mais provas? (yes/no): ')
        if pergunta == 'no':
            break
        
        elif pergunta == 'yes':
            continue 
        
        elif pergunta != "yes" and "no": 
            print ('Escreve algo aê pô!')
            pergunta = input('Deseja adicionar mais provas? (yes/no): ')
    
soma = sum(notas_bimestre)

try:
    media = soma / (len(notas_bimestre))
    print(f'A média é: {media}')

except ZeroDivisionError:
    print('Não foi adicionada nenhuma prova')

quit()