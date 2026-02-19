primeiro_termo = int(input('Digite o valor do Primeiro Termo: '))
razao = int(input('Digite o valor da Razão: '))

lista_vazia = []

for i in range(primeiro_termo, 99999999, razao):
    lista_vazia.append(i)

for n in range(0,10):
    print(lista_vazia[n])