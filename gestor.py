from datetime import datetime

class Usuario:
    def __init__(self, nombre, apellido, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.tareas = []

    def __repr__(self):
        return f"{self.nombre} {self.apellido}"


class Tarea:
    def __init__(self, titulo, descripcion, prioridad="Media", fecha_vencimiento=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False
        self.fecha_creacion = datetime.now()

    def marcar_completada(self):
        self.completada = True

    def __repr__(self):
        estado = "✔️" if self.completada else "❌"
        return f"[{estado}] {self.titulo} (Prioridad: {self.prioridad})"


class GestorTareas:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre, apellido, contraseña):
        if len(contraseña) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        nuevo_usuario = Usuario(nombre, apellido, contraseña)
        self.usuarios.append(nuevo_usuario)
        return nuevo_usuario

    def iniciar_sesion(self, nombre, contraseña):
        for u in self.usuarios:
            if u.nombre == nombre and u.contraseña == contraseña:
                return u
        raise ValueError("Credenciales incorrectas")

    def crear_tarea(self, usuario, titulo, descripcion, prioridad="Media", fecha_vencimiento=None):
        tarea = Tarea(titulo, descripcion, prioridad, fecha_vencimiento)
        usuario.tareas.append(tarea)
        return tarea

    def eliminar_tarea(self, usuario, titulo):
        usuario.tareas = [t for t in usuario.tareas if t.titulo != titulo]

    def buscar_tareas(self, usuario, prioridad=None):
        if prioridad:
            return [t for t in usuario.tareas if t.prioridad == prioridad]
        return usuario.tareas
