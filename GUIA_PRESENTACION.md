# Guía de Presentación del Proyecto: Análisis y Predicción de Ventas

Este documento detalla el flujo de trabajo realizado durante el proyecto. Úsalo como guion o material de estudio para explicar paso a paso cómo se construyó la solución.

---

## 1. Definición del Problema y Objetivo
**Situación**: Una tienda minorista cuenta con datos históricos de ventas dispersos en varios archivos (Excel) y necesita extraer valor de ellos.
**Objetivo**: Centralizar la información, entender el comportamiento del negocio (EDA) y construir una herramienta predictiva para estimar ventas futuras.

---

## 2. Procesamiento de Datos (Data Wrangling)
Lo primero fue "limpiar la casa". Los datos venían en formato `.xlsx` (Excel), que es bueno para humanos pero lento para procesamiento masivo.
*   **Acción**: Convertimos todos los archivos (`clientes`, `productos`, `ventas`, `detalle_ventas`) a formato `.csv`.
*   **Beneficio**: Lectura mucho más rápida y estandarizada para Python (Pandas).
*   **Unificación**: Creamos un dataset maestro (`df_completo`) uniendo todas las tablas mediante sus claves (`id_cliente`, `id_producto`, `id_venta`). Esto nos permitió cruzar información (ej. saber qué ciudad compra más qué producto).

---

## 3. Análisis Exploratorio de Datos (EDA)
Aquí "interrogamos" a los datos para encontrar patrones.

### Clientes
*   **Hallazgo**: La mayoría de los clientes se concentran en ciudades específicas (ej. Río Cuarto).
*   **Visualización**: Gráfico de barras de distribución por ciudad.

### Productos
*   **Hallazgo**: Identificamos los productos "estrella" por categoría (Alimentos vs. Limpieza).
*   **Dato**: Hay una gran variabilidad en los precios unitarios.

### Ventas
*   **Outliers (Valores Atípicos)**: Detectamos ventas con importes inusualmente altos. Al cruzar con `medio_pago`, vimos que estos montos grandes suelen pagarse con Transferencia o QR, no efectivo.
*   **Estacionalidad**: Analizamos cómo varían las ventas a lo largo de los meses y días de la semana.

---

## 4. Ingeniería de Características (Feature Engineering)
Para que un modelo aprenda, necesitamos darle "pistas" (features) más allá de los datos crudos.
*   **Variables de Tiempo**: Descompusimos la fecha en `día_semana`, `día_mes` y `mes`.
*   **Variables de Negocio**:
    *   `antiguedad_cliente`: ¿Los clientes viejos compran más? (Matriz de correlación mostró relación débil).
    *   `gasto_promedio`: Útil para describir, pero peligroso para predecir (riesgo de data leakage si no se maneja bien).

---

## 5. Modelado Predictivo: Sales Forecasting
El plato fuerte del proyecto. Decidimos predecir **cuánto se venderá cada día**.

### Preparación
*   Agrupamos las ventas por día (`resample('D')`).
*   Creamos variables de "rezago" (Lags):
    *   `lag_1`: ¿Cuánto se vendió ayer?
    *   `lag_7`: ¿Cuánto se vendió hace exactamente una semana? (Captura patrones semanales).
    *   `rolling_mean_7`: Promedio móvil de la última semana (suaviza el ruido).

### El Modelo: Random Forest Regressor
*   **Por qué este modelo**: Es robusto, maneja bien relaciones no lineales y no requiere tanto pre-procesamiento como una regresión lineal o redes neuronales complejas.
*   **Entrenamiento**: Usamos el 80% de los días más antiguos para entrenar y el 20% más reciente para probar (Split temporal, no aleatorio, para respetar el orden del tiempo).

### Resultados
*   Evaluamos con **MAE** (Error Absoluto Medio) y **RMSE**.
*   **Gráfico**: La curva de predicción sigue bastante bien la tendencia real de las ventas en el set de prueba, validando la utilidad del modelo.

---

## 6. Segmentación de Clientes (Clustering)
Para entender mejor *quién* nos compra, aplicamos una técnica de agrupamiento (K-Means).

### Metodología RFM
Calculamos tres métricas clave para cada cliente:
*   **Recency (Recencia)**: ¿Hace cuánto fue su última compra?
*   **Frequency (Frecuencia)**: ¿Cuántas veces compró?
*   **Monetary (Monto)**: ¿Cuánto gastó en total?

### Resultados
El algoritmo encontró 3 grupos naturales de clientes:
1.  **Nuevos/Ocasionales**: Compraron poco y hace poco tiempo.
2.  **En Riesgo**: Compraron hace mucho tiempo.
3.  **VIP**: Compran frecuentemente y gastan mucho.

**Acción de Negocio**: Esto nos permite diseñar estrategias diferentes (fidelizar a los VIP, reactivar a los de Riesgo).

---

## 7. Conclusión y Siguientes Pasos
El proyecto logró transformar datos crudos en conocimiento accionable.
*   **Valor para el negocio**: Ahora se puede estimar la caja diaria con antelación y personalizar el trato con los clientes.
*   **Futuro**: Se podrían probar modelos más complejos (Prophet, XGBoost) o agregar datos externos (clima, feriados) para mejorar la precisión.
