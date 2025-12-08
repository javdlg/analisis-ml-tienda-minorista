import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# Configuración de visualización
sns.set(style="whitegrid")

# Cargar datos
print("Cargando datos...")
df_completo = pd.read_csv('../data/df_completo.csv')
df_completo['fecha'] = pd.to_datetime(df_completo['fecha'])

# --- 1. Cálculo de RFM ---
print("Calculando métricas RFM...")
# Fecha de referencia = día siguiente a la última venta registrada
snapshot_date = df_completo['fecha'].max() + pd.Timedelta(days=1)

# Agrupamos por cliente
rfm = df_completo.groupby('id_cliente').agg({
    'fecha': lambda x: (snapshot_date - x.max()).days, # Recency
    'id_venta': 'nunique',                             # Frequency
    'importe': 'sum'                                   # Monetary
}).reset_index()

rfm.rename(columns={
    'fecha': 'Recency',
    'id_venta': 'Frequency',
    'importe': 'Monetary'
}, inplace=True)

print(rfm.head())

# --- 2. Preprocesamiento ---
print("Preprocesando datos para Clustering...")
# Log transformation para reducir el sesgo (skewness)
rfm_log = rfm[['Recency', 'Frequency', 'Monetary']].apply(np.log1p)

# Estandarización
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

# --- 3. K-Means Clustering ---
print("Ejecutando K-Means...")
# Usaremos K=3 para simplificar la interpretación inicial (ej. VIP, Regulares, En Riesgo)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(rfm_scaled)

rfm['Cluster'] = kmeans.labels_

# Análisis de los clusters
cluster_summary = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'id_cliente': 'count'
}).reset_index()

print("\n--- Resumen de Clusters ---")
print(cluster_summary)

# --- 4. Visualización ---
print("Generando visualizaciones...")
if not os.path.exists('../reports'):
    os.makedirs('../reports')

# Boxplots para interpretar clusters
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.boxplot(x='Cluster', y='Recency', data=rfm, ax=axes[0])
axes[0].set_title('Recency (Días desde última compra)')

sns.boxplot(x='Cluster', y='Frequency', data=rfm, ax=axes[1])
axes[1].set_title('Frequency (Cantidad de compras)')

sns.boxplot(x='Cluster', y='Monetary', data=rfm, ax=axes[2])
axes[2].set_title('Monetary (Gasto total)')

plt.suptitle('Perfil de Clientes por Cluster', fontsize=16)
plt.savefig('../reports/customer_segments_profile.png')
print("Gráfico de perfiles guardado en reports/customer_segments_profile.png")

# Scatter Plot 3D (Opcional, proyectado en 2D con hue)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster', palette='viridis', s=100, alpha=0.8)
plt.title('Segmentación de Clientes: Recency vs Monetary')
plt.savefig('../reports/customer_segments_scatter.png')
print("Gráfico de dispersión guardado en reports/customer_segments_scatter.png")

# Guardar resultados
rfm.to_csv('../data/clientes_rfm_clusters.csv', index=False)
print("Datos de segmentación guardados en data/clientes_rfm_clusters.csv")
