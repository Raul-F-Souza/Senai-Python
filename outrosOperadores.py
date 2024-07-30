#Operador de Potência
usuario = int(input('Digite um valor a ser pontecializado: '))
valor = int(input('Digite a potência do valor anterior: '))
potencia = usuario ** valor

print(usuario , '**' , valor , '=' , potencia)

#Operador Modulo
usuario = int(input('Digite um valor para descobrir seu modulo: '))
valor = int(input('Digite o valor desejado: '))
modulo = usuario % valor

print(usuario, '%', valor, '=' , modulo)

#Operador de divisão inteira
usuario = int(input('Digite um valor a ser divido: '))
valor = int(input('Digite um divisor: '))
divisaoInteira = usuario // valor

print(usuario, '//', valor , '=' , divisaoInteira)