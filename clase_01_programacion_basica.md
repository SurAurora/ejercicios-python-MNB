# Clase 1 - Programacion basica en Python

**Objetivo:** practicar los pilares iniciales de programacion en Python:
variables, ciclos `for`, condicionales `if`, ciclos `while` y funciones,
usando ejemplos simples relacionados con meteorologia.

## A. Variables

### Ejercicio A1. Temperatura estimada

Una estacion meteorologica registra:

- temperatura a las 12:00: `T_12 = 18.5` grados C
- tendencia horaria: `dT_dt = 1.2` grados C/h
- intervalo de tiempo: `dt = 1` h

Calcule la temperatura estimada a las 13:00:

```python
T_13 = T_12 + dT_dt * dt
```

Muestre el resultado con un mensaje claro.

### Ejercicio A2. Conversion de temperatura

Convierta una temperatura de grados Celsius a Kelvin usando:

```python
T_K = T_C + 273.15
```

Use `T_C = 22.4` grados C.

### Ejercicio A3. Rapidez del viento

Las componentes del viento son:

- `u = 6.0` m/s
- `v = 8.0` m/s

Calcule la rapidez del viento:

```python
rapidez = (u**2 + v**2)**0.5
```

### Ejercicio A4. Diferencia entre modelo y observacion

Una observacion de temperatura es `T_obs = 16.8` grados C y el modelo entrega
`T_mod = 18.1` grados C.

Calcule:

- `error = T_mod - T_obs`
- `error_abs = abs(error)`

### Ejercicio A5. Precipitacion acumulada

Una estacion registra precipitacion horaria:

- `p1 = 0.0` mm
- `p2 = 1.2` mm
- `p3 = 3.4` mm

Calcule la precipitacion acumulada total.

## B. Ciclo for

### Ejercicio B1. Promedio de viento

Dada la lista:

```python
viento = [2.5, 3.1, 4.0, 5.2, 3.8, 2.9, 6.1, 4.7]
```

Use un ciclo `for` para calcular el promedio. No use `sum()`.

### Ejercicio B2. Temperatura maxima

Dada la lista:

```python
temperaturas = [11.2, 13.5, 17.8, 21.0, 20.4, 16.9]
```

Use un ciclo `for` para encontrar la temperatura maxima. No use `max()`.

### Ejercicio B3. Conteo de horas calidas

Con la lista `temperaturas` del ejercicio anterior, cuente cuantas horas tienen
temperatura mayor o igual a 20 grados C.

### Ejercicio B4. Error medio

Dadas las listas:

```python
obs = [10.0, 12.5, 14.0, 15.2]
mod = [11.0, 12.0, 15.5, 16.0]
```

Use un ciclo `for` con indices para calcular el error medio:

```python
error_medio = promedio(mod - obs)
```

### Ejercicio B5. Crear una lista de anomalias

Dada la serie:

```python
serie = [14.0, 15.5, 13.2, 16.1]
media = 14.7
```

Cree una nueva lista llamada `anomalias`, donde cada elemento sea:

```python
anomalia = valor - media
```

## C. Condicionales if

### Ejercicio C1. Clasificar temperatura

Escriba una condicion que clasifique una temperatura `T`:

- `"helada"` si `T < 0`
- `"frio"` si `0 <= T <= 15`
- `"templado"` si `15 < T <= 25`
- `"caluroso"` si `T > 25`

Pruebe con `T = -3`, `8`, `19` y `29`.

### Ejercicio C2. Clasificar viento

Clasifique una rapidez de viento `v`:

- `"debil"` si `v < 3`
- `"moderado"` si `3 <= v <= 8`
- `"fuerte"` si `v > 8`

### Ejercicio C3. Detectar lluvia

Dada una precipitacion horaria `p`, muestre:

- `"sin lluvia"` si `p == 0`
- `"lluvia debil"` si `0 < p < 2`
- `"lluvia moderada o intensa"` si `p >= 2`

### Ejercicio C4. Evaluar sesgo del modelo

Dado un error `error = T_mod - T_obs`, indique:

- `"modelo frio"` si `error < 0`
- `"modelo sin sesgo"` si `error == 0`
- `"modelo calido"` si `error > 0`

### Ejercicio C5. Validar dato meteorologico

Una rapidez de viento no deberia ser negativa. Dado `viento_registrado`,
muestre:

- `"dato invalido"` si es negativo
- `"dato valido"` si es cero o positivo

## D. Ciclo while

### Ejercicio D1. Contador de horas

Use `while` para imprimir las horas desde `0` hasta `5`.

### Ejercicio D2. Aumento gradual de temperatura

La temperatura inicial es `T = 10.0` grados C. Cada hora aumenta `1.5` grados C.
Use `while` para calcular cuantas horas pasan hasta que `T >= 20.0`.

### Ejercicio D3. Precipitacion acumulada hasta umbral

Use la lista:

```python
lluvia = [0.2, 0.0, 1.5, 2.1, 0.8, 3.0]
```

Con `while`, sume la lluvia hasta que la acumulacion sea mayor o igual a `4.0`
mm o hasta terminar la lista.

### Ejercicio D4. Buscar primera hora con viento fuerte

Use la lista:

```python
viento_horario = [2.0, 3.5, 4.1, 8.5, 7.0]
```

Con `while`, encuentre la primera posicion donde el viento sea mayor a `8` m/s.

### Ejercicio D5. Disminucion de contaminante

Una concentracion inicial es `C = 80.0` ug/m3. Cada hora disminuye un 20%.
Use `while` para calcular cuantas horas pasan hasta que `C < 25.0`.

## E. Funciones

### Ejercicio E1. Funcion para clasificar temperatura

Cree una funcion `clasificar_temperatura(T)` que implemente las categorias del
ejercicio C1.

### Ejercicio E2. Funcion para promedio

Cree una funcion `promedio(datos)` que reciba una lista numerica y retorne el
promedio. Si la lista esta vacia, debe retornar `None`.

### Ejercicio E3. Funcion para resumen de serie

Cree una funcion `resumen_serie(datos)` que retorne tres valores:

- promedio
- minimo
- maximo

Si la lista esta vacia, debe retornar `None`.

### Ejercicio E4. Funcion para error absoluto medio

Cree una funcion `error_absoluto_medio(obs, mod)` que reciba dos listas del
mismo largo y retorne el promedio de los errores absolutos.

### Ejercicio E5. Funcion para convertir Celsius a Kelvin

Cree una funcion `celsius_a_kelvin(T_C)` que retorne la temperatura en Kelvin.

## Pregunta breve

Explique en 3 a 5 lineas por que las funciones son utiles cuando se analizan
muchas estaciones meteorologicas o muchas salidas de un modelo numerico.

