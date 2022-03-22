import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Cambio de texto para el botón')
ventana.iconbitmap('icono.ico')

# width es la cantidad de caracteres que ocupa la caja de texto
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
# state=tk.DISABLED
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)

#show es para cuendo el usuario escriba, independientemente de lo que ponga aparecerá lo que declares
#en este caso lo declarado es un *. Eso sirve para las contraseñas

#En caso de querer deshabilitar una caja de texto, se usa state=tk.DISABLED
#En caso de solo lectura, state='readonly'

# insert agrega un texto
entrada1.insert(0,'Introduce una cadena')
entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')

def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminar el contenido
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto de la caja
    entrada1.select_range(0, tk.END)
    # Para hacer efectiva la selección del texto
    entrada1.focus()

# Creamos un botón
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
