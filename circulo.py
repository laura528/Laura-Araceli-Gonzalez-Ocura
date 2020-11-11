import cv2
import numpy as np

img=cv2.imread('circulo.jpg')

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

morado_bajo= np.array([140,100,100])
morado_alto= np.array([160,255,255])

verde_bajo= np.array([40,100,100])
verde_alto= np.array([70,255,255])

naranja_bajo= np.array([10,100,100])
naranja_alto= np.array([25,255,255])

mask1=cv2.inRange(hsv,morado_bajo,morado_alto)
mask2=cv2.inRange(hsv,verde_bajo,verde_alto)
mask3=cv2.inRange(hsv,naranja_bajo,naranja_alto)

mask = mask1+mask2+mask3

cv2.imshow('foto original',img)
cv2.imshow('foto extraida',mask)
cv2.waitKey(0)

