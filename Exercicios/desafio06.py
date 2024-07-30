#Desafio 05 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesoMaior = 0
pesoMenor = 0
for pessoas in range (5):
    peso = float(input(f'Digite o peso da {pessoas + 1}° pessoa: '))
    if peso == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
        
print(pesoMaior, pesoMenor)