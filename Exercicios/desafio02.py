times = ('Palmeiras', 'Santos', 'São Paulo', 'Novorizontino', 'São Bernardo', 'Bragantino', 'Inter de Limeira',
         'Ponte Preta', 'Água Santa', 'Corinthians', 'Mirassol', 'Botafogo', 'Portuguesa', 'Guarani', 'Santo André', 'Ituano')

print('Digite "A" para exibir os 3 primeiros colocados')
print('Digite "B" para exibir os 3 últimos colocados')
print('Digite "C" para exibir a lista em ordem alfabetica')
print('Digite "D" para saber a posição do São Paulo')

escolha = input('Digite aqui sua escolha: ')
escolha = escolha.upper()

if escolha == 'A':
    print(times[:3])
elif escolha == 'B':
    print(times[12:])
elif escolha == 'C':
    print(sorted(times))
elif escolha == 'D':
    print(times.index('São Paulo') + 1)
else:
    print('Escolha não identificada, verificar escolha e fazer novamente!')
