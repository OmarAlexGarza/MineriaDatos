import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os 

df = pd.read_csv('JugadoresFIFAv2.csv')

output_dir = 'Graficas'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

X = df[['calificacion']]
y = df['potencial']

modelo_regresion = LinearRegression()
modelo_regresion.fit(X, y)

predicciones = modelo_regresion.predict(X)

plt.scatter(X, y, label='Calificacion vs Potencial')
plt.plot(X, predicciones, color='red', label='Regresión lineal')
plt.xlabel('Calificacion')
plt.ylabel('Potencial')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Regresion Lineal Calificacion vs Potencial.png'))
plt.show()

