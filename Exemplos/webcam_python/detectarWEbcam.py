import cv2

camera = cv2.VideoCapture(0)
cascadeFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    
    sucesso, frame = camera.read()  
    videoTonsDeCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascadeFace.detectMultiScale(videoTonsDeCinza, scaleFactor=1.3, minNeighbors=3, minSize=(30,30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
    
    cv2.imshow("Imagem webcam", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()