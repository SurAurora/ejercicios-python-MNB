"""
Clase 1 - Programacion basica en Python

Complete los espacios marcados con TODO.
Ejecute este archivo con:

    python clase_01_programacion_basica.py
"""


# ============================================================
# Ejercicio 1. Variables y calculo directo
# ============================================================
T_12 = 18.5
dT_dt = 1.2
dt = 1

# TODO: calcule T_13
T_13 = None

print("Ejercicio 1")
print("Temperatura estimada a las 13:00:", T_13, "grados C")


# ============================================================
# Ejercicio 2. Condicionales
# ============================================================
def clasificar_temperatura(T):
    """Clasifica una temperatura en grados C."""
    # TODO: reemplace este bloque por condicionales if/elif/else
    return "sin clasificar"


print("\nEjercicio 2")
for T in [-3, 8, 19, 29]:
    print(T, "grados C ->", clasificar_temperatura(T))


# ============================================================
# Ejercicio 3. Bucles con viento
# ============================================================
viento = [2.5, 3.1, 4.0, 5.2, 3.8, 2.9, 6.1, 4.7]

suma_viento = 0
max_viento = viento[0]
contador_viento_fuerte = 0

# TODO: use un bucle for para actualizar las tres variables anteriores

promedio_viento = None  # TODO: calcule el promedio

print("\nEjercicio 3")
print("Suma total:", suma_viento)
print("Promedio:", promedio_viento)
print("Maximo:", max_viento)
print("Registros con viento >= 5 m/s:", contador_viento_fuerte)


# ============================================================
# Ejercicio 4. Funcion reutilizable
# ============================================================
def resumen_serie(datos):
    """
    Retorna promedio, minimo y maximo de una lista.
    Si la lista esta vacia, retorna None.
    """
    # TODO: complete la funcion
    return None


print("\nEjercicio 4")
print("Resumen de viento:", resumen_serie(viento))
print("Resumen de lista vacia:", resumen_serie([]))


# ============================================================
# Ejercicio 5. Pseudocodigo llevado a Python
# ============================================================
def clasificar_viento(v):
    """Clasifica la intensidad del viento en m/s."""
    # TODO: implemente las categorias debil, moderado y fuerte
    return "sin clasificar"


print("\nEjercicio 5")
for v in [1.5, 4.0, 10.2]:
    print(v, "m/s ->", clasificar_viento(v))

