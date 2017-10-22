'''
https://www.tutorialspoint.com/python/python_gui_programming.htm

https://www.tutorialspoint.com/python/tk_button.htm
'''

from tkinter import *
from tkinter import ttk
raiz=Tk()
raiz.geometry('500x300')
raiz.configure(bg='black')
raiz.title('Ejemplo')
ttk.Button(raiz,text='Salir',command=quit).pack(side=BOTTOM)
raiz.mainloop()
