# Clase 2026-06-25 - Analisis de series de tiempo atmosfericas con Python

**Objetivo:** aplicar `pandas`, `numpy` y `matplotlib` para analizar una serie
de observaciones meteorologicas reales: temperatura media diaria en la estacion
Quinta Normal.

Use el archivo:

```text
datos/QN_TEMP.csv
```

El archivo contiene:

- `agno`: año de la observacion
- `mes`: mes de la observacion
- `dia`: dia de la observacion
- `valor`: temperatura media diaria en grados C

## Ejercicio 1. Lectura e inspeccion

Lea el archivo CSV con `pandas`.

Como los nombres de columnas pueden venir con espacios, limpie los nombres con:

```python
datos.columns = datos.columns.str.strip()
```

Responda:

- Cuantas filas tiene la tabla?
- Cuales son los nombres de las columnas?
- Cual es el primer año disponible?
- Cual es el ultimo año disponible?
- Cual es el rango de temperaturas observadas?

## Ejercicio 2. Crear una columna de fecha

Cree una columna llamada `fecha` usando `pd.to_datetime`.

Una forma posible es:

```python
datos["fecha"] = pd.to_datetime(
    dict(year=datos["agno"], month=datos["mes"], day=datos["dia"])
)
```

Luego:

- ordene la tabla por fecha
- verifique la primera y ultima fecha disponible
- cuente cuantos dias tiene la serie
- compare ese numero con la cantidad de dias entre la primera y ultima fecha

Comente si la serie tiene dias faltantes.

## Ejercicio 3. Estadistica descriptiva

Para la columna `valor`, calcule:

- promedio
- desviacion estandar
- minimo
- maximo
- percentil 10
- percentil 90

Identifique ademas:

- fecha de la temperatura media diaria minima
- fecha de la temperatura media diaria maxima

## Ejercicio 4. Climatologia mensual

Calcule la temperatura media para cada mes usando `groupby`.

Responda:

- Cual es el mes mas calido en promedio?
- Cual es el mes mas frio en promedio?
- Cual es la amplitud anual aproximada entre esos dos meses?

Grafique la climatologia mensual con una linea o barras.

## Ejercicio 5. Anomalias respecto a la climatologia mensual

Cree una columna `climatologia_mensual` que asigne a cada dia el promedio
climatologico de su mes.

Luego cree:

```python
datos["anomalia"] = datos["valor"] - datos["climatologia_mensual"]
```

Calcule:

- promedio de las anomalias
- desviacion estandar de las anomalias
- fecha de la anomalia positiva mas alta
- fecha de la anomalia negativa mas baja

Explique por que las anomalias permiten comparar dias de meses distintos.

## Ejercicio 6. Tendencia anual

Calcule la temperatura media anual:

```python
temperatura_anual = datos.groupby("agno")["valor"].mean()
```

Ajuste una recta entre año y temperatura media anual usando `np.polyfit`.

Responda:

- Cual es la pendiente en grados C/año?
- Cual es la pendiente aproximada en grados C/decada?
- La tendencia calculada representa variabilidad diaria, anual o climatica?

Grafique la temperatura media anual y la recta ajustada.

## Ejercicio 7. Dias calidos y frios

Defina dos umbrales usando percentiles:

```python
umbral_frio = datos["valor"].quantile(0.10)
umbral_calido = datos["valor"].quantile(0.90)
```

Cree una columna `categoria`:

- `"frio"` si `valor <= umbral_frio`
- `"calido"` si `valor >= umbral_calido`
- `"normal"` en los otros casos

Calcule:

- cuantos dias frios hay
- cuantos dias calidos hay
- en que mes ocurren mas dias calidos
- en que mes ocurren mas dias frios

## Ejercicio 8. Promedios por decada

Cree una columna `decada`:

```python
datos["decada"] = (datos["agno"] // 10) * 10
```

Calcule la temperatura media por decada.

Grafique los promedios por decada y comente si se observa una diferencia entre
las primeras y las ultimas decadas disponibles.

## Ejercicio 9. Figuras finales

Genere tres figuras:

1. Serie completa de temperatura media diaria.
2. Climatologia mensual.
3. Temperatura media anual con tendencia lineal.

Cada figura debe incluir:

- titulo
- ejes con unidades
- grilla
- leyenda cuando corresponda

## Pregunta breve

Explique en 4 a 6 lineas una ventaja y una limitacion de usar una serie de una
sola estacion meteorologica para caracterizar cambios de temperatura en una
ciudad.

