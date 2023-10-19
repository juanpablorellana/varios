###         PIDOU          ###
from tkinter import *
from tkinter import ttk
import string
import random

ventana = Tk()
ventana.geometry("300x225")
ventana.title("Creador De Contraseñas")
ventana.configure(background = "#212226")
# ventana.iconbitmap("./logo.ico")
'''
principal = Frame(ventana).pack(fill = BOTH, expand = 1)
canvas = Canvas(principal).pack(side = LEFT, fill = BOTH, expand = 1)
barra = ttk.Scrollbar(principal, orient = VERTICAL, command = canvas.yview).pack(side = RIGHT, fill = Y)
canvas.configure(yscrollcommand = barra.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
segunda = Frame(canvas)
canvas.create_window((0,0), window = segunda, anchor = "nw")
'''

def crear():
    contra = ""
    caracteres = list(string.printable)
    caracteres = caracteres[:-6]
    for i in range(int(texto.get())):
        contra += random.choice(caracteres)
    contraseña = Label(ventana, text = contra, font = ("Helvelica", 15), bg = "#212226", fg = "white").pack(pady = 5)
    cant = len(caracteres)
    prob = ("Probablildad de adivinarla de {:.1e}".format((1/cant) ** int(texto.get())) + "%")
    probtxt = Label(ventana, text = prob, font = ("Helvelica", 8), bg = "#212226", fg = "white").pack()
    def copy():
        ventana.clipboard_clear()
        ventana.clipboard_append(contra)
    copiar = Button(ventana, text = "Copiar", command = copy).pack(pady = 10)
    
    #def borrar():
    #    contraseña.destroy()
    #    copiar.destroy()
    #botonborrar = Button(ventana, text = "Borrar", command = borrar, justify = RIGHT).place(x = 200, y = 80)

titulo = Label(ventana, text = "Crea tu contraseña segura", font = ("Helvelica", 15), bg = "#212226", fg = "white").pack(pady = 10)

texto = StringVar()
texto.set("Selecciona Dígitos")

op = ("4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")

opciones = ttk.Combobox(ventana, textvariable = texto, values = op).pack()

boton = Button(ventana, text = "Crear contraseña", command = crear).pack(pady = 10)

ventana.mainloop()
###         PIDOU          ###