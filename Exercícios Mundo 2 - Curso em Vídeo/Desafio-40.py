while True:
    try:
        while True:
            n1 = float(input('Digite o valor da Nota1: '))
            if n1 < 0:
                print('Número negativo inválido\n')
                continue
            else:
                break
        
        while True:
            n2 = float(input('Digite o valor da Nota2: '))
            if n2 < 0:
                print('Número negativo inválido\n')
                continue
            else:
                break
        
        media = (n1 + n2) / 2

        if media >= 7:
            print(f'Nota1 = {n1}\nNota2 = {n2}\nMedia = {media}')
            print('Parabéns vocé foi APROVADO!!!\n')
        elif media >= 5:
            print(f'Nota1 = {n1}\nNota2 = {n2}\nMedia = {media}')
            print('Você entrou em RECUPERAÇÃO\n')
        else:
            print(f'Nota1 = {n1}\nNota2 = {n2}\nMedia = {media}')
            print('Infelizmente você foi REPROVADO\n')
    except ValueError:
        print('Digite um valor válido\n')