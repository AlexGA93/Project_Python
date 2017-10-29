#Abrir, crear, editar, enviar documento txt(llamado colegio) con info del alumno
#       nombre,apellidos,edaed,direccion,email,telefonos
#guardamos los txt en carpetas llamadas por la comunidad( donde se guardaran varios txt de colegios)---> HACER MENU AL INICIAR PARA ACCEDER A LAS CARPETAS
#interfaz grafica
#cifrdo por pass--> comparacion con txt---> si es erronea se enviara un codigo
#from ARCHIVO import FUNCION
#archivo.funcion(args)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import shutil
import platform
from os import listdir

def CrearCarpeta():
    nombre=input('Introduce el nombre: ').title()
    ruta=r'C:\prueba'
    carpeta=ruta+'\\'+nombre
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
def BorrarCarpeta():

    nombre=input('Nombre de la carpeta a borrar: ').title()
    directorio=r'C:\prueba'
    carpeta=directorio+'\\'+nombre
    shutil.rmtree(carpeta)
def AbrirCarpeta():
    nombre = input('Nombre de la carpeta a borrar: ').title()
    directorio = r'C:\prueba'
    carpeta = directorio + '\\' + nombre
    os.startfile(carpeta)
def seleccion(opcion):
    if opcion==1:
        #creamos directorio en una carpeta escritorio
        CrearCarpeta()
    elif opcion==2:
        #Borramos carpeta en directorio
        BorrarCarpeta()
    elif opcion==3:
        #abrimos la carpeta
        AbrirCarpeta()
    elif opcion==4:
        print("Saliendo del programa")
        pass
def eleccion():
    opcion=eleccion.get()
    if opcion<1 or opcion>4:
        mensaje_saliente = messagebox.showinfo("Error Enocntrado", "Procure introducir una variable correcta.")
    else:
        seleccion(opcion)
raiz = Tk()
raiz.geometry('500x500')  # dimensiones de ventana
raiz.iconbitmap('ico_python.ico')  # llamamos a la foto de portada
raiz.title('Menu de Tratamiento de Ficheros')  # titulo

logo=PhotoImage(file="D:\GOOGLE DRIVE\Programacion\PYTHON\Project_Python\source.gif")
label1=Label(raiz,image=logo).pack(fill=X)

etiqueta_intro = Label(raiz, text="Acceso al Programa de Tratamiento de Ficheros del S.E.").place(x=100, y=170)
etiqueta_intro2 = Label(raiz, text="Escoja una de las opciones disponibles: ").place(x=135, y=190)
etiqueta_intro = Label(raiz, text="------------------------------------------------------------------").place(x=80,y=210)
etiqueta_opcion1 = Label(raiz, text="1.Crear carpeta de comunidad. ").place(x=100, y=240)
etiqueta_opcion2 = Label(raiz, text="2.Borrar carpeta de comunidad.").place(x=100, y=270)
etiqueta_opcion3 = Label(raiz, text="3.Consultar carpeta.").place(x=100, y=300)
etiqueta_opcion4 = Label(raiz, text="4.Salir.").place(x=100, y=330)

opcion=StringVar()
etiqueta_eleccion = Label(raiz, text="Eleccion: ").place(x=100, y=360)
caja_eleccion = Entry(raiz, textvariable=opcion).place(x=150, y=360)

ttk.Button(raiz,text='Aceptar',command=eleccion).place(x=50,y=450)
ttk.Button(raiz,text='Salir',command=quit).place(x=370,y=450)
#opcion()
raiz.mainloop()

