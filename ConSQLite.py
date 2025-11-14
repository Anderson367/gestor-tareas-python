import sqlite3
import tkinter as tk
from tkinter import messagebox

def crear_tabla():
    conn = sqlite3.connect("Gestor de tareas/tareas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            completada INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def agregar_tarea(desc):
    conn = sqlite3.connect("Gestor de tareas/tareas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tareas (descripcion) VALUES (?)", (desc,))
    conn.commit()
    conn.close()
    actualizar_lista()

def listar_tareas():
    conn = sqlite3.connect("Gestor de tareas/tareas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas")
    datos = cursor.fetchall()
    conn.close()
    return datos

def completar_tarea(id_tarea):
    conn = sqlite3.connect("Gestor de tareas/tareas.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas SET completada=1 WHERE id=?", (id_tarea,))
    conn.commit()
    conn.close()
    actualizar_lista()

def eliminar_tarea(id_tarea):
    conn = sqlite3.connect("Gestor de tareas/tareas.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id=?", (id_tarea,))
    conn.commit()
    conn.close()
    actualizar_lista()

def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in listar_tareas():
        estado = "✔️" if tarea[2] else "❌"
        lista.insert(tk.END, f'{tarea[0]}. {tarea[1]} - {estado}')

def agregar():
    desc = entrada.get()
    if desc:
        agregar_tarea(desc)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Atención", "La descripción no puede estar vacía")

def completar():
    seleccion = lista.curselection()
    if seleccion:
        id_tarea = int(lista.get(seleccion[0]).split(".")[0])
        completar_tarea(id_tarea)

def eliminar():
    seleccion = lista.curselection()
    if seleccion:
        id_tarea = int(lista.get(seleccion[0]).split(".")[0])
        eliminar_tarea(id_tarea)

ventana = tk.Tk()
ventana.title("Gestor de Tareas con SQLite")

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

tk.Button(ventana, text="Agregar tarea", command=agregar).pack(pady=5)
tk.Button(ventana, text="Completar tarea", command=completar).pack(pady=5)
tk.Button(ventana, text="Eliminar tarea", command=eliminar).pack(pady=5)

lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

crear_tabla()
actualizar_lista()

ventana.mainloop()
