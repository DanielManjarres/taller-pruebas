import unittest
from gestor import GestorTareas

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorTareas()
        self.usuario = self.gestor.registrar_usuario("Daniel", "Manjarres", "Clave123*")

    def test_registro_usuario(self):
        self.assertEqual(self.usuario.nombre, "Daniel")
        self.assertEqual(self.usuario.apellido, "Manjarres")

    def test_contraseña_invalida(self):
        with self.assertRaises(ValueError):
            self.gestor.registrar_usuario("Ana", "Lopez", "123")

    def test_inicio_sesion(self):
        usuario_log = self.gestor.iniciar_sesion("Daniel", "Clave123*")
        self.assertEqual(usuario_log.nombre, "Daniel")

    def test_crear_tarea(self):
        tarea = self.gestor.crear_tarea(self.usuario, "Estudiar", "Repasar Python", "Alta")
        self.assertEqual(tarea.titulo, "Estudiar")

    def test_buscar_tareas_por_prioridad(self):
        self.gestor.crear_tarea(self.usuario, "Dormir", "Descansar", "Baja")
        tareas_bajas = self.gestor.buscar_tareas(self.usuario, "Baja")
        self.assertEqual(len(tareas_bajas), 1)

    def test_eliminar_tarea(self):
        self.gestor.crear_tarea(self.usuario, "Ejercicio", "Correr 5km")
        self.gestor.eliminar_tarea(self.usuario, "Ejercicio")
        self.assertEqual(len(self.usuario.tareas), 0)


if __name__ == '__main__':
    unittest.main()
