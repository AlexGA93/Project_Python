'''
algoritmo de cifrado en comparacion con una cadena de un txt llamado password.txt
1.abrimos el documento en memoria
2. pedimos al usuario que meta la password
3. comparamos:
    si es correcto-->invocamos al .py
    si no es correcto--> volvemos al princpio mostrando mensaje de error
'''
import os


def Comparacion():
    password = open('password.txt','r').read().split('\n')
    orden = input('Introduzca la contraseña: ').title()

    if password[0] != orden:
        print('ERROR: pass erronea.')
    else:
        print('CORRECTO')
        import menu_global
        from menu_global import menu
        print('prueba')
        menu_global.menu()

if __name__=="__main__":
    Comparacion()