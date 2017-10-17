#Abrir, crear, editar, enviar documento txt(llamado colegio) con info del alumno
#       nombre,apellidos,edaed,direccion,email,telefonos
#guardamos los txt en carpetas llamadas por la comunidad( donde se guardaran varios txt de colegios)---> HACER MENU AL INICIAR PARA ACCEDER A LAS CARPETAS
#interfaz grafica
#cifrdo por pass--> comparacion con txt---> si es erronea se enviara un codigo
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
from os import listdir

def Menu():
    print("1.Crear carpeta de comunidad. ")
    print("2.Borrar carpeta de comunidad.")
    print("3.Consultar carpeta.")
    print("4.Acceder a una carpeta(se mostrara una lista de los archivos).")
    print("5.Salir")

def CrearCarpeta():
    directorio=os.getcwd()
    if(os.path.isdir(directorio)):
        nombre=input('Introduce nombre de carpeta: ')
        os.mkdir(nombre)
        print("carpeta ",nombre," creada correctamente en",directorio)


def BorrarCarpeta():
    directorio=os.getcwd()
    if(os.path.isdir(directorio)):
        nombre=input('Introduce nombre de carpeta: ')
        os.rmdir(nombre)
        print("Carpeta ",nombre," borrada")


def AbrirCarpeta():
    for nombre in listdir("."):
        print(nombre)


def Acceso():
    ruta=input('Introduce la ruta de la carpeta: ')

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
        #Accedemos a una carpeta
        Acceso()
    elif opcion==5:
        pass


def opcion():
    opcion=int(input('Introduce la opcion: '))
    while opcion>=1 and opcion<=5:
        if(opcion.isdigit()==True):
            seleccion(opcion)
        else:
            print("ERROR: Introduzca una opcion numerica.")
            pass
print("Bienvenido a la base de datos educacional. Seleccione una de las opciones: ")
Menu()
opcion()