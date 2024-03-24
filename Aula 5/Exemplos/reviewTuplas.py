listaProdutos = ('Arroz' , 3.50 , 'Feijao' , 2.50 , 'Oleo' , 1.50 , 'Goiabada' , 1)

#Exibindo somente o Arroz
print(listaProdutos[0])

#Exibindo todos os valores
print(listaProdutos)

print('-'*15)

for i in range(len(listaProdutos)):
    print(listaProdutos[i])
    
print('-'*15)
    
#Exibir somente os produtos cadastrados
for i in range(0, len(listaProdutos), 2):
    print(listaProdutos[i])

print('-'*15)

#Exibir o preço da goiabada
for i in range(0, len(listaProdutos)):
    if listaProdutos[i] == 'Goiabada':
        print(f'O preço da goiabada é {listaProdutos[i+1]}')
        
print('-'*15)

#Adicionar mais um item na tupla - não é possível
#Excluir - não é possível