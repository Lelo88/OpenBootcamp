from tkinter import *

ventana = Tk()
objeto = StringVar()
lista = Listbox(ventana)

for elemento in ['Independiente', 'Racing', 'Boca', 'River Plate', 'San Lorenzo']:
    lista.insert(END, elemento)

lista.pack()

etiqueta = Label(text="Listado de clubes de futbol")
etiqueta.pack(ipady=100, ipadx=100)

ventana.mainloop()