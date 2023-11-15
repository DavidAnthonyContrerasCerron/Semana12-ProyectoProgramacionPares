import cmath

class ExceptionDatos(Exception):
    pass


class EcuacionSegundoGrado:
    def __init__(self, coeficientes):
        if coeficientes is not None:
            self.__coeficientes = self.validarCoeficientes(coeficientes)
        else:
            raise ExceptionDatos("Se requieren tres coeficientes.")

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
            # Dos raíces reales distintas
            Raiz1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
            Raiz2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
            self.raiz1 = format(Raiz1.real, '.2f')
            self.raiz2 = format(Raiz2.real, '.2f')
            return self.raiz1, self.raiz2

        elif discriminante == 0:
            # Una raíz real (doble)

            Raiz1 = -b / (2 * a)
            self.raiz1 = format(Raiz1.real, '.2f')
            self.raiz2 = self.raiz1
            return self.raiz1, self.raiz2
        else:
            # Dos raíces complejas conjugadas
            Raiz1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
            Raiz2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
            self.raiz1 = round(Raiz1.real, 2) + round(Raiz1.imag, 2) * 1j
            self.raiz2 = round(Raiz2.real, 2) + round(Raiz2.imag, 2) * 1j
            return self.raiz1, self.raiz2

    def imprimir_raices(self):
        print(f"Raiz 1: {self.raiz1}\nRaiz 2: {self.raiz2}")
