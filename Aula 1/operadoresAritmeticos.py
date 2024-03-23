#Desafio da aula: elaborar um código simples que permita o usuário escolher valores para as operações, mostrando o resultado de forma individual.

#Operador Soma
print(' **** SOMA **** ')
valorSoma = int(input('Digite um valor para a soma: '))
somador = int(input('Digite o valor a ser somado: '))
soma = valorSoma + somador

print(valorSoma , '+' , somador , '=' , soma)

#Operador Subtração
print(' **** SUBTRAÇÃO **** ')
valorSubtracao = int(input('Digite um valor a ser subtraido: '))
subtrair = int(input('Digite um valor a subtrair: '))
subtracao = valorSubtracao - subtrair

print(valorSubtracao , '-' , subtrair , '=' , subtracao)

#Operador Multiplicação
print(' **** MULTIPLICAÇÃO **** ')
valorMultiplicacao = int(input('Digite um valor a ser multiplicado: '))
multiplicador = int(input('Digite um muultiplicador: '))
multiplicacao = valorMultiplicacao * multiplicador

print(valorMultiplicacao , '*' , multiplicador , '=' , multiplicacao)

#Operador Divisãos
print('**** DIVISÃO **** ')
valorDivisao = int(input('Digite um valor a ser dividido: '))
divisor = int(input('Digite um divisor: '))
divisao = valorDivisao / divisor

print(valorDivisao, '/' , divisor , '=' , divisao)

#Testes Pessoais
#print('Resultado da soma' , soma, 'Resultado da subtração' , subtracao , 'Resultado da divisão' , divisao , 'Resultado da multiplicação' , multiplicacao)
#print('Resultado da divisão de' , usuario , 'por' , divisor , 'é' , divisao)