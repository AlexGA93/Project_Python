'''
Programa que se encargue de descifrar una cadena de texto leida de un .txt
abrimos en memoria el archivo
leemos el contenido
transformamos lo leido en un vector
comparamos los elementos de dicho vector con otro con los que se cambiaran...
reasignar nuevos variables a un vector nuevo
convertir dicho vector en cadena
comparar cadena con palabra introducida por el usuario


Dohmdqgur  <---->   Alejandro
'''
def Comparacion(archivo,lista):
    contador_a=0
    contador_b=0
    lista_final=[]
    for a in archivo:
        for l in lista:
            lista_final.append(l[])
            contador_a+=1
    print(lista_final)
archivo=open('hola.txt','r').read().split()
'''
Hemos creado un vector con las letras del bloc de notas formando un vector dispuesto a ser comparado
'''
lista=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

contador=0
while contador<=8:
    if archivo[contador].isdigit() == False:
        #comparemos
        Comparacion(archivo,lista)
        print('todo bien')
        contador += 1
    else:
        print('Alguien o algo ha modificado el contenido del txt')


