#Crie uma lista que leia do teclado 3 nomes de carros
#Logo após, exiba corretamenta os carros digitado

#for para criar
listaCarro = []

for i in range(3):
    carro = input(f'Digite o nome do {i + 1}° carro: ')
    listaCarro.append(carro)

#For Para exibir
for carro in listaCarro:
    print(carro)