# Revisão Função
def desenvolvimento ():
    nomeDesenvolvedor = 'Raul Souza'
    linguagem = 'Python'
    print(f"Desenvolvedor do programa : {nomeDesenvolvedor}")
    print(f"Linguagem de desenvolvimento : {linguagem}")
    
def curso():
    nomeCurso = 'Programação em Python'
    return nomeCurso
    
print("Informações sobre o programa:")
desenvolvimento()

nomeCurso = curso()

print(f"O nome do curso é {nomeCurso}")