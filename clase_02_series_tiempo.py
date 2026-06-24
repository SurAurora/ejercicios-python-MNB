"""
Clase 2 - Analisis de temperatura media diaria en Quinta Normal

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
datos = pd.read_csv("datos/QN_TEMP.csv")
datos.columns = datos.columns.str.strip()

print("Ejercicio 1")
print(datos.head())
print("Numero de filas:", None)       # TODO
print("Columnas:", None)              # TODO
print("Primer año disponible:", None) # TODO
print("Ultimo año disponible:", None) # TODO
print("Temperatura minima:", None)    # TODO
print("Temperatura maxima:", None)    # TODO


# ============================================================
# Ejercicio 2. Crear una columna de fecha
# ============================================================
# TODO: cree la columna fecha con pd.to_datetime
datos["fecha"] = None

# TODO: ordene la tabla por fecha

print("\nEjercicio 2")
print("Primera fecha:", None)          # TODO
print("Ultima fecha:", None)           # TODO
print("Dias con observacion:", None)   # TODO
print("Dias calendario:", None)        # TODO
print("Dias faltantes:", None)         # TODO


# ============================================================
# Ejercicio 3. Estadistica descriptiva
# ============================================================
temperatura = datos["valor"]

# TODO: calcule estadisticos de temperatura

print("\nEjercicio 3")
print("Promedio:", None)
print("Desviacion estandar:", None)
print("Minimo:", None)
print("Maximo:", None)
print("Percentil 10:", None)
print("Percentil 90:", None)
print("Fecha temperatura minima:", None)
print("Fecha temperatura maxima:", None)


# ============================================================
# Ejercicio 4. Climatologia mensual
# ============================================================
# TODO: calcule la temperatura media por mes
climatologia_mensual = None

print("\nEjercicio 4")
print(climatologia_mensual)
print("Mes mas calido:", None)
print("Mes mas frio:", None)
print("Amplitud anual aproximada:", None)

# TODO: grafique la climatologia mensual


# ============================================================
# Ejercicio 5. Anomalias respecto a la climatologia mensual
# ============================================================
# TODO: cree climatologia_mensual y anomalia para cada dia

print("\nEjercicio 5")
print("Promedio de anomalias:", None)
print("Desviacion estandar de anomalias:", None)
print("Fecha anomalia positiva mas alta:", None)
print("Fecha anomalia negativa mas baja:", None)


# ============================================================
# Ejercicio 6. Tendencia anual
# ============================================================
# TODO: calcule temperatura media anual
temperatura_anual = None

# TODO: ajuste una recta con np.polyfit
pendiente = None
intercepto = None
tendencia = None

print("\nEjercicio 6")
print("Pendiente:", pendiente, "grados C/año")
print("Pendiente:", None, "grados C/decada")  # TODO

# TODO: grafique temperatura_anual y tendencia


# ============================================================
# Ejercicio 7. Dias calidos y frios
# ============================================================
# TODO: calcule umbrales con quantile
umbral_frio = None
umbral_calido = None


def clasificar_dia(valor):
    """Clasifica un dia como frio, normal o calido."""
    # TODO: use los umbrales definidos arriba
    return "sin clasificar"


# TODO: cree la columna categoria aplicando clasificar_dia

print("\nEjercicio 7")
print("Umbral frio:", umbral_frio)
print("Umbral calido:", umbral_calido)
print("Cantidad de dias frios:", None)
print("Cantidad de dias calidos:", None)
print("Mes con mas dias calidos:", None)
print("Mes con mas dias frios:", None)


# ============================================================
# Ejercicio 8. Promedios por decada
# ============================================================
# TODO: cree columna decada y calcule temperatura media por decada
temperatura_decadal = None

print("\nEjercicio 8")
print(temperatura_decadal)

# TODO: grafique temperatura_decadal


# ============================================================
# Ejercicio 9. Figuras finales
# ============================================================
# TODO: figura 1, serie completa de temperatura media diaria
# TODO: figura 2, climatologia mensual
# TODO: figura 3, temperatura media anual con tendencia

plt.show()

