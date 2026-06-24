"""
Clase 2 - Analisis de series de tiempo atmosfericas

Complete los espacios marcados con TODO.
Ejecute este archivo desde la carpeta ejercicios_python:

    python clase_02_series_tiempo.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# Ejercicio 1. Lectura e inspeccion
# ============================================================
datos = pd.read_csv("datos_clase_02_series.csv")

print("Ejercicio 1")
print(datos.head())
print("Numero de filas:", None)  # TODO
print("Columnas:", None)         # TODO
print("Rango horario:", None)    # TODO


# ============================================================
# Ejercicio 2. Estadistica descriptiva
# ============================================================
hora = datos["hora"]
temperatura_obs = datos["temperatura_obs"]
temperatura_modelo = datos["temperatura_modelo"]
viento_obs = datos["viento_obs"]
viento_modelo = datos["viento_modelo"]

# TODO: calcule estadisticos de temperatura_obs y viento_obs

print("\nEjercicio 2")
print("Promedio temperatura observada:", None)
print("Desviacion estandar temperatura observada:", None)
print("Minimo temperatura observada:", None)
print("Maximo temperatura observada:", None)
print("Hora temperatura maxima:", None)
print("Promedio viento observado:", None)
print("Desviacion estandar viento observado:", None)


# ============================================================
# Ejercicio 3. Comparacion observacion-modelo
# ============================================================
# TODO: calcule errores, sesgos y errores absolutos medios

print("\nEjercicio 3")
print("Sesgo medio temperatura:", None)
print("Error absoluto medio temperatura:", None)
print("Sesgo medio viento:", None)
print("Error absoluto medio viento:", None)


# ============================================================
# Ejercicio 4. Tendencia y regresion lineal
# ============================================================
# TODO: ajuste una recta con np.polyfit
pendiente = None
intercepto = None
temperatura_ajustada = None

print("\nEjercicio 4")
print("Pendiente:", pendiente, "grados C/h")
print("Intercepto:", intercepto, "grados C")

# TODO: grafique temperatura_obs y temperatura_ajustada


# ============================================================
# Ejercicio 5. Correlacion
# ============================================================
# TODO: use np.corrcoef o pandas.Series.corr

print("\nEjercicio 5")
print("Correlacion temperatura obs-modelo:", None)
print("Correlacion viento obs-modelo:", None)
print("Correlacion temperatura-viento observado:", None)


# ============================================================
# Ejercicio 6. Analisis de compuestos
# ============================================================
def clasificar_periodo(h):
    """Clasifica una hora del dia en madrugada, manana, tarde o noche."""
    # TODO: complete la funcion
    return "sin clasificar"


datos["periodo"] = datos["hora"].apply(clasificar_periodo)

# TODO: calcule promedios por periodo
compuestos = None

print("\nEjercicio 6")
print(compuestos)

# TODO: grafique compuestos de temperatura y viento


# ============================================================
# Ejercicio 7. Figuras finales
# ============================================================
# TODO: grafique temperatura observada/modelada y viento observado/modelado

plt.show()

