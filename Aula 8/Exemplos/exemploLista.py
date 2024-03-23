listaBancos = ['Banco do Brasil' , 'Nubank' , 'Inter']
#Exibir a lista
print(listaBancos)
print('#'*20)

for banco in listaBancos:
    print(banco)
    
print('#'*20)

for i in range(len(listaBancos)):
    print(listaBancos[i])
    
print('#'*20)

#Adicionar elementos a lista
listaBancos.append('Itau')
listaBancos.append('C6')
for banco in listaBancos:
    print(banco)

print('#'*20)

