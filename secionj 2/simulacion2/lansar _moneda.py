#lanzar dado
import random

def lanzar_dado():
    return random.randint(1, 6)

def calcular_probabilidades(num_lanzamientos):
    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(num_lanzamientos):
        resultado = lanzar_dado()
        resultados[resultado] += 1

    probabilidades = {cara: frecuencia / num_lanzamientos for cara, frecuencia in resultados.items()}
    return probabilidades

num_lanzamientos = 10000
probabilidades = calcular_probabilidades(num_lanzamientos)

print("Probabilidades de cada cara del dado:")
for cara, probabilidad in probabilidades.items():
    print(f"Cara {cara}: {probabilidad:.2f}")