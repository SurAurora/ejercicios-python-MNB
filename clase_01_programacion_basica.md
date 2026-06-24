# Clase 1 - Programacion basica en Python

**Objetivo:** practicar los pilares de programacion revisados en clase:
variables, condicionales, bucles y funciones, usando ejemplos meteorologicos
simples.

## Ejercicio 1. Variables y calculo directo

Una estacion meteorologica registra:

- temperatura a las 12:00: `T_12 = 18.5` grados C
- tendencia horaria: `dT_dt = 1.2` grados C/h
- intervalo de tiempo: `dt = 1` h

Calcule la temperatura estimada a las 13:00 con:

```python
T_13 = T_12 + dT_dt * dt
```

Muestre el resultado con un mensaje claro.

## Ejercicio 2. Condicionales

Escriba una funcion `clasificar_temperatura(T)` que retorne:

- `"helada"` si `T < 0`
- `"frio"` si `0 <= T <= 15`
- `"templado"` si `15 < T <= 25`
- `"caluroso"` si `T > 25`

Pruebe la funcion con las temperaturas: `-3`, `8`, `19`, `29`.

## Ejercicio 3. Bucles con viento

Dada la lista:

```python
viento = [2.5, 3.1, 4.0, 5.2, 3.8, 2.9, 6.1, 4.7]
```

Use un bucle `for` para calcular:

- suma total
- promedio
- valor maximo
- cantidad de registros con viento mayor o igual a 5 m/s

En este ejercicio no use `numpy`.

## Ejercicio 4. Funcion reutilizable

Cree una funcion `resumen_serie(datos)` que reciba una lista numerica y retorne:

- promedio
- minimo
- maximo

La funcion debe manejar el caso de una lista vacia retornando `None`.

## Ejercicio 5. Pseudocodigo

Escriba pseudocodigo para clasificar la intensidad de viento:

- menor que 3 m/s: `"debil"`
- entre 3 y 8 m/s: `"moderado"`
- mayor que 8 m/s: `"fuerte"`

Luego implemente ese pseudocodigo como una funcion de Python.

## Pregunta breve

Explique en 3 a 5 lineas por que una funcion es util cuando se analizan muchas
estaciones meteorologicas o muchas salidas de un modelo numerico.

