from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

def solucionarEcuacion (coef1, coef2, coef3):
    ecuacionSegundoGrado = EcuacionSegundoGrado([coef1, coef2, coef3])
    raiz1, raiz2 = ecuacionSegundoGrado.calcular_raices()
    print(f"Raíz 1: {raiz1}\nRaíz 2: {raiz2}")

if __name__ == '__main__':
    print("Ecuación 1:")
    solucionarEcuacion(1, 1, 1)
    print("\nEcuación 2:")
    solucionarEcuacion(1, 2, 1)
