from tkinter import *
from tkinter import ttk

azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#B0C6E6"
gris = "#6b7280"
texto = "#111827"
borde = "#d1d5db"

def treeview(contenedor, encabezados,datos):
    frame=Frame(contenedor)
    frame.grid(column=0,row=0)
    tree=ttk.Treeview(frame, columns=encabezados, show="headings") #headings oculta la columna fantasma de python
    for titulo in encabezados:
        tree.heading(titulo, text=titulo) #le asigna a cada columna us nombre
        
    for fila in datos:
        tree.insert('','end', values=fila) #'' se deja vacio siempre para estas tabalas, end para que se inserte al final
    
    barra_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview) #.yview mueve el ejey
    tree.configure(yscrollcommand=barra_scroll.set)#para cuando se mueva la ruedita se mueva la barra
    
    tree.pack(side="left", fill="both", expand=True)#expand para cuando se agranda la pagina
    barra_scroll.pack(side="right", fill="y") #fill hace qye se estire
    return tree

def crear_boton(nombre,fila,contenedor,comando):
    Button(
        contenedor,
        text=nombre,
        command=comando,
        font=("Arial", 10),
        bg=azul,
        fg=blanco,
        padx=30,
        pady=10
    ).grid(row=fila, column=0, padx=10, pady=10)
    
