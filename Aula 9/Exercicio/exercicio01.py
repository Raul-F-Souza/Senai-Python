from math import prod
from pickle import TRUE

numeros = []

while TRUE:
    digitado = int(input('Informe um número inteiro (digite "0" para sair): '))

    if digitado != 0:
        numeros.append(digitado)
    elif digitado == 0:
        break

print(f'O maior número dessa lista: {max(numeros)}')
print(f'O menor número: {min(numeros)}')
print(f'A soma de todos os números: {sum(numeros)}')
print(f'A multiplicação de todos os números: {prod(numeros)}')