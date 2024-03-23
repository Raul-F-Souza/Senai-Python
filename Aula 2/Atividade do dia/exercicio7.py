# Desafio: crie um programa que peça as notas de um aluno. Em seguida, mostre as duas primeiras notas e sua média.

print('Desafio 07')

nome = str(input('Digite seu nome: '))
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))

print(f'Olá, {nome} !! Suas notas são {nota1 , nota2} que totalizam uma média de {(nota1 + nota2) / 2}')