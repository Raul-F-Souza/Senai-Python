#Desafio 04 - Crie um programa que leia a idade de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maiores = 0
for idade in range(7):
    idade = int(input(f'Digite a idade da {idade + 1}° pessoa: '))
    if idade >= 18:
        maiores += 1

print(f'Temos um total de {maiores} pessoas maiores de idade.')