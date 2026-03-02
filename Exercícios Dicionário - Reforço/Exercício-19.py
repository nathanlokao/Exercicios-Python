# Crie um dicionário com 3 alunos e suas notas.
# Mostre qual aluno tem a maior nota.

sala_de_aula = [
    {'nome' : 'joão', 'nota' : 7},
    {'nome' : 'lucas', 'nota' : 9},
    {'nome' : 'caua', 'nota' : 11},
]

nome_melhor_aluno = ''
maior_nota = 0

for aluno in sala_de_aula:
    nota_loop_atual = aluno['nota']

    if nota_loop_atual > maior_nota:
        maior_nota = nota_loop_atual
        nome_melhor_aluno = aluno['nome']

print(f'SALA DE AULA\n{list(sala_de_aula)}\n')
print(f'ALUNO QUE ATINGIU A MAIOR NOTA\nNome: {nome_melhor_aluno}\nNota = {maior_nota:.2f}')