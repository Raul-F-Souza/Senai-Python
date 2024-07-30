#Perguntar se o aluno gosta do curso de Python Sabadão

while True:
    resposta = input('Você gosta de Python? (s/n): ')
    resposta = resposta.upper
    if resposta == 'S':
        print('Resposta correta!\n Fim do programa...')
        break