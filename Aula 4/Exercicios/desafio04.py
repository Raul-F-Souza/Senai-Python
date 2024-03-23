#Exercício 02: Elabore um programa que peça um número e retorne sua tabuada.
num = int(input("Digite o numero entre 1 a 10 desejado: "))
for tabuada in range (1, 11):
    print(f'1 X {tabuada} = {num * tabuada}')