from tkinter import *
from tkinter.ttk import *
import mysql.connector

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="covid"
)
mycursor= mydb.cursor()

windows=Tk()
windows.title('MENU PRINCIPAL')
windows.geometry('300x400')
            
def coahuila():

    mycursor.execute("SELECT * FROM datos where control='1'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    windows.destroy()
    windows.__init__()
    windows.geometry('525x250')
    windows.title('COAHUILA')
    windows.geometry('525x250')
        
    eti=Label(windows, text='Control          Confirmados        Recuperados         Fallecidos')
    eti.place(x=100,y=50)
    et=Label(windows, text=a)
    et.place(x=115, y=70)
    et=Label(windows, text=b)
    et.place(x=190, y=70)
    et=Label(windows, text=c)
    et.place(x=285, y=70)
    et=Label(windows, text=d)
    et.place(x=375, y=70)
    
    boton=Button(windows,text='Salir',command=salir)
    boton.place(x=210,y=140)

def chihuahua():
    mycursor.execute("SELECT * FROM datos where control='2'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    windows.destroy()
    windows.__init__()
    windows.geometry('525x250')
    windows.title('CHIHUAHUA')
    windows.geometry('525x250')
        
    eti=Label(windows, text='Control          Confirmados        Recuperados         Fallecidos')
    eti.place(x=100,y=50)
    et=Label(windows, text=a)
    et.place(x=115, y=70)
    et=Label(windows, text=b)
    et.place(x=190, y=70)
    et=Label(windows, text=c)
    et.place(x=285, y=70)
    et=Label(windows, text=d)
    et.place(x=375, y=70)
    
    boton=Button(windows,text='Salir',command=salir)
    boton.place(x=210,y=140)

def colima():
    mycursor.execute("SELECT * FROM datos where control='3'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    windows.destroy()
    windows.__init__()
    windows.geometry('525x250')
    windows.title('COLIMA')
    windows.geometry('525x250')
        
    eti=Label(windows, text='Control          Confirmados        Recuperados         Fallecidos')
    eti.place(x=100,y=50)
    et=Label(windows, text=a)
    et.place(x=115, y=70)
    et=Label(windows, text=b)
    et.place(x=190, y=70)
    et=Label(windows, text=c)
    et.place(x=285, y=70)
    et=Label(windows, text=d)
    et.place(x=375, y=70)
    
    boton=Button(windows,text='Salir',command=salir)
    boton.place(x=210,y=140)


def durango():
    mycursor.execute("SELECT * FROM datos where control='4'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    windows.destroy()
    windows.__init__()
    windows.geometry('525x250')
    windows.title('DURANGO')
    windows.geometry('525x250')
        
    eti=Label(windows, text='Control          Confirmados        Recuperados         Fallecidos')
    eti.place(x=100,y=50)
    et=Label(windows, text=a)
    et.place(x=115, y=70)
    et=Label(windows, text=b)
    et.place(x=190, y=70)
    et=Label(windows, text=c)
    et.place(x=285, y=70)
    et=Label(windows, text=d)
    et.place(x=375, y=70)
    
    boton=Button(windows,text='Salir',command=salir)
    boton.place(x=210,y=140)
 

def cdmx():
    mycursor.execute("SELECT * FROM datos where control='5'")
    myresult= mycursor.fetchall()

    a=myresult[0][0]
    b=myresult[0][1]
    c=myresult[0][2]
    d=myresult[0][3]

    print("")
    windows.destroy()
    windows.__init__()
    windows.geometry('525x250')
    windows.title('CDMX')
    windows.geometry('525x250')
        
    eti=Label(windows, text='Control          Confirmados        Recuperados         Fallecidos')
    eti.place(x=100,y=50)
    et=Label(windows, text=a)
    et.place(x=115, y=70)
    et=Label(windows, text=b)
    et.place(x=190, y=70)
    et=Label(windows, text=c)
    et.place(x=285, y=70)
    et=Label(windows, text=d)
    et.place(x=375, y=70)

    boton=Button(windows,text='Salir',command=salir)
    boton.place(x=210,y=140)


def salir():
    windows.destroy()

def agg():
     windows.destroy()
     windows.__init__()
     def guardar():
          mycursor.execute("SELECT MAX(Control) AS maximum FROM estados")
          result = mycursor.fetchall()
          for i in result:
               x=i[0]
          x=x+1
          sql=("""INSERT INTO estados (control, estado) VALUES (%s,%s)""")
          val= (x,estado.get())
          sqll = ("""INSERT INTO datos (control, confirmados, recuperados, fallecidos) VALUES (%s,%s,%s,%s) """)
          vall = (x,confirmados.get(),recuperados.get(),fallecidos.get())
          mycursor.execute(sql, val)
          mycursor.execute(sqll, vall)
          mydb.commit()
          windows.destroy()
          windows.__init__()
          windows.title('Agregar')
          windows.geometry('525x250')
          eti=Label(windows, text='Se guardo correctamente')
          eti.place(x=220,y=20)
          boton=Button(windows,text='Salir',command=salir)
          boton.place(x=250,y=180)
          
     windows.title('Agregar')
     windows.geometry('525x250')

     etiqueta=Label(windows,text='Estado:')
     etiqueta.place(x=20,y=20)
     etiqueta=Label(windows,text='Confirmados:')
     etiqueta.place(x=20,y=50)
     etiqueta=Label(windows,text='Recuperados:')
     etiqueta.place(x=20,y=80)
     etiqueta=Label(windows,text='Fallecidos:')
     etiqueta.place(x=20,y=110)

     estado=StringVar()
     cajatexto=Entry(windows,textvariable=estado)
     cajatexto.place(x=110,y=20)
     confirmados=IntVar()
     cajatexto=Entry(windows,textvariable=confirmados)
     cajatexto.place(x=110,y=50)
     recuperados=IntVar()
     cajatexto=Entry(windows,textvariable=recuperados)
     cajatexto.place(x=110,y=80)
     fallecidos=IntVar()
     cajatexto=Entry(windows,textvariable=fallecidos)
     cajatexto.place(x=110,y=110)
     
     boton=Button(windows,text='Guardar',command=guardar)
     boton.place(x=50,y=180)



    
b1=Button(windows,text="Coahuila",command=coahuila).place(x=100,y=50)
b2=Button(windows,text="Chihuahua",command=chihuahua).place(x=100,y=100)
b3=Button(windows,text="Colima",command=colima).place(x=100,y=150)
b4=Button(windows,text="Durango",command=durango).place(x=100,y=200)
b5=Button(windows,text="CDMX",command=cdmx).place(x=100,y=250)
b6=Button(windows,text="Agregar estado",command=agg).place(x=100,y=300)

windows.mainloop()
