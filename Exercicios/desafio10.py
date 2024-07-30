#Desafio 01: um programa que faça contagem regressiva de 10 a 1 com um atraso de 1 seg na contagem.
import time
for contagem in range(10, -1, -1):
    time.sleep(1)
    print(f'Contagem regressiva para os fogos: {contagem}')