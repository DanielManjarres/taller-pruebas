from gestor import GestorTareas

gestor = GestorTareas()

print("=== GESTOR DE TAREAS ===")
usuario = gestor.registrar_usuario("Daniel", "Manjarres", "Clave123*")
print(f"Usuario registrado: {usuario}")

tarea1 = gestor.crear_tarea(usuario, "Estudiar Python", "Repasar TDD", "Alta")
tarea2 = gestor.crear_tarea(usuario, "Hacer ejercicio", "30 minutos diarios", "Media")

print("\nTareas registradas:")
for t in usuario.tareas:
    print(t)

tarea1.marcar_completada()

print("\nTareas actualizadas:")
for t in usuario.tareas:
    print(t)
