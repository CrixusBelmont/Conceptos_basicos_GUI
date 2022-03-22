import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')
#fr es foreground (primer plano) color de la fuente de letra
#relief cambia el contorno del boton, es decir, los alrededores, las esquinas.
#bg es background, cambia el fondo del boton

# Definimos los botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, ipadx=20, ipady=50)
#El padx es el padding, o sea el espacio, la x al final es la configuracion de izq a der
#Por lo tanto de arriba a abajo seria pady
# ipad es inner padding, por lo que se usa para el espacio interno

# N(arriba), E(derecha), S(abajo), W(izquierda)
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1,column=0, sticky='NSWE')

# Boton3
boton3 = ttk.Button(ventana, text='Botón 3')
boton3.grid(row=0, column=1, sticky='NSWE')

# Boton4
boton4= tk.Button(ventana,text='Botón 4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()

#Las configuraciones del boton 4 en su evento es posible porque usa el paquete de tk
#Por ejemplo: boton4 = tk.Button()
#El resto de los botones usan el paquete de ttk, por lo que no será posible hacer esas configuraciones
