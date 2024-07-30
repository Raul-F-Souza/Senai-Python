import sys, cv2
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

# Trazendo dados cadastrados em um projeto anterior para uso no projeto atual
import dados
dadosPessoais = dados.informacoes()

import reconhecimentoCaracterees
# Função para reconher caracteres
def buscar():
    placaReconhecida = reconhecimentoCaracterees.reconhcerTextos('Img/placa02.jpg')
    
    # Verificando se no meio dos textos reconhecida tem a placa cadastrada
    for p in dadosPessoais:
        if p in placaReconhecida:
            print(dadosPessoais[p][0])
    
    #print(placaReconhecida)

# função básica para mostrar webcam
def MostrarWebcam():
    camera = cv2.VideoCapture(0)
    
    while True:
        sucesso, frame = camera.read()
        cv2.imshow("Webcam", frame)
        
        # Verificar se na imagem capturada está a nossa placa
        cv2.imwrite('Img/textoPlaca.jpg', frame) # Convertendo o frame em imagem
        
        placaReconhecida = reconhecimentoCaracterees.reconhcerTextos('Img/textoPlaca.jpg')
        #print(placaReconhecida)
        for p in dadosPessoais:
            if p in placaReconhecida:
                
                print(dadosPessoais[p][0])
                
                # Adicionando os dados cadastrados pelo numero da placa
                txtNome.setText(dadosPessoais[p][0])
                txtModelo.setText(dadosPessoais[p][1])
                txtAnoVeiculo.setText(dadosPessoais[p][2])
                txtPlaca.setText(placaReconhecida)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            camera.release()
            cv2.destroyAllWindows()
            break
    

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(500, 700)
janela.setWindowTitle('Monitoramento Veicular')

# Importação do arquivo CSS para estiização
with open("style.css", "r") as file:
    app.setStyleSheet(file.read())


# Titulo abreviado de 'monitoramento veicular
titulo = QLabel("Monitoramento veicular", janela)
titulo.move(110, 50)
titulo.setStyleSheet("font-size: 25px")

# Nome do usuário
lblNome = QLabel("Nome", janela)
lblNome.move(50, 160)
txtNome = QLineEdit("", janela)
txtNome.setGeometry(250, 150, 200, 40)

# Placa do veículo
lblModelo = QLabel("Modelo", janela)
lblModelo.move(50, 260)
txtModelo = QLineEdit("", janela)
txtModelo.setGeometry(250, 250, 200, 40)

# Placa do veículo
lblPlaca = QLabel("Placa", janela)
lblPlaca.move(50, 360)
txtPlaca = QLineEdit("", janela)
txtPlaca.setGeometry(250, 350, 200, 40)

# Ano do veículo
lblAno = QLabel("Ano Veículo", janela)
lblAno.move(50, 460)
txtAnoVeiculo = QLineEdit("", janela)
txtAnoVeiculo.setGeometry(250, 450, 200, 40)

# Botao para câmera
btnCamera = QPushButton("Abrir câmera", janela)
btnCamera.setGeometry(120, 570, 250, 70) 
btnCamera.clicked.connect(MostrarWebcam) # Ativando a função do botâo ao ser clicado

janela.show()
app.exec()