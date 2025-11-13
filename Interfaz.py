import tkinter as tk
from tkinter import messagebox
import json

tareas = []

def cargar_tareas():
    global tareas
    try:
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        tareas = []

def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

def agregar_tarea():
    desc = entrada.get()
    if desc:
        tarea = {"id": len(tareas)+1, "descripcion": desc, "completada": False}
        tareas.append(tarea)
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Atención", "La descripción no puede estar vacía")

def completar_tarea():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = True
        actualizar_lista()

def eliminar_tarea():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        actualizar_lista()

def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        estado = "✔️" if tarea["completada"] else "❌"
        lista.insert(tk.END, f'{tarea["id"]}. {tarea["descripcion"]} - {estado}')
    guardar_tareas()

ventana = tk.Tk()
ventana.title("Gestor de Tareas")

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

btn_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Completar tarea", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

cargar_tareas()
actualizar_lista()

ventana.mainloop()