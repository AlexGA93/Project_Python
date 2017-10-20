#Programa que manejara (en cada comunidad) la informacion de los alumnos(alumnos.py)
#Volcareos todos los datos en un txt con el nombre de la escuela
#nota: acceder a una carpeta determinada para crear archivo txt-->os.path.join('usr', 'bin', 'spam')-->usr\\bin\\spam
'''
Info que se pedira:
    Nombre del centro--->NOMBRE TXT= NOMBRE CENTRO
    direccion
    nombre director/a
    correo
Opciones a tratar:
   1.registrar centro
   2.dar de baja un centro
   3.mostrar listado de centros existentes
   4.salir
'''
import os
def Menu():
    print("*************MENU DE CENTROS EDUCATIVOS*****************")
    print("1.Registrar Centro")
    print("2.Dar de bajaCentro")
Menu()
