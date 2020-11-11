import cv2
import numpy as np

img=cv2.imread('circulo.jpg')

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

morado_bajo= np.array([140,50,50])
morado_alto= np.array([160,255,255])

verde_bajo= np.array([40,50,50])
verde_alto= np.array([70,255,255])

rojo_bajo= np.array([160,50,50])
rojo_alto= np.array([180,255,255])

azul_bajo= np.array([90,50,50])
azul_alto= np.array([140,255,255])

amarillo_bajo= np.array([20,50,50])
amarillo_alto= np.array([40,255,255])

mask1=cv2.inRange(hsv,morado_bajo,morado_alto)
mask2=cv2.inRange(hsv,verde_bajo,verde_alto)
mask3=cv2.inRange(hsv,rojo_bajo,rojo_alto)
mask4=cv2.inRange(hsv,azul_bajo,azul_alto)
mask5=cv2.inRange(hsv,amarillo_bajo,amarillo_alto)

mask = mask1+mask2+mask3+mask4+mask5

cv2.imshow('foto original',img)
cv2.imshow('foto extraida',mask)
cv2.waitKey(0)
