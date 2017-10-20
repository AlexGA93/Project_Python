'''
algoritmo llamado desde el programa de cifrado de seguridad
'''
import os

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
menu()