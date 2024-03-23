contagem = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numeroExtenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
                 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
num = int(input('Digite um número de 0 a 10: '))

for i in range(0, len(contagem)):
    if contagem[i] == num:
        print(f'O número escolhido foi: {numeroExtenso[i]}')
