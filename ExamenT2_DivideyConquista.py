import random

def generar_coordenadas(cant):  # Generamos coordenadas
    matriz = []
    for _ in range(cant):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        matriz.append([x, y])
    return matriz

def distancia(coordenada):
    x, y = coordenada
    return x**2 + y**2  # método de Pitágoras a^2 = b^2 + c^2

# Algoritmo de Divide y Conquista
def coordenadamasLejana(lista):
    if len(lista) == 1:
        x = lista[0][0]
        y = lista[0][1]
        if x > 0 and y < 0:
            return lista[0]
        else:
            return [0, 0]  # si no es del cuarto cuadrante
    else:
        mitad = len(lista) // 2
        izquierda = coordenadamasLejana(lista[:mitad])
        derecha = coordenadamasLejana(lista[mitad:])

        dist_izq = distancia(izquierda)
        dist_der = distancia(derecha)

        if dist_izq > dist_der:
            return izquierda
        else:
            return derecha

# Función principal
def main():
    cantidad = int(input("Ingrese la cantidad de coordenadas que desea generar: "))
    coordenadas = generar_coordenadas(cantidad)

    print("\nCoordenadas generadas:")
    for par in coordenadas:
        print(par)

    resultado = coordenadamasLejana(coordenadas)

    # Si el resultado es [0, 0], no se encontró ninguno válido
    if resultado[0] == 0 and resultado[1] == 0:
        print("\nLo sentimos, no hay coordenadas en el cuarto cuadrante D:")
    else:
        print("\nCoordenada más alejada en el cuarto cuadrante:")
        print(resultado)

# Ejecutar
main()
