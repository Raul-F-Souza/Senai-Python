#Pedir para o usuário digitar dois números e então exibir o maior e o menor
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#Verificando o maior e o menor número
if num1 > num2:
    print(f'O número {num1} é maior que {num2}')
elif num1 < num2:
    print(f'O número {num2} é maior que o {num1}')
else:
    print(f'O número {num1} e {num2} são iguais')