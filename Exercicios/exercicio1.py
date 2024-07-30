#Crie um programa em Python que peça a temperatura em graus Celsius e o programa deve exibir a temperatura em graus Fahrenheit

print('Desafio 01')
print(40*'-')

temperaturaCelsius = float(input('Digite sua temperatura em graus Celsius: '))
conversaoTemperatura = (temperaturaCelsius * 1.8) + 32

print(f'A conversão de sua temperatura em grau Celsius para Fahrenheit será: {conversaoTemperatura}')