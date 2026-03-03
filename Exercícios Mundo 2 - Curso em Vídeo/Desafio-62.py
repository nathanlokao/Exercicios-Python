import sys

while True:
    
    while True:
        try:
            primeiro_termo = int(input('Digite o valor do Primeiro Termo: '))

            if primeiro_termo < 0:
                print('Não aceitamos Termos Negativos\n')
                continue
            else:                
                break
        except ValueError:
            print('Digite Apenas Valores Numéricos\n')
    
    while True:
        try:
            razao = int(input('Digite o valor da Razão: '))
            
            if razao < 0:
                print('Não aceitamos Termos Negativos\n')
                continue
            else:                
                break
        except ValueError:
            print('Digite Apenas Valores Numéricos\n')

    print(primeiro_termo)
    contador = 1
    iterador = 10

    while contador < iterador:
        r = primeiro_termo + razao
        
        print(r)
        primeiro_termo = r
        contador += 1

        if contador == iterador:
            
            while True:
                try:
                    escolha_int = int(input('\nDeseja quantos termos a mais? '))
    
                    if escolha_int < 0:
                        print('Não aceitamos Termos Negativos')
                        continue
                    elif escolha_int == 0:
                        sys.exit('Encerrando Programa...')
                    else:    
                        while contador < (iterador + escolha_int):
                            r = primeiro_termo + razao 

                            print(r)
                            primeiro_termo = r
                            contador += 1    
                            
                            if contador == (iterador + escolha_int):
                                print('')
                                break
                    break

                except ValueError:
                    print('Digite Apenas Valores Numéricos')
