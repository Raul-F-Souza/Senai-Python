#Usuario e senha
usuario = 'root'
senha = 1234

usuarioDigitado = input('Digite do usuario: ')
senhaDigitada = int(input('Digite a sua senha: '))

if usuario == usuarioDigitado:
    print('Usuário correto!')

    if senha == senhaDigitada:
        print('Senha correta! \nAcesso permitido')
    else:
        print('Senha incorreta!')
else:
    print('Usuario incorreto!')