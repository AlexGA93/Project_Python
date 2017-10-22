'''
https://www.tutorialspoint.com/python/python_gui_programming.htm

https://www.tutorialspoint.com/python/tk_button.htm
'''
import os
from tkinter import *
from tkinter import ttk

'''
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
'''

raiz=Tk()
raiz.geometry('500x300')
raiz.configure(bg='white')
raiz.title('Contraseña')
ttk.Button(raiz,text='Salir',command=quit).pack(side=BOTTOM)

label1=Label(raiz,text="Contraseña")
label1.pack(side=LEFT)

Entry1=Entry(raiz,bd=6)
Entry1.pack(side=RIGHT)

#ttk.Button(raiz,text='Salir',command=Comparacion()).pack(side=BOTTOM)

raiz.mainloop()

