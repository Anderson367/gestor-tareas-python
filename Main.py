import json
tareas = []
def agregar_tarea(descripcion):
    tarea = {"id": len(tareas)+1, "descripcion": descripcion, "completada": False}
    tareas.append(tarea)

def listar_tareas():
    for tarea in tareas:
        if tarea["completada"]:
            estado = "✔"
        else:
            estado = "❌"
    print (f'{tarea["id"]}. {tarea["descripcion"]} - {estado}')

def completar_tarea(id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True

def eliminar_tarea(id_tarea):
    global tareas
    tareas = [registro for registro in tareas if registro["id"] != id_tarea]

def guardar_tareas():
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

def cargar_tareas():
    global tareas
    try:
        with open("tareas.json", "r") as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        tareas = []

def menu():
    cargar_tareas()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Guardar y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            desc = input("Descripción de la tarea: ")
            agregar_tarea(desc)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            id_tarea = int(input("ID de la tarea a completar: "))
            completar_tarea(id_tarea)
        elif opcion == "4":
            id_tarea = int(input("ID de la tarea a eliminar: "))
            eliminar_tarea(id_tarea)
        elif opcion == "5":
            guardar_tareas()
            print("Tareas guardadas. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
     
if __name__ == "__main__":
    menu()