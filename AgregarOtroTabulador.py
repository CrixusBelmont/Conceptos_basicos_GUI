import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Componentes')
ventana.iconbitmap('icono.ico')

def crear_componentes_tabulador1(tabulador):
    # Agregar una etiqueta y un componente de entrada
    etiqueta1 = ttk.Label(tabulador, text='Nombre:')
    etiqueta1.grid(row=0, column=0, sticky=tk.E)
    entrada1 = ttk.Entry(tabulador, width=30)
    entrada1.grid(row=0, column=1, padx=5, pady=5)

    # Agregamos un botón
    def enviar():
        messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

    boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
    boton1.grid(row=1, column=0, columnspan=2)


def crear_tabs():
    # Creamos un tab control, para ello usamos la clase Notebook
    control_tabulador = ttk.Notebook(ventana)
    # Agregamos un marco (frame) para agregar dentrol del tab y organizar elementos
    tabulador1 = ttk.Frame(control_tabulador)
    # Agregamos el tabulador al control de tabuladores
    control_tabulador.add(tabulador1, text='Tabulador 1')
    # Mostramos el tabulador
    control_tabulador.pack(fill='both')
    # Creamos los componentes del tabulador1
    crear_componentes_tabulador1(tabulador1)
    # Creamos un segundo tabulador
    tabulador2 = ttk.LabelFrame(control_tabulador, text='Contenido')
    control_tabulador.add(tabulador2, text='Tabulador 2')

crear_tabs()

ventana.mainloop()

#La diferencia aqui en comparacion al archivo de tabuladores es que los codigos de agregar los componentes de
#Entrada y etiqueta pasaron  ser definidos como un metodo que se llama crear_componentes_tabulador1
#Originalmente los codigos mencionados estaban escritos debajo del metodo crear tab
#Sin embargo como pasaron ser definidos como un metodo entonces el codigo pasó a estar arriba del metodo crear tabs


#Ver el archivo de continuacion: Tabulador Scrolled Tex