from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

def solucionarEcuacion (coef1, coef2, coef3) :
    ecuacionSegundoGrado = EcuacionSegundoGrado([coef1, coef2, coef3])
    ecuacionSegundoGrado.calcular_raices( )
    ecuacionSegundoGrado.imprimir_raices( )

if __name__ == '__main__':
    print("Ecuación 1:")
    solucionarEcuacion(3, -5, 1)
