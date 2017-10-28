'''
https://www.tutorialspoint.com/python/python_gui_programming.htm

https://www.tutorialspoint.com/python/tk_button.htm
'''
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def Comparacion():

    contraseña_documento = open('password_prueba.txt','r').read().split('\n')
    cadena_contraseña_documento=''.join(contraseña_documento)


    #print(password.get().title())
    #print(cadena_contraseña_documento)

    if cadena_contraseña_documento!= password.get().title():
        mensaje_saliente = messagebox.showinfo("Acceso Denegado", "ERROR: pass erronea.")
    else:
        print('CORRECTO')
        mensaje_saliente=messagebox.showinfo("Acceso Concedido","Contraseña correcta.Acceso concedido")
        import menu_global
        menu_global.menu()


# Montamos la ventana estetica
raiz=Tk()
password=StringVar()
raiz.geometry('500x300')#dimensiones de ventana
raiz.iconbitmap('ico_python.ico')#llamamos a la foto de portada
raiz.title('Control de Acceso')#titulo
#color='#ffffff'
#raiz.configure(bg=color)#definimos color de fondo de la ventana
logo=PhotoImage(file="D:\GOOGLE DRIVE\Programacion\PYTHON\Project_Python\source.gif")
label1=Label(raiz,image=logo)
label1.pack(fill=X)#cargo la foto de portada


etiqueta1=Label(raiz,text="Contraseña: ").place(x=170,y=170)
caja=Entry(raiz,textvariable=password).place(x=170,y=200)

ttk.Button(raiz,text='Aceptar',command=Comparacion).place(x=50,y=270)
ttk.Button(raiz,text='Salir',command=quit).place(x=370,y=270)

raiz.mainloop()

