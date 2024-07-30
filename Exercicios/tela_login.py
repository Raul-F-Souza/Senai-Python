import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(450, 809)
janela.setWindowTitle("Login Netflix")

with open("style.css", "r") as file:
    app.setStyleSheet(file.read())

lblLogar = QLabel("Sign in", janela)
lblLogar.move(68,50)
lblLogar.setStyleSheet("color: white; font-size: 20px; text-align: left;")

txtUser = QLineEdit("", janela)
txtUser.setGeometry(68, 100, 314, 56)
txtUser.setPlaceholderText("Email or mobile number")

txtPassword = QLineEdit("", janela)
txtPassword.setGeometry(68, 175, 314, 56)
txtPassword.setPlaceholderText("Password")

tbnLogar = QPushButton("Sign in", janela)
tbnLogar.setGeometry(68, 250, 314, 40)
tbnLogar.setStyleSheet("background-color: #e30020; color: white; font-size: 16px")

lblOr = QLabel("OR", janela)
lblOr.move(220, 310)
lblOr.setStyleSheet("color: #a8b4a9")

tbnUseCode = QPushButton("Use a Sign-in Code", janela)
tbnUseCode.setGeometry(68, 350, 314, 40)
tbnUseCode.setStyleSheet("background-color: #383737; color: white; font-size: 16px")

tbnForgetPassword = QPushButton("Forget your passwprd?", janela)
tbnForgetPassword.setGeometry(68, 400, 314, 40)
tbnForgetPassword.setStyleSheet(" color: white; font-size: 16px")

janela.show()
app.exec()