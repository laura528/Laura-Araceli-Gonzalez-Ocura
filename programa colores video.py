#Algoritmo de deteccion de colores
#jesus homero carmona mendoza
#
#
#Detecta objetos verdes, elimina el ruido y busca su centro
 
import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)
 
while(1):
     
    #Capturamos una imagen y la convertimos de RGB -> HSV
    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
    #Establecemos el rango de colores que vamos a detectar
    #En este caso de verde oscuro a verde-azulado claro
    rojo_bajo = np.array([165,50,50], dtype=np.uint8)
    rojo_alto = np.array([180,255,255], dtype=np.uint8)
    amarillo_bajo = np.array([20,50,50], dtype=np.uint8)
    amarillo_alto = np.array([40,255,255], dtype=np.uint8)
    azul_bajo = np.array([95,50,50], dtype=np.uint8)
    azul_alto = np.array([135,255,255], dtype=np.uint8)
    
    #Crear una mascara con solo los pixeles dentro del rango de verdes
    mask1 = cv2.inRange(hsv, rojo_bajo, rojo_alto)
    mask2 = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)
    mask3 = cv2.inRange(hsv, azul_bajo, azul_alto)
    mask= mask1+mask2+mask3
    
    #Encontrar el area de los objetos que detecta la camara
    moments = cv2.moments(mask)
    area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
    if(area > 2000000):
         
        #Buscamos el centro x, y del objeto
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
        print ("x = ", x)
        print ("y = ", y)
 
        #Dibujamos una marca en el centro del objeto
        cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
    cv2.imshow('mask', mask)
    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()
