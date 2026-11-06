from tkinter import *
from tkinter import ttk

azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#B0C6E6"
gris = "#6b7280"
texto = "#111827"
borde = "#d1d5db"
celeste= "#abdbee"

def treeview(contenedor, encabezados,datos):
    frame=Frame(contenedor)
    frame.grid(column=0,row=0,padx=5, pady=10)
    tree=ttk.Treeview(frame, columns=encabezados, show="headings") #headings oculta la columna fantasma de python
    for titulo in encabezados:
        tree.heading(titulo, text=titulo, anchor="center") #le asigna a cada columna us nombre
        tree.column(titulo, anchor="center", width=120)
    tree.tag_configure('par',background=celeste)
    tree.tag_configure('impar',background='white')
    nro=1
    for fila in datos:
        if nro % 2 == 0:
            tree.insert('','end', values=fila,tags=('par',)) #'' se deja vacio siempre para estas tabalas, end para que se inserte al final
        else:
            tree.insert('','end', values=fila,tags=('impar',))
        nro+=1
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
    
