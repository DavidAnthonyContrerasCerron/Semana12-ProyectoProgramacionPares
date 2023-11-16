import cmath

class ExceptionDatos(Exception):
    pass


class EcuacionSegundoGrado:
    def __init__(self, coeficientes):
        self.__coeficientes = self.validarCoeficientes(coeficientes)
        self.raiz1 = 0
        self.raiz2 = 0

    def validarCoeficientes(self, coeficientes):
        if coeficientes is not None:
            if len(coeficientes) != 3:
                raise ExceptionDatos("Se requieren tres coeficientes.")
            for coeficiente in coeficientes:
                if not isinstance(coeficiente, (int, float)):
                    raise ExceptionDatos("Los coeficientes deben ser números.")
            return coeficientes
        else:
            raise ExceptionDatos("Se requieren tres coeficientes.")

    @property
    def coeficientes(self):
        return self.__coeficientes

    @coeficientes.setter
    def coeficientes(self, coeficientes):
        try:
            self.__coeficientes = self.validarCoeficientes(coeficientes)
        except ExceptionDatos as e:
            raise e

    def calcular_raices(self):
        a, b, c = self.__coeficientes

        discriminante = b ** 2 - 4 * a * c

        if discriminante > 0:
            Raiz1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
            Raiz2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
            return Raiz1.real, Raiz2.real

        elif discriminante == 0:
            Raiz1 = -b / (2 * a)
            return Raiz1.real, Raiz1.real

        else:
            Raiz1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
            Raiz2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
            return Raiz1, Raiz2

    def imprimir_raices(self):
        print(f"Raiz 1: {self.raiz1}\nRaiz 2: {self.raiz2}")
