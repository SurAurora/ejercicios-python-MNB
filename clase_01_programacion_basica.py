"""
Clase 1 - Programacion basica en Python

Complete los espacios marcados con TODO.
Ejecute este archivo con:

    python clase_01_programacion_basica.py
"""


# ============================================================
# A. Variables
# ============================================================
print("A. Variables")

# A1. Temperatura estimada
T_12 = 18.5
dT_dt = 1.2
dt = 1
T_13 = None  # TODO
print("A1. Temperatura estimada a las 13:00:", T_13)

# A2. Conversion de temperatura
T_C = 22.4
T_K = None  # TODO
print("A2. Temperatura en Kelvin:", T_K)

# A3. Rapidez del viento
u = 6.0
v = 8.0
rapidez = None  # TODO
print("A3. Rapidez del viento:", rapidez)

# A4. Diferencia entre modelo y observacion
T_obs = 16.8
T_mod = 18.1
error = None      # TODO
error_abs = None  # TODO
print("A4. Error:", error, "| Error absoluto:", error_abs)

# A5. Precipitacion acumulada
p1 = 0.0
p2 = 1.2
p3 = 3.4
precipitacion_total = None  # TODO
print("A5. Precipitacion acumulada:", precipitacion_total)


# ============================================================
# B. Ciclo for
# ============================================================
print("\nB. Ciclo for")

# B1. Promedio de viento
viento = [2.5, 3.1, 4.0, 5.2, 3.8, 2.9, 6.1, 4.7]
suma_viento = 0

# TODO: use for para sumar los valores de viento

promedio_viento = None  # TODO
print("B1. Promedio de viento:", promedio_viento)

# B2. Temperatura maxima
temperaturas = [11.2, 13.5, 17.8, 21.0, 20.4, 16.9]
temperatura_maxima = temperaturas[0]

# TODO: use for para encontrar la temperatura maxima

print("B2. Temperatura maxima:", temperatura_maxima)

# B3. Conteo de horas calidas
horas_calidas = 0

# TODO: cuente temperaturas >= 20 grados C

print("B3. Horas calidas:", horas_calidas)

# B4. Error medio
obs = [10.0, 12.5, 14.0, 15.2]
mod = [11.0, 12.0, 15.5, 16.0]
suma_error = 0

# TODO: use for con indices para sumar los errores mod[i] - obs[i]

error_medio = None  # TODO
print("B4. Error medio:", error_medio)

# B5. Crear lista de anomalias
serie = [14.0, 15.5, 13.2, 16.1]
media = 14.7
anomalias = []

# TODO: agregue a anomalias cada valor - media

print("B5. Anomalias:", anomalias)


# ============================================================
# C. Condicionales if
# ============================================================
print("\nC. Condicionales if")

# C1. Clasificar temperatura
for T in [-3, 8, 19, 29]:
    categoria = "sin clasificar"  # TODO
    print("C1.", T, "grados C ->", categoria)

# C2. Clasificar viento
v_prueba = 9.2
categoria_viento = "sin clasificar"  # TODO
print("C2. Viento:", v_prueba, "m/s ->", categoria_viento)

# C3. Detectar lluvia
p = 1.4
categoria_lluvia = "sin clasificar"  # TODO
print("C3. Precipitacion:", p, "mm ->", categoria_lluvia)

# C4. Evaluar sesgo del modelo
error_modelo = T_mod - T_obs
categoria_sesgo = "sin clasificar"  # TODO
print("C4. Sesgo:", error_modelo, "->", categoria_sesgo)

# C5. Validar dato meteorologico
viento_registrado = -1.0
validez = "sin evaluar"  # TODO
print("C5. Viento registrado:", viento_registrado, "->", validez)


# ============================================================
# D. Ciclo while
# ============================================================
print("\nD. Ciclo while")

# D1. Contador de horas
hora = 0
horas = []

# TODO: use while para agregar las horas 0, 1, 2, 3, 4, 5

print("D1. Horas:", horas)

# D2. Aumento gradual de temperatura
T = 10.0
horas_hasta_20 = 0

# TODO: use while hasta que T >= 20.0

print("D2. Horas hasta T >= 20:", horas_hasta_20, "| T final:", T)

# D3. Precipitacion acumulada hasta umbral
lluvia = [0.2, 0.0, 1.5, 2.1, 0.8, 3.0]
i = 0
acumulado = 0

# TODO: use while hasta acumulado >= 4.0 o hasta terminar la lista

print("D3. Lluvia acumulada:", acumulado, "| registros usados:", i)

# D4. Buscar primera hora con viento fuerte
viento_horario = [2.0, 3.5, 4.1, 8.5, 7.0]
i = 0
primera_hora_fuerte = None

# TODO: use while para encontrar la primera posicion con viento > 8

print("D4. Primera hora con viento fuerte:", primera_hora_fuerte)

# D5. Disminucion de contaminante
C = 80.0
horas_contaminante = 0

# TODO: use while hasta que C < 25.0

print("D5. Horas hasta C < 25:", horas_contaminante, "| C final:", C)


# ============================================================
# E. Funciones
# ============================================================
print("\nE. Funciones")


def clasificar_temperatura(T):
    """Clasifica una temperatura en grados C."""
    # TODO
    return "sin clasificar"


def promedio(datos):
    """Retorna el promedio de una lista numerica."""
    # TODO
    return None


def resumen_serie(datos):
    """Retorna promedio, minimo y maximo de una lista numerica."""
    # TODO
    return None


def error_absoluto_medio(obs, mod):
    """Retorna el error absoluto medio entre dos listas."""
    # TODO
    return None


def celsius_a_kelvin(T_C):
    """Convierte una temperatura de grados C a Kelvin."""
    # TODO
    return None


print("E1. Clasificar temperatura:", clasificar_temperatura(19.0))
print("E2. Promedio:", promedio(viento))
print("E3. Resumen:", resumen_serie(temperaturas))
print("E4. Error absoluto medio:", error_absoluto_medio(obs, mod))
print("E5. Celsius a Kelvin:", celsius_a_kelvin(22.4))

