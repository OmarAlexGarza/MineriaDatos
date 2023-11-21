import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

def cargar_datos(ruta_archivo, nrows=None):
    df = pd.read_csv(ruta_archivo, nrows=nrows)
    return df


def aplicar_kmeans(df, num_clusters=3):

    df = df.dropna(subset=['velocidad'])
    X = df[['velocidad']]
    kmeans = KMeans(n_clusters=num_clusters, random_state=3, n_init=10)
    kmeans.fit(X)
    df = df.copy()
    df.loc[:, 'Cluster'] = kmeans.labels_

    return df, kmeans.cluster_centers_

def asignar_colores_por_cluster(df):
    return df['Cluster'].tolist()

def graficar_dispersion(df, colores, save_path=None):
    plt.figure(figsize=(15, 6))

    scatter = plt.scatter(df.index, df['velocidad'], c=colores, cmap='viridis', marker='o', alpha=0.7, edgecolors='w')

    plt.title('Gráfica de Dispersión de la Velocidad y Agrupación con K-Means')
    plt.xlabel('')
    plt.ylabel('Velocidad')
    plt.colorbar(scatter, label='Cluster')

    plt.xticks([])

    if save_path:
        plt.savefig(save_path)
        print(f"La gráfica ha sido guardada en: {save_path}")
    else:
        plt.show()

def visualizar_centros_de_masa(centros_de_masa, cmap, save_path=None):
    plt.figure(figsize=(10, 4))
    plt.scatter(np.random.rand(len(centros_de_masa)), centros_de_masa, c=range(len(centros_de_masa)), cmap=cmap, marker='x', s=100)
    plt.title('Centros de Masa de los Clusters')
    plt.xlabel('Aleatorio')

    if save_path:
        plt.savefig(save_path)
        print(f"La gráfica ha sido guardada en: {save_path}")
    else:
        plt.show()

def main():
    df = cargar_datos('JugadoresFIFAv2.csv')
    df, centros_de_masa = aplicar_kmeans(df)
    colores = asignar_colores_por_cluster(df)
    graficar_dispersion(df, colores, save_path='Graficas/K-Means.png')
    visualizar_centros_de_masa(centros_de_masa, 'viridis', save_path='Graficas/centros_de_masa.png')

if __name__ == "__main__":
    main()