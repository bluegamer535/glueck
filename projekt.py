import random
from tkinter import *
import time

versuch = 10

def buttonneuClick():
    z1 = random.randint(1, 9)
    print(z1)
    z2 = random.randint(1, 9)
    print(z2)
    z3 = random.randint(1, 9)
    print(z3)
    label1 = Label(master=tkFenster, text=z1, fg='white', bg='gray', font=('Arial', 16))
    label1.place(x=210, y= 500, width=200, height=100)


    label2 = Label(master=tkFenster, text=z2, fg='white', bg='gray', font=('Arial', 16))
    label2.place(x=535, y= 500, width=200, height=100)


    label3 = Label(master=tkFenster, text=z3, fg='white', bg='gray', font=('Arial', 16))
    label3.place(x=860, y= 500, width=200, height=100)
    
    label4 = Label(master=tkFenster, text=z4, fg='white', bg='gray', font=('Arial', 16))
    label4.place(x=1185, y= 500, width=200, height=100)

    label5 = Label(master=tkFenster, text=z5, fg='white', bg='gray', font=('Arial', 16))
    label5.place(x=1510, y= 500, width=200, height=100)

    labeleinsatz = Label(master=tkFenster, text='hallo', fg='white', bg='gray', font=('Arial', 16))
    labeleinsatz.place(x=700, y= 500, width=200, height=100)

    versuch = int(labelzaehler.cget('text')) 
    versuch = versuch - 1
    labelzaehler.config(text=int(versuch))
    if z1 == z2:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    if z1 == z3:
        versuch = int(labelzaehler.cget('text'))
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    if z2 == z3:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
    
    if z3 == z4:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    
    if z1 == z4:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    
    if z2 == z4:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
        
    if z4 == z5:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
     
    if z1 == z5:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    
    if z2 == z5:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    
    if z3 == z5:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 1.2
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    if z1 == z2 == z3:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 10
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))
        
    if z1 == z2 == z3 == z4:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 20
        round(versuch, 0)
        labelzaehler.config(text=int(versuch))   
        
       
    if z1 == z2 == z3 == z4 == z5:
        versuch = int(labelzaehler.cget('text')) 
        versuch = versuch * 20
        round(versuch, 0)
        labelzaehler.config(text=int(versuch)) 
        


  
# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title('Test')
tkFenster.geometry('1920x1080')

z1 = random.randint(1, 9)
print(z1)

z2 = random.randint(1, 9)
print(z2)

z3 = random.randint(1, 9)
print(z3)

z4 = random.randint(1, 9)
print(z4)

z5 = random.randint(1, 9)


label1 = Label(master=tkFenster, text=z1, fg='white', bg='gray', font=('Arial', 16))
label1.place(x=210, y= 500, width=200, height=100)


label2 = Label(master=tkFenster, text=z2, fg='white', bg='gray', font=('Arial', 16))
label2.place(x=535, y= 500, width=200, height=100)


label3 = Label(master=tkFenster, text=z3, fg='white', bg='gray', font=('Arial', 16))
label3.place(x=860, y= 500, width=200, height=100)

label4 = Label(master=tkFenster, text=z4, fg='white', bg='gray', font=('Arial', 16))
label4.place(x=1185, y= 500, width=200, height=100)

label5 = Label(master=tkFenster, text=z4, fg='white', bg='gray', font=('Arial', 16))
label5.place(x=1510, y= 500, width=200, height=100)

labelzaehler = Label(master=tkFenster, text=versuch, fg='red', bg='blue', font=('Arial', 16))
labelzaehler.place(x=910, y= 650, width=100, height=50)

labeleinsatz = Label(master=tkFenster, text='hallo', fg='white', bg='gray', font=('Arial', 16))
labeleinsatz.place(x=500, y= 650, width=200, height=100)


buttonneu = Button(master=tkFenster, text='Neu', bg='red', command=buttonneuClick)
buttonneu.place(x=910, y=750, width=100, height=50)


buttonmehr = Button(master=tkFenster, text='mehr', bg='red', command=buttonneuClick)
buttonmehr.place(x=500, y=750, width=100, height=50)


buttonweniger = Button(master=tkFenster, text='weniger', bg='red', command=buttonneuClick)
buttonweniger.place(x=300, y=750, width=100, height=50)



logo1 = PhotoImage(file='H:/zzDaten/Informatik/Bilder/logo_BookOfRaClassic-1.png')

labellogo = Label(image=logo1)
labellogo.place(x=660, y=50, width=600, height=350)

tkFenster.mainloop()