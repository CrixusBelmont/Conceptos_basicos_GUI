#GUI - Graphical User Interface
#TKinker - TK Interface
#Importamos el modulo de TKinker
import tkinter as tk
#Importamos el modulo del tema de tkinker
from tkinter import ttk

#Creamos un objeto usando la clase tk
ventana = tk.Tk()

#Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')

#Cambiamos el nombre de la ventana
ventana.title('Nueva ventana')

#Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')

#Definimos el metodo evento click
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecuion del evento click')
    #Creamos un nuevo boton y la mostramos
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()

#creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)
boton1.grid(row=0, column=0, sticky='E')
#row y column son para cambiar la posicion del boton, no funciona si el metodo .pack() está activo
#sticky es para cargar el boton y sus valores son puntos cardenales en ingles, E de east

#Utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()

#Iniciamos la ventana (esta linea la ejecutamos al final)
#Si la ejecutamos antes no se van a mostrar la configuracion
ventana.mainloop()