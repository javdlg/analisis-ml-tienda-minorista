# Insights de Negocio y Preguntas Clave

Este documento recopila las preguntas de negocio que guían nuestro análisis y los hallazgos (insights) obtenidos de los datos y modelos.

## 1. Predicción de Ventas (Sales Forecasting)
**Pregunta**: ¿Podemos estimar cuánto venderemos en los próximos días para optimizar el stock?
**Insight**:
- El modelo de Random Forest logró capturar la tendencia general de las ventas diarias.
- Se identificaron patrones semanales claros (días de mayor y menor venta).
- **Acción**: Utilizar la predicción diaria para ajustar los pedidos a proveedores con 1 semana de antelación.

## 2. Segmentación de Clientes
**Pregunta**: ¿Quiénes son nuestros mejores clientes y cuáles están en riesgo de irse?
**Hallazgo**:
- Se identificaron 3 clusters claros de clientes:
    - **Cluster 0 (Probablemente "Nuevos/Ocasionales")**: Recencia baja (compraron hace poco), pero Frecuencia y Monto bajos.
    - **Cluster 1 (Probablemente "En Riesgo")**: Recencia alta (hace mucho no compran), Frecuencia y Monto variados.
    - **Cluster 2 (Probablemente "VIP")**: Frecuencia y Monto altos.
- **Acción**:
    - **VIP**: Programa de fidelización.
    - **En Riesgo**: Campaña de reactivación (email marketing con descuento).
    - **Nuevos**: Incentivar segunda compra.
