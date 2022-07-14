from tkinter import *

def seleccion():
    pantalla.config(text="{}".format(opcion.get()))

def reset():
    opcion.set(None)
    pantalla.config(text="")

ventana = Tk()
opcion = StringVar()
opcion.set(None)

Radiobutton(ventana, text="Independiente", variable=opcion, value='Independiente', command=seleccion).pack(anchor=W)
Radiobutton(ventana, text="Boca", variable=opcion, value='Boca', command=seleccion).pack(anchor=W)
Radiobutton(ventana, text="River", variable=opcion, value='River', command=seleccion).pack(anchor=W)
Radiobutton(ventana, text="Racing", variable=opcion, value='Racing', command=seleccion).pack(anchor=W)

pantalla = Label(ventana)
pantalla.pack()

Button(ventana, text="Reiniciar", command=reset).pack()

ventana.mainloop()