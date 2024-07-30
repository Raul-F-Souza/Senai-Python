import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(300, 580)
janela.setWindowTitle("Calculadora")

with open("aula 12/exercicios/style.css", "r") as file:
    app.setStyleSheet(file.read())

def ExibirNoDisplay(x):
    valorDisplay = txtDisplay.text()
    concatenar = valorDisplay + x
    txtDisplay.setText(concatenar)
    
def calcular():
    resultado = eval(txtDisplay.text())
    txtDisplay.setText(str(resultado))
    
def limparVisor():
    txtDisplay.setText('')

# Visor principal
txtDisplay = QLineEdit("", janela)
txtDisplay.setGeometry(10, 10, 280, 95)

# Botão de apagar
btnApagar = QPushButton("⌫", janela)
btnApagar.setGeometry(230, 135, 50, 50)
btnApagar.setStyleSheet("background-color: black; font-size: 25px; font-weight: 250;")

# Fileira de numeros: 7, 8, 9
btnNum7 = QPushButton("7", janela)
btnNum7.setGeometry(10, 270, 70, 70)
btnNum7.clicked.connect(lambda: ExibirNoDisplay('9'))

btnNum8 = QPushButton("8", janela)
btnNum8.setGeometry(80, 270, 70, 70)
btnNum8.clicked.connect(lambda: ExibirNoDisplay('8'))

btnNum9 = QPushButton("9", janela)
btnNum9.setGeometry(150, 270, 70, 70)
btnNum9.clicked.connect(lambda: ExibirNoDisplay('9'))

# Fileira de numeros: 4, 5, 6
btnNum4 = QPushButton("4", janela)
btnNum4.setGeometry(10, 340, 70, 70)
btnNum4.clicked.connect(lambda: ExibirNoDisplay('4'))

btnNum5 = QPushButton("5", janela)
btnNum5.setGeometry(80, 340, 70, 70)
btnNum5.clicked.connect(lambda: ExibirNoDisplay('5'))

btnNum6 = QPushButton("6", janela)
btnNum6.setGeometry(150, 340, 70, 70)
btnNum6.clicked.connect(lambda: ExibirNoDisplay('6'))

# Fileira de numeros: 1, 2, 3
btnNum1 = QPushButton("1", janela)
btnNum1.setGeometry(10, 410, 70, 70)
btnNum1.clicked.connect(lambda: ExibirNoDisplay('1'))

btnNum2 = QPushButton("2", janela)
btnNum2.setGeometry(80, 410, 70, 70)
btnNum2.clicked.connect(lambda: ExibirNoDisplay('2'))

btnNum3 = QPushButton("3", janela)
btnNum3.setGeometry(150, 410, 70, 70)
btnNum3.clicked.connect(lambda: ExibirNoDisplay('3'))

# Fileira dos digitos: +/- , 0, .
btnOpositor = QPushButton("+/-", janela)
btnOpositor.setGeometry(10, 480, 70, 70)

btnNum0 = QPushButton("0", janela)
btnNum0.setGeometry(80, 480, 70, 70)
btnNum0.clicked.connect(lambda: ExibirNoDisplay('0'))

btnDot = QPushButton(".", janela)
btnDot.setGeometry(150, 480, 70, 70)

# Fileira de utilitarios: Cleaner, parenteses, %
btnC = QPushButton("C", janela)
btnC.setGeometry(10, 200, 70, 70)
btnC.setStyleSheet("color: red; background-color: #323232; font-weight: 800;")
btnC.clicked.connect(limparVisor)

btnParenteses = QPushButton("( )", janela)
btnParenteses.setGeometry(80, 200, 70, 70)
btnParenteses.setStyleSheet("color: #228b22; background-color: #323232; font-weight: 800;")

btnPorcentagem = QPushButton("%", janela)
btnPorcentagem.setGeometry(150, 200, 70, 70)
btnPorcentagem.setStyleSheet("color: #228b22; background-color: #323232; font-weight: 800;")
btnPorcentagem.clicked.connect(lambda: ExibirNoDisplay('%'))

# Fileira de numeros: ÷, X, -, +, =
btnDivisor = QPushButton("÷", janela)
btnDivisor.setGeometry(220, 200, 70, 70)
btnDivisor.setStyleSheet("color: #228b22; background-color: #323232; font-weight: 800; font-size: 25px;")
btnDivisor.clicked.connect(lambda: ExibirNoDisplay('/'))

btnMultiplicacao = QPushButton("X", janela)
btnMultiplicacao.setGeometry(220, 270, 70, 70)
btnMultiplicacao.setStyleSheet("color: #228b22; background-color: #323232; font-weight: 800;")
btnMultiplicacao.clicked.connect(lambda: ExibirNoDisplay('*'))

btnSubtracao = QPushButton("-", janela)
btnSubtracao.setGeometry(220, 340, 70, 70)
btnSubtracao.setStyleSheet("color: #228b22; background-color: #323232; font-weight: 800; font-size: 30px")
btnSubtracao.clicked.connect(lambda: ExibirNoDisplay('-'))

btnAdicao = QPushButton("+", janela)
btnAdicao.setGeometry(220, 410, 70, 70)
btnAdicao.setStyleSheet("color: #228b22; background-color: #323232; font-weight: 800; font-size: 25px")
btnAdicao.clicked.connect(lambda: ExibirNoDisplay('+'))

btnResultado = QPushButton("=", janela)
btnResultado.setGeometry(220, 480, 70, 70)
btnResultado.setStyleSheet("color: white; background-color: #228b22;")
btnResultado.clicked.connect(calcular)

janela.show()
app.exec()