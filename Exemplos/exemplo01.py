produtos = [['banana' , 'maça'] , [3.5 , 5.5]]

# Qual o preço da banana?
for indice in range(len(produtos[0])):
    if produtos[0][indice] == 'banana':
        print(f'O preço do abacate é: {produtos[1][indice]}')
        break
else:
    print(f'Banana não está disponivel para venda')

# Qual o preço do abacate?
for indice2 in range(len(produtos[0])):
    if produtos[0][indice2] == 'abacate':
        print(f'O preço do abacate é: {produtos[1][indice2]}')
        break
    else:
        print(f'Abacate não está disponivel para venda')