'''
https://www.tutorialspoint.com/python/python_gui_programming.htm

https://www.tutorialspoint.com/python/tk_button.htm
'''
import os
from tkinter import *
from tkinter import ttk



def Comparacion():
    password = open('password_prueba.txt','r').read().split('\n')
    Label1=Label(raiz,SystemExit="Contraseña: ")
    orden = input('Introduzca la contraseña: ').title()

    if password[0] != orden:
        print('ERROR: pass erronea.')
    else:
        print('CORRECTO')
        import menu_global
        from menu_global import menu
        print('prueba')
        menu_global.menu()


raiz=Tk()
raiz.geometry('500x300')
raiz.iconbitmap('ico_python.ico')
raiz.title('Control de Acceso')

color='#ffffff'
raiz.configure(bg=color)

logo=PhotoImage(file="D:\GOOGLE DRIVE\Programacion\PYTHON\Project_Python\pruebas\source.gif")
label1=Label(raiz,image=logo)
label1.pack(fill=X)

ttk.Button(raiz,text='Salir',command=quit).place(x=370,y=270)#.place(bordermode=OUTSIDE, height=25, width=50,)#.pack(side=RIGHT)
ttk.Button(raiz,text='Aceptar',command=Comparacion()).place(x=70,y=270)#.pack(side=LEFT)#se puede llamnar a una funcion

label2=Label(raiz,text="Contraseña")
label2.pack(anchor=CENTER)


Entry1=Entry(raiz,bd=6)
Entry1.pack(anchor=CENTER)


raiz.mainloop()

