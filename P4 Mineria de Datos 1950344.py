import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os  

df = pd.read_csv('JugadoresFIFAv2.csv')
output_dir = 'Graficas'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def grafica_piernahabil(df):
    conteo_piernahabil = df['piernahabil'].value_counts()
    plt.bar(conteo_piernahabil.index, conteo_piernahabil.values)
    plt.xlabel('Pierna Habil')
    plt.ylabel('Cantidad de jugadores')
    plt.title('Gráfica de pierna Habil por Jugadores')
    plt.savefig(os.path.join(output_dir, 'grafica_piernahabil.png'))
    plt.show()

def grafica_histograma_edad(df):
    plt.figure(figsize=(10, 6)) 
    plt.hist(df['edad'], bins=20, edgecolor='k', alpha=0.7)
    plt.xlabel('Edad de jugadores')
    plt.ylabel('Cantidad de jugadores')
    plt.title('Histograma de Edades de jugadores')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'grafica_histograma_edad.png'))
    plt.show()

def grafica_distribucion_edades_por_posicion(df):
   plt.figure(figsize=(12, 8))
   sns.boxplot(x='posicion', y='edad', data=df, palette='viridis')
   plt.title('Distribución de Edades por Posición de Juego en Fútbol')
   plt.xlabel('Posición de Juego')
   plt.ylabel('Edad')
   plt.tight_layout()
   plt.xticks(rotation=90, ha='right')
   plt.savefig(os.path.join(output_dir, 'grafica_distribucion_edades_por_posicion.png'))
   plt.show()

def grafica_puntos_jugadoresporpais(df):

  jugadores_por_pais = df['nacionalidad'].value_counts().head(30)

  plt.figure(figsize=(12, 8))
  plt.scatter(jugadores_por_pais.index, jugadores_por_pais, marker='o', color='blue')
  plt.title('Cantidad de Jugadores por País')
  plt.xlabel('País')
  plt.ylabel('Cantidad de Jugadores')
  plt.xticks(rotation=90, ha='right')
  plt.savefig(os.path.join(output_dir, 'grafica_puntos_Jugadoresporpais.png'))

  plt.show()

grafica_piernahabil(df)
grafica_histograma_edad(df)
grafica_distribucion_edades_por_posicion(df)
grafica_puntos_jugadoresporpais(df)
