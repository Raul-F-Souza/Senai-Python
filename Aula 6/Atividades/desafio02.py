#Crie um programa em python que possua e exiba uma lista que contenha números pares de 0 a 60
listaPares = []

for par in range(2, 61, 2):
    listaPares.append(par)

print(listaPares)