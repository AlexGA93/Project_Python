'''
algoritmo llamado desde el programa de cifrado de seguridad
'''
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def control(opcion):
    if opcion==1:
        #llamamos a cuerpo.py

        print("")
        import CUERPO
        CUERPO.main()
    elif opcion==2:
        #llamamos a ficheros.py

        print("")
        # from ficheros import main
        #ficheros.main()
    elif opcion==3:
        print("Saliendo... ")
        pass
def menu():
    print('Bienvenido al Asistente de la Base de Datos Educacional.')
    print('Escoja una de las opciones disponibles:')
    print('1.Seccion Ficheros por Comunidad Autonoma.')
    print('2. Seccion Centros educacionales. ')
    print('3. Salir.')
    opcion=eval(input('Opcion: '))
    control(opcion)

raiz=Tk()
password=StringVar()
raiz.geometry('1000x1000')#dimensiones de ventana
raiz.iconbitmap('ico_python.ico')#llamamos a la foto de portada
raiz.title('Menu del Servicio Educacional')#titulo


logo=PhotoImage(file="D:\GOOGLE DRIVE\Programacion\PYTHON\Project_Python\source.gif")
label1=Label(raiz,image=logo)
label1.pack(fill=X)#cargo la foto de portada


#etiqueta1=Label(raiz,text="Contraseña: ").place(x=170,y=170)
#caja=Entry(raiz,textvariable=password).place(x=170,y=200)

#ttk.Button(raiz,text='Aceptar',command=Comparacion).place(x=50,y=270)

ttk.Button(raiz,text='Salir',command=quit).place(x=370,y=270)
#Comparacion(raiz)
raiz.mainloop()