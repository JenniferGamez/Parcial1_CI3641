# test_buddy_system.py

import unittest
from buddy_system import BuddySystem
from io import StringIO
from unittest.mock import patch
import main 

class TestBuddySystem(unittest.TestCase):
    def setUp(self):
        self.buddy = BuddySystem(45)  # Crear una única instancia de BuddySystem

    def test_reservar_bloque(self):
        self.assertTrue(self.buddy.reservar_bloque("Proceso1", 4))
        self.assertFalse(self.buddy.reservar_bloque("Proceso1", 3))  # Intento de reasignar el mismo proceso1
        self.assertTrue(self.buddy.reservar_bloque("Proceso2", 2))
        self.assertTrue(self.buddy.reservar_bloque("Proceso3", 15))

    def test_liberar_bloque(self):
        self.assertFalse(self.buddy.liberar_bloque("Proceso2"))
        self.assertFalse(self.buddy.liberar_bloque("Proceso5"))
    
    def test_dividir_bloques(self):
        
        self.assertTrue(self.buddy.reservar_bloque("Proceso1", 4))
        self.assertTrue(self.buddy.reservar_bloque("Proceso2", 4))

        
        self.buddy.dividir_bloques(self.buddy.memoria[4][0], 3)

        # Verificamos si se crearon los bloques hijos y el bloque original se marcó como no disponible
        self.assertFalse(self.buddy.memoria[4][0].bloque_disp)  # El bloque original debe estar ocupado
        self.assertTrue(self.buddy.memoria[3][0].bloque_disp)  # Bloque hijo izquierdo debe estar libre

    def test_buscar_bloque(self):
        bloque = self.buddy.buscar_bloque(3)
        self.assertIsNotNone(bloque)
        self.assertTrue(bloque.bloque_libre())


class TestMain(unittest.TestCase):
    @patch("builtins.input", side_effect=["4", "MOSTRAR", "AYUDA", "SALIR"])
    def test_mostrar_ayuda_y_salir(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main.main()

        output = mock_stdout.getvalue()
        self.assertIn("Manejador de memoria que implementa el buddy system.", output)
        self.assertIn("Bloques de tamaño", output)  # Verifica la presencia de información sobre los bloques disponibles
        self.assertIn("Lista con los procesos que tienen bloques de memoria reservados.", output)  # Verifica la presencia de información de procesos
        self.assertIn("Instrucciones del programa:", output)  # Verifica que se imprima el mensaje de ayuda
        self.assertIn("Adiós!", output)  # Verifica que el programa muestra un mensaje de despedida

if __name__ == '__main__':
    unittest.main()
    