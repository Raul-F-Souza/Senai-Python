#Medias utilizando elif: pedir 2 notas para o usuário. media for maior que 6, aprovado; se for menor que 4, reprovado; se media entre 4 e 5, recuperacao
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(int('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media > 6: 
    print('Aprovado!')
elif media < 4:
    print('Reprovado!')
else:
    print('Recuperação!')