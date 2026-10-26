from tkinter import *
from tkinter import ttk

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

