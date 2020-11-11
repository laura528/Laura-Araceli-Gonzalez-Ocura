import cv2
import numpy as np

img=cv2.imread('arbol.jpg')

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rojo_bajo= np.array([170,50,50])
rojo_alto= np.array([180,255,255])

celeste_bajo= np.array([90,50,50])
celeste_alto= np.array([100,255,255])

marron_bajo= np.array([10,100,100])
marron_alto= np.array([23,255,255])

mask1=cv2.inRange(hsv,rojo_bajo,rojo_alto)
mask2=cv2.inRange(hsv,celeste_bajo,celeste_alto)
mask3=cv2.inRange(hsv,marron_bajo,marron_alto)
mask= mask1+mask2+mask3

cv2.imshow('foto original',img)
cv2.imshow('foto extraida',mask)

cv2.waitKey(0)
cv2.destroyALLWindows()
