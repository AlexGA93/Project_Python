'''
algoritmo llamado desde el programa de cifrado de seguridad
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def control():
    opcion=eleccion.get()

    if opcion=="1":
        import ficheros
        if __name__ == '__main__':
            ficheros

    elif opcion=="2":
        #invocar a centros.py
        print("holis")

    elif opcion=="3":
        mensaje_saliente = messagebox.showinfo("Salir", "Saliendo del sistema. Gracias!")
        sys.exit(0)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

raiz=Tk()
raiz.geometry('500x500')#dimensiones de ventana
raiz.iconbitmap('ico_python.ico')#llamamos a la foto de portada
raiz.title('Menu del Servicio Educacional')#titulo
logo=PhotoImage(file="D:\GOOGLE DRIVE\Programacion\PYTHON\Project_Python\source.gif")
label1=Label(raiz,image=logo).pack(fill=X)

etiqueta_intro = Label(raiz, text="Bienvenido al Asistente de la Base de Datos Educacional.").place(x=100, y=170)
etiqueta_intro2 = Label(raiz, text="Escoja una de las opciones disponibles: ").place(x=135, y=190)
etiqueta_intro = Label(raiz, text="------------------------------------------------------------------").place(x=80, y=210)
etiqueta_opcion1 = Label(raiz, text="1.Seccion Ficheros por Comunidad Autonoma.").place(x=100, y=240)
etiqueta_opcion2= Label(raiz, text="2. Seccion Centros educacionales. ").place(x=100, y=270)
etiqueta_opcion3 = Label(raiz, text="3. Salir.").place(x=100, y=300)


eleccion=StringVar()
etiqueta_eleccion = Label(raiz, text="Eleccion: ").place(x=100, y=360)
caja_eleccion = Entry(raiz, textvariable=eleccion).place(x=150, y=360)
ttk.Button(raiz, text='Aceptar', command=control).place(x=90, y=470)

#ttk.Button(raiz, text='Aceptar', command=control(opcion)).place(x=90, y=470)
ttk.Button(raiz,text='Salir',command=quit).place(x=370,y=470)
raiz.mainloop()