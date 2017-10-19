#Abrir, crear, editar, enviar documento txt(llamado colegio) con info del alumno
#       nombre,apellidos,edaed,direccion,email,telefonos
#guardamos los txt en carpetas llamadas por la comunidad( donde se guardaran varios txt de colegios)---> HACER MENU AL INICIAR PARA ACCEDER A LAS CARPETAS
#interfaz grafica
#cifrdo por pass--> comparacion con txt---> si es erronea se enviara un codigo
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
import shutil
import platform
from os import listdir

def Menu():
    print("1.Crear carpeta de comunidad. ")
    print("2.Borrar carpeta de comunidad.")
    print("3.Consultar carpeta.")
    print("4.Salir")

def CrearCarpeta():
    nombre=input('Introduce el nombre: ').title()
    ruta=r'C:\prueba'
    carpeta=ruta+'\\'+nombre
    if platform.system()=="Windows":
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
    else:
        print("Error. Accion no compatible con sistema. Proximamente en actualizaciones.")
        pass



def BorrarCarpeta():

    nombre=input('Nombre de la carpeta a borrar: ').title()
    directorio=r'C:\prueba'
    carpeta=directorio+'\\'+nombre
    if platform.system()=="Windows":
        if (os.path.exists(carpeta)):
            shutil.rmtree(carpeta)
    else:
        print("Error. Accion no compatible con sistema. Proximamente en actualizaciones.")
        pass



def AbrirCarpeta():
    nombre = input('Nombre de la carpeta a borrar: ').title()
    directorio = r'C:\prueba'
    carpeta = directorio + '\\' + nombre
    if platform.system()=="Windows":
        os.startfile(carpeta)
    else:
        print("Error. Accion no compatible con sistema. Proximamente en actualizaciones.")
        pass

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


def opcion():
    opcion=eval(input('Introduce la opcion: '))
    if opcion<1 or opcion>4:
        print("Error: revisa rango numerico de respuestas.")
    else:
        seleccion(opcion)


print("Acceso a Manejo de Ficheros del Centro Educacional. Seleccione una de las opciones: ")
Menu()
opcion()