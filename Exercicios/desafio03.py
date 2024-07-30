#Crie um programa em Python que possua uma lista com os números entre 30 e 50 e exiba a soma desses números.
listaNumeros = []
soma = 0

for num in range(30, 51):
    listaNumeros.append(num)
print(listaNumeros)
print('#'*25)

for sum in listaNumeros:
    soma += sum
    
print(soma)
