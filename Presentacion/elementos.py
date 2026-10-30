from tkinter import *
from tkinter import ttk

azul = "#2864e8"
azul_oscuro = "#093068"
blanco = "#ffffff"
gris = "#6b7280"
texto = "#111827"

def treeview(contenedor, encabezados,datos):
    frame=Frame(contenedor)
    frame.grid(column=0,row=0)
    tree=ttk.Treeview(frame, columns=encabezados, show="headings")
    for titulo in encabezados:
        tree.heading(titulo, text=titulo)
        
    for fila in datos:
        tree.insert('', 'end', values=fila)
    
    barra_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=barra_scroll.set)
    
    tree.pack(side="left", fill="both", expand=True)
    barra_scroll.pack(side="right", fill="y")
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
    
