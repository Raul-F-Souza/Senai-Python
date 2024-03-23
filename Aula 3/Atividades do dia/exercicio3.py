#Desafio 03: Elabore um programa que peça 3 notas, faça a media e retorne se o aluno foi aprovado ou não

aluno = input('Digite o nome do aluno(a): ')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 5:
    print(f'Aluno(a) {aluno} foi aprovado(a) com uma média de {media}!')
else:
    print(f'Aluno(a) foi reprovado(a) com uma média de {media}')