# Análisis y modelado predictivo — Tienda minorista

Descripción
----------
Proyecto completo que incluye análisis exploratorio (EDA), preparación y modelado predictivo de datos de una tienda minorista. Contiene:
- Carga y conversión de archivos (.xlsx → .csv).
- Análisis de clientes, productos, ventas y detalle de ventas.
- Visualizaciones clave (distribuciones, outliers, series temporales).
- Unión de tablas en un dataframe consolidado (df_completo).
- Feature engineering, selección de variables y matriz de correlación.
- Por aplicar (proximamente):
- Modelado predictivo, evaluación y artefactos de modelo (modelos entrenados, métricas y scripts de inferencia).

Estado
------
En desarrollo. El repositorio incluye notebook con EDA, visualizaciones, union de tablas en dataframe principal y matriz de correlacion. Proximamente modelado.

Estructura del repositorio
--------------------------
- data/                      — Datos .xlsx y .csv (clientes, productos, ventas, detalle_ventas).
- notebooks/                 — Notebooks de EDA y modelado.
- models/                    — Modelos entrenados y artefactos (pesos, pipeline, métricas). # proximamente
- reports/                   — Visualizaciones y reportes de resultados. # proximamente
- README.md                  — Este archivo.

Requisitos
----------
Instalar dependencias mínimas:
pip install pandas numpy matplotlib seaborn openpyxl scikit-learn joblib

Uso
---
1. Revisar notebooks en notebooks/ para reproducir EDA y entrenamiento.
2. Para inferencia rápida: cargar el pipeline guardado en models/ y usar el script de inferencia en scripts/ (si existe).
3. Todos los resultados y métricas se encuentran en reports/ y models/.

Notas
-----
Para reproducibilidad, conservar los datos originales en data/ y los artefactos en models/.