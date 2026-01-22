# Desafio-07 TUNADO

# Programa de cadastro, visualização e aplicação de notas para alunos

alunos = {}
id = 1

def adicionar_aluno():
    global id
    
    while True:
        
        nome = str(input('Digite o nome do Aluno: ').strip())

        if nome.replace(' ', '').isalpha():
            break
        
        else:
            print('Digite apenas caractéres válidos!!!')

    alunos[id] = {
            'nome' : nome,
            'n1' : 0,
            'n2' : 0,
            'media' : 0,
        }    
    id += 1

def visualizar_alunos():

    if alunos == {}:
        print('Não possui alunos cadastrados')

    for id, dados in alunos.items():
   
        print(f'Identificador: {id}, Nome do aluno: {dados['nome']}, Nota 1: {dados['n1']}, Nota 2: {dados['n2']}, Media: {dados['media']}')

def adicionar_notas(): 
        
    while True:
        
        if alunos == {}:
            print('Alunos não cadastrados')
            break

        global id
        x = int(input('Escolha o aluno para atribuir as notas (ID): '))

        if x not in alunos:
                print('Valor de Identificação Inválido')
        
        else:
            n1 = float(input('Digite a primeira nota: '))
            if n1 < 0:
                print('Número Negativo Inválido')
                break

            n2 = float(input('Digite a segunda nota: '))
            if n2 < 0:
                print('Número Negativo Inválido')
                break

            media = (n1 + n2) / 2

            alunos[x]['n1'] = n1
            alunos[x]['n2'] = n2
            alunos[x]['media'] = media

            print(f'A primeira nota: {n1} (ADICIONADO COM SUCESSO)')
            print(f'A segunda nota: {n2} (ADICIONADO COM SUCESSO)')
            print(f'A media das notas: {media} (ADICIONADO COM SUCESSO)')
            break

while True:

    print('-' * 8, 'Menu', '-' * 8)
    print('1 - Adicionar Aluno\n2 - Visualizar Alunos Matriculados\n3 - Atribuir Nota\n0 - Encerrar Programa')
    
    try:
        escolha = int(input('Qual funcionalidade deseja executar?:\n'))

        if escolha == 1 :    
            adicionar_aluno()

        elif escolha == 2 :
            visualizar_alunos()

        elif escolha == 3 :
            adicionar_notas()

        elif escolha == 0 :
            break
    
    except ValueError:
        print('Digita direito ae!!! >:/')
