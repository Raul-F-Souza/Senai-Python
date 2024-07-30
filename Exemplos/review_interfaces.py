# Importando biblioteca padrâo de sistema
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

# iniciação padrão para aplicações
app = QApplication(sys.argv) # Aplicando biblioteca do sistema ao aplicativo
janela = QWidget()
janela.resize(400, 600)
janela.setWindowTitle("Exemplo Interface!")

with open("style.css", "r") as file:
    app.setStyleSheet(file.read())

# 'txt' se refere a caixas de textos
# 'btn' se refere a botôes
# 'lbl' se refere a labels(rótulos)

lblNome = QLabel("Exemplo Tela", janela)
lblNome.move(130, 120)
lblNome.setStyleSheet("font-size: 25px; color: black;")

lblLogin = QLabel("Login", janela)
lblLogin.move(50, 193)
lblLogin.setStyleSheet("color: black; font-size: 15px")

lblSenha = QLabel("Senha", janela)
lblSenha.move(50, 273)
lblSenha.setStyleSheet("color: black; font-size: 15px;")

txtLogin = QLineEdit("", janela)
txtLogin.setGeometry(150, 190, 200, 25)

txtSenha = QLineEdit("", janela)
txtSenha.setGeometry(150, 270, 200, 25)


btnEntrar = QPushButton("Entrar", janela)
btnEntrar.setGeometry(50, 360, 300, 50)

#rgba(220, 220, 220, 0.445)
janela.show()
app.exec()