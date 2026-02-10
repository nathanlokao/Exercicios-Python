# Verificador de Ano Bissexto

while True:
    try:
        ano = int(input('Digite o ano: '))

        if ano >= 0:
            if (ano % 4 == 0 and ano % 100 != 0):
                print(f'O ano {ano} é bissexto')
            
            elif ano % 400 == 0: # ANO CENTENÁRIO
                print(f'O ano {ano} é bissexto')
            
            else:
                print(f'O ano {ano} NÃO é bissexto')
        else:
            print('Não existe ano negativo')
    except ValueError:
        print('Digite um valor válido')