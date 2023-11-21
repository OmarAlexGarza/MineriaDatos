import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap

def cargar_datos(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    return df

def procesar_datos(df):

    bins = [0, 50, 60, 70, 80, 90, 100]
    labels = ['50', '51 - 60', '61-70', '71-80', '81-90', '91-100']
    df['grupo_calificacion'] = pd.cut(df['calificacion'], bins=bins, labels=labels, right=False)

    df = df.dropna(subset=['calificacion', 'grupo_calificacion'])

    return df

def dividir_datos(df):
    X = df.index.values.reshape(-1, 1)
    y = df['calificacion']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def entrenar_modelo(X_train, y_train):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    return knn

def evaluar_modelo(modelo, X_test, y_test):
    accuracy = modelo.score(X_test, y_test)
    print(f"Precisión del modelo KNN: {accuracy * 100:.2f}%")

def graficar_dispersion(X_test, y_test, cmap, save_path=None):
    plt.figure(figsize=(15, 6))

    scatter = plt.scatter(X_test, y_test, c=y_test, cmap=cmap, marker='o', alpha=0.7, edgecolors='w')

    plt.title('Gráfica de Dispersión de las Calificaciones')
    plt.xlabel('Índice de Calificaciones')
    plt.ylabel('Calificacion')
    plt.colorbar(scatter, label='Calificacion')

    plt.xticks([])

    if save_path:
        plt.savefig(save_path)
        print(f"La gráfica ha sido guardada en: {save_path}")
    else:
        plt.show()

def main():
    df = cargar_datos('JugadoresFIFAv2.csv')
    df = procesar_datos(df)
    X_train, X_test, y_train, y_test = dividir_datos(df)
    modelo = entrenar_modelo(X_train, y_train)
    evaluar_modelo(modelo, X_test, y_test)
    save_path = 'Graficas/scatter.png'
    cmap = ListedColormap(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'])
    graficar_dispersion(X_test, y_test, cmap, save_path)

if __name__ == "__main__":
    main()