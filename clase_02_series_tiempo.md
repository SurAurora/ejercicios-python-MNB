# Clase 2 - Analisis de series de tiempo atmosfericas con Python

**Objetivo:** aplicar `numpy`, `pandas` y `matplotlib` para analizar series de
tiempo, calcular estadisticos, comparar observaciones con una simulacion y
construir una interpretacion meteorologica breve.

Use el archivo `datos_clase_02_series.csv`.

## Ejercicio 1. Lectura e inspeccion

Lea el archivo CSV con `pandas`.

Responda:

- Cuantas filas tiene la tabla?
- Cuales son los nombres de las columnas?
- Cual es el rango horario de la serie?

## Ejercicio 2. Estadistica descriptiva

Para `temperatura_obs`, calcule:

- promedio
- desviacion estandar
- minimo
- maximo
- hora de la temperatura maxima

Repita el promedio y la desviacion estandar para `viento_obs`.

## Ejercicio 3. Comparacion observacion-modelo

Calcule el error del modelo:

```python
error_T = temperatura_modelo - temperatura_obs
error_viento = viento_modelo - viento_obs
```

Luego calcule:

- sesgo medio de temperatura
- error absoluto medio de temperatura
- sesgo medio de viento
- error absoluto medio de viento

Interprete si el modelo esta, en promedio, mas calido/frio y con mas/menos
viento que las observaciones.

## Ejercicio 4. Tendencia y regresion lineal

Ajuste una recta simple entre hora y temperatura observada:

```python
coef = np.polyfit(hora, temperatura_obs, 1)
pendiente = coef[0]
intercepto = coef[1]
```

Grafique la serie observada y la recta ajustada.

Responda:

- Que unidades tiene la pendiente?
- Es razonable interpretar una unica tendencia lineal para todo el dia?

## Ejercicio 5. Correlacion

Calcule la correlacion entre:

- `temperatura_obs` y `temperatura_modelo`
- `viento_obs` y `viento_modelo`
- `temperatura_obs` y `viento_obs`

Comente cual relacion es mas fuerte y cual requiere mas cuidado al interpretarse.

## Ejercicio 6. Analisis de compuestos

Cree una nueva columna `periodo` con estas categorias:

- `madrugada`: 0 a 5 h
- `manana`: 6 a 11 h
- `tarde`: 12 a 17 h
- `noche`: 18 a 23 h

Calcule el promedio por periodo para:

- temperatura observada
- viento observado
- precipitacion

Grafique los promedios de temperatura y viento por periodo.

## Ejercicio 7. Figuras finales

Genere dos figuras:

1. Temperatura observada y modelada vs hora.
2. Viento observado y modelado vs hora.

Cada figura debe incluir titulo, ejes con unidades, leyenda y grilla.

