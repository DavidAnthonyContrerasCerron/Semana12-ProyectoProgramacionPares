import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado, ExceptionDatos


class PruebaRaices(unittest.TestCase):
    def setUp(self):
        self.ecuacionSegundoGrado = EcuacionSegundoGrado([3, -5, 1])

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

    def test_TresCoeficientesNoNumericos_lanzaException(self):
        # Act y Assert
        with self.assertRaises(ExceptionDatos):
            self.ecuacionSegundoGrado.coeficientes = ["a", "b", "c"]

    def test_RaicesComplejas_retornaRaicesComplejas(self):
        # Arrange
        self.ecuacionSegundoGrado.coeficientes = [1, 0, 1]
        raiz1 = complex(0, 1)
        raiz2 = complex(0, -1)

        # Do
        raiz1Calculada, raiz2Calculada = self.ecuacionSegundoGrado.calcular_raices()

        # Assert
        self.assertEqual(raiz1Calculada, raiz1)
        self.assertEqual(raiz2Calculada, raiz2)