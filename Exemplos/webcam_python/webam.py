import cv2

# Criando uma variável para capturar imagens (Frames)
# camera = cv2.VideoCapture("video.mp4")

# Criando uma variável para armazenar a webcam, localizada no dispositivo 0
camera = cv2.VideoCapture(0)

# loop para percorrer frame frame, imagem por imagem
while True:
    sucesso, frame = camera.read()
    cv2.imshow("imagem video", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break
 
# Limpando a variável que contem a imagem
camera.release()
cv2.destroyAllWindows()