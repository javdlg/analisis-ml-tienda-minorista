import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
import os

# Cargar datos
df_completo = pd.read_csv('data/df_completo.csv')
df_completo['fecha'] = pd.to_datetime(df_completo['fecha'])

# Preparación de datos
df_daily = df_completo.groupby('fecha')['importe'].sum().reset_index()
df_daily = df_daily.set_index('fecha').asfreq('D').fillna(0).reset_index()

# Feature Engineering
df_daily['day_of_week'] = df_daily['fecha'].dt.dayofweek
df_daily['day_of_month'] = df_daily['fecha'].dt.day
df_daily['month'] = df_daily['fecha'].dt.month
df_daily['lag_1'] = df_daily['importe'].shift(1)
df_daily['lag_7'] = df_daily['importe'].shift(7)
df_daily['rolling_mean_7'] = df_daily['importe'].rolling(window=7).mean()

# Eliminamos filas con NaN generados por los lags
df_daily = df_daily.dropna()

print("Datos preparados para modelado:")
print(df_daily.head())

# Split Train/Test
train_size = int(len(df_daily) * 0.8)
train, test = df_daily.iloc[:train_size], df_daily.iloc[train_size:]

features = ['day_of_week', 'day_of_month', 'month', 'lag_1', 'lag_7', 'rolling_mean_7']
target = 'importe'

X_train = train[features]
y_train = train[target]
X_test = test[features]
y_test = test[target]

print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

# Entrenamiento del modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicción y Evaluación
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f'MAE: {mae:.2f}')
print(f'RMSE: {rmse:.2f}')

# Guardar el modelo entrenado
if not os.path.exists('models'):
    os.makedirs('models')

model_path = 'models/sales_forecasting_rf.pkl'
joblib.dump(model, model_path)
print(f"Modelo guardado en {model_path}")

# Generar gráfico (opcional, para verificar que no falle)
plt.figure(figsize=(12, 6))
plt.plot(train['fecha'], y_train, label='Train')
plt.plot(test['fecha'], y_test, label='Test')
plt.plot(test['fecha'], y_pred, label='Predicted', linestyle='--')
plt.legend()
plt.title('Sales Forecasting: Actual vs Predicted')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.savefig('reports/sales_forecast.png')
print("Gráfico guardado en reports/sales_forecast.png")
