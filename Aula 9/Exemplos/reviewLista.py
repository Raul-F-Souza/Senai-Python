# Exemplo listas
# Criar uma lista com 4 nomes de alunos

alunosPython = ['Enzo', 'Raul', 'Jonathan', 'Pedro']

# Exibir a lista corretamente
for aluno in alunosPython:
    print(f'Aluno: {aluno}')

print(15*'#')

for i in range(len(alunosPython)):
    print(f'Aluno: {alunosPython[i]}')

print(15*'#')

cursosSenai = ['Java', 'Python', 'Banco de Dados', 'JavaScript']
print(cursosSenai[2])

print(15*'#')

nomeEscola = 'Senai "Nami Jafet"'
print(nomeEscola[3])

print(15*'#')

# Lista de listas
cursoPython = [['Aula 1', 'Aula 2', 'Aula 3', 'Aula 4'], [
    'Tipos de Dados', 'Condicionais', 'Laços de repetição', 'Tuplas']]

print(f'Na {cursoPython[0][0]} de Python : aprendemos {cursoPython[1][0]}')

print(15*'#')

# Exibir todas as aulas e o coteudo dado
for i in range(len(cursoPython[0])):
    print(f'Na {cursoPython[0][i]} de Python aprendemos : {cursoPython[1][i]}')