#Desafio 05: Elabore um programa que simule um seáforo e que exiba a ação com base na resposta

print('Simulador simples de semáforo')
print(40*'-')

resposta = input('Digite uma das seguintes cores: verde, amarelo, vermelho e descubra o que deve ser feito: ')
#convertendo para minusculo
resposta = resposta.lower()
#convertendo para maiusculo
resposta = resposta.upper()
#apenas primeira em maisculo
resposta = resposta.capitalize()

if resposta == 'Verde':
    print('Tudo certo, siga em frente!')
elif resposta == 'Amarelo':
    print('Diminua a velocidade e pare.')
elif resposta == 'Vermelho':
    print('Pare e aguarde o semáforo mudar para a cor verde.')
else:
    print('Resposta invalida!')