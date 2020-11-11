import cv2
from tkinter import *
   
while 1:
    
    def cerrar():
        print('gracias')
        ventana.destroy()
        exit()
        
    camara= cv2.VideoCapture(0)
    leido,frame=camara.read()
    if leido== True:
        cv2.imwrite('foto1.png',frame)
        print('se tomo con exito la foto')
            
    else:
        print('error camara no existe o esta apagada o no esta configurada')
        exit()

    camara.release()
        
        
    ventana=Tk()
    ventana.title('imagenes')
    ventana.geometry('645x550')
    selected=IntVar()

    foto=PhotoImage(file='foto1.png')
    fondo=Label(ventana,image=foto).place(x=0, y=0)

    boton1=Button(ventana,text=' foto ',command=ventana.destroy)
    boton1.place(x=260,y=500)

    boton2=Button(ventana,text='cerrar',command=cerrar)
    boton2.place(x=330,y=500)

    ventana.mainloop()

