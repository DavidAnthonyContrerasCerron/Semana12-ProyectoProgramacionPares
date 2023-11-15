import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado, ExceptionDatos


class PruebaRaices(unittest.TestCase):
    def setUp(self):
        self.ecuacionSegundoGrado = EcuacionSegundoGrado([])

    def tearDown(self):
        self.ecuacionSegundoGrado = None

    def test_TresCoeficientesEnteros_retornaRaicesReales(self):
        # Arrange
        self.ecuacionSegundoGrado.coeficientes = [3, -5, 1]
        raiz1 = 1.43
        raiz2 = 0.23

        # Do
        raiz1Calculada, raiz2Calculada = self.ecuacionSegundoGrado.calcular_raices()

        # Assert
        self.assertAlmostEqual(raiz1Calculada, raiz1, places=2)
        self.assertAlmostEqual(raiz2Calculada, raiz2, places=2)
