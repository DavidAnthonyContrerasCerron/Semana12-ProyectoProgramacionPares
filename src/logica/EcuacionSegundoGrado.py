import cmath


class ExceptionDatos(Exception):
    pass


class EcuacionSegundoGrado:
    def __init__(self, coeficientes):
        self.__coeficientes = coeficientes

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
            raiz1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
            raiz2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
            return format(raiz1.real, '.2f'), format(raiz2.real, '.2f')

        elif discriminante == 0:
            # Una raíz real (doble)
            raiz = -b / (2 * a)
            return format(raiz.real, '.2f')
        else:
            # Dos raíces complejas conjugadas
            raiz1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
            raiz2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
            return complex(round(raiz1.real, 2), round(raiz1.imag, 2)), complex(round(raiz2.real, 2), round(raiz2.imag, 2))

ecSegGrado = EcuacionSegundoGrado([1, 1, 1])
raizcalculada1, raizcalculada2 = ecSegGrado.calcular_raices()
print(raizcalculada1)
print(raizcalculada2)
