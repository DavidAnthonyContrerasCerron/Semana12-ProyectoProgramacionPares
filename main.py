from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

def solucionarEcuacion (coef1, coef2, coef3):
    ecuacionSegundoGrado = EcuacionSegundoGrado([coef1, coef2, coef3])
    raiz1, raiz2 = ecuacionSegundoGrado.calcular_raices()
    print(f"Raíz 1: {raiz1}\nRaíz 2: {raiz2}")

if __name__ == '__main__':
    solucionarEcuacion(1, 1, 1)
