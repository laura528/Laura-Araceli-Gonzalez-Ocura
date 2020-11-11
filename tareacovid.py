from tkinter import *
from tkinter.ttk import *
import json5

def linearSearch(item,my_list):
    found= False
    position=0
    while position < len(my_list)and not found:
        if my_list[position]==item:
            found=True
        position= position + 1
    return found

bolsa=['COAHUILA','CHIHUAHUA','COLIMA','DURANGO','CDMX']

item=0
windows=Tk()
windows.title('MENU')

selected=IntVar()

b1=Radiobutton(windows,text='COAHUILA ',value=1,variable=selected)
b2=Radiobutton(windows,text='CHIHUAHUA',value=2,variable=selected)
b3=Radiobutton(windows,text='COLIMA   ',value=3,variable=selected)
b4=Radiobutton(windows,text='DURANGO  ',value=4,variable=selected)
b5=Radiobutton(windows,text='CDMX     ',value=5,variable=selected)

def clicked():
    if (selected.get())==1:
        item=('COAHUILA')
    if (selected.get())==2:
        item=('CHIHUAHUA')
    if (selected.get())==3:
        item=('COLIMA')
    if (selected.get())==4:
        item=('DURANGO')
    if (selected.get())==5:
        item=('CDMX')

  
    itemfound=linearSearch(item,bolsa)
    if itemfound:
       data={}

       data['COAHUILA']=[]
       data['COAHUILA'].append({
           'confirmados': 26389,
           'negativos': 35574,
           'sospechosos': 3504,
           'recuperados': 21371,
           'fallecidos': 1880,
           'activos': 1042 })
       
       data['CHIHUAHUA']=[]
       data['CHIHUAHUA'].append({
           'confirmados': 11123,
           'negativos': 10531,
           'sospechosos': 3619,
           'recuperados': 7443,
           'fallecidos': 1389,
           'activos': 330 })
        
       data['COLIMA']=[]
       data['COLIMA'].append({
           'confirmados':4870,
           'negativos': 3385,
           'sospechosos': 252,
           'recuperados':3224,
           'fallecidos':531,
           'activos': 307 })
       
       data['DURANGO']=[]
       data['DURANGO'].append({
           'confirmados':8947,
           'negativos': 15184,
           'sospechosos': 1592,
           'recuperados':6948,
           'fallecidos':632,
           'activos': 598 })

       data['CDMX']=[]
       data['CDMX'].append({
           'confirmados':126371,
           'negativos': 212710,
           'sospechosos': 20498,
           'recuperados':99500,
           'fallecidos':9667,
           'activos': 4569})

       for c in data[item]:
            print(item)
            print('confirmados',c['confirmados'])
            print('negativos',c['negativos'])
            print('sospechosos',c['sospechosos'])
            print('recuperados',c['recuperados'])
            print('fallecidos',c['fallecidos'])
            print('activos',c['activos'])
            print(' ')

            with open('covid data '+item,'w') as file:
                json5.dump(data[item],file)
            with open('covid data '+item) as file:
                data=json5.load(file)


btn=Button(windows,text='enter', command=clicked)

b1.grid(column=0, row=0)
b2.grid(column=0, row=1)
b3.grid(column=0, row=2)
b4.grid(column=0, row=3)
b5.grid(column=0, row=4)
btn.grid(column=0, row=5)

windows.mainloop()

