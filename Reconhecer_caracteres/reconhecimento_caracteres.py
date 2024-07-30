import cv2
import pytesseract

def reconhcerPlacas (imagem):
    # Chamando o executavel de reconhecimento de caracteres (bibilioteca)
    pytesseract.pytesseract.tesseract_cmd=r"C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    # Registrando imagem da placa em uma variavel
    placa = cv2.imread(imagem, 0)

    # Converter/capturar textos da imagem
    textos = pytesseract.image_to_string(placa, config='l eng --oem 3 --psm 12')
    
    return textos

# Exibir uma imagem para a função e mostrar texto reconhecidos
print(reconhcerPlacas('placa01.png'))
print(reconhcerPlacas('placa02.jpg'))
print(reconhcerPlacas('placa03.png'))
print(reconhcerPlacas('placa04.png'))
print(reconhcerPlacas('placa05.jpg'))