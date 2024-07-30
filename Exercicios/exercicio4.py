#Desafio 04: Elabore um programa que leia dois números e retorne qual é o maior e o menor deles.

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

if numero1 > numero2:
    print(f'O maior número é {numero1} e o menor número é {numero2}')
else:
    print(f'O maior número é {numero2} e o menor é {numero1}')
if numero1 == numero2:
    print(f"O número {numero1} e {numero2} são iguais.")