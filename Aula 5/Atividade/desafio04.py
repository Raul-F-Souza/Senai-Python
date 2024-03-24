valores = (int(input('Digite o 1° valor: ')),
           int(input('Digite o 2° valor: ')),
           int(input('Digite o 3° valor: ')),
           int(input('Digite o 4° valor: '))
           )

print('-'*15)

print('Digite "A" para saber quantas vezes o número "9" apareceu')
print('Digite "B" para saber em que posição foi digitado o primeiro "3"')
print('Digite "C" para saber quais foram os números pares')

escolha = input('Digite sua escolha: ')
escolha = escolha.upper()

if escolha == 'A':
    print(f'O número 9 aparece {valores.count(9)} vezes')
elif escolha == 'B':
    for i in range(0, len(valores)):
        if valores[i] == 3:
            print(f'A posição do número 3 é {valores.index(valores[i + 1])}')
elif escolha == 'C':
    print('Os números pares digitados foram:')
    for num in valores:
        if num % 2 == 0:
            print(num)
else:
    print('Escolha não identificada, por favor verificar e fazer novamente!')
