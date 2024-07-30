while True:
    resposta = input('Gostaria de ver a tabuada de algum numero? (s/n): ')
    if resposta.upper() == 'S':
        num = int(input("Digite o numero entre 1 a 10 desejado: "))
        for tabuada in range (1, 11):
            print(f'1 X {tabuada} = {num * tabuada}')
    else:
        print('Tenha um bom dia!')
        break
    