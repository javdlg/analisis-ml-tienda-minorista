# Análisis y modelado predictivo — Tienda minorista

Descripción
----------
Proyecto completo que incluye análisis exploratorio (EDA), preparación y modelado predictivo de datos de una tienda minorista. Contiene:
- Carga y conversión de archivos (.xlsx → .csv).
- Análisis de clientes, productos, ventas y detalle de ventas.
- Visualizaciones clave (distribuciones, outliers, series temporales).
- Unión de tablas en un dataframe consolidado (df_completo).
- Feature engineering, selección de variables y matriz de correlación.
- **Segmentación de Clientes**: Clustering K-Means basado en métricas RFM, con perfilado de clientes y análisis de impacto en el negocio.

Estado
------
Completado. El repositorio incluye notebook con EDA, visualizaciones, matriz de correlación y una segmentación de clientes.

Estructura del repositorio
--------------------------
- data/                      — Datos .xlsx y .csv (clientes, productos, ventas, detalle_ventas).
- analisis-ml-tienda-minorista.ipynb                 — Notebook de EDA y modelado.
- models/                    — Modelos entrenados y artefactos (pesos, pipeline, métricas).
- reports/                   — Visualizaciones y reportes de resultados.
- scripts/                   — Scripts auxiliares.
- README.md                  — Este archivo.

Requisitos
----------
Instalar dependencias mínimas:
pip install pandas numpy matplotlib seaborn openpyxl scikit-learn joblib

Uso
---
1. Revisar notebooks en analisis-ml-tienda-minorista.ipynb para reproducir EDA y entrenamiento.
2. Para re-entrenar el modelo de forma independiente:
   ```bash
   python scripts/train_model.py
   ```
3. Todos los resultados y métricas se encuentran en reports/ y models/.

Notas
-----
Para reproducibilidad, conservar los datos originales en data/ y los artefactos en models/.

Resultados de Segmentación
--------------------------
El análisis de segmentación identificó 3 perfiles clave de clientes:
1.  **Leales**: Clientes con frecuencia y recencia moderada/alta. Son la base del negocio.
2.  **Nuevos**: Clientes recientes con pocas compras. Oportunidad de fidelización.
3.  **En Riesgo**: Clientes que compraron hace mucho tiempo. Requieren campañas de reactivación.

**Insights de Negocio:**
*   **Contribución**: Se analizó el % de ingresos que aporta cada segmento (Pareto).
*   **Geografía**: Distribución de segmentos por ciudades clave (ej. Río Cuarto, Córdoba).
*   **Pagos**: Preferencias de pago (Tarjeta vs Transferencia) por tipo de cliente.