from tkinter import *
from tkinter import ttk
ventana=Tk()
cuadro_uno = Listbox(ventana, bg='yellow')
cuadro_uno.insert(0,'yellow')
cuadro_uno.insert(0,'negro')
cuadro_uno.insert(0,'green')
cuadro_uno.pack()
ventana.mainloop()