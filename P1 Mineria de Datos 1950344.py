import requests

url = "https://query.data.world/s/wifkbzyh2ml6osedekekn6cdbcapgl?dws=00000"

nombre = "JugadoresFIFA.csv"

respuesta = requests.get(url)

if respuesta.status_code == 200:

    with open(nombre, 'wb') as archivo:
        archivo.write(respuesta.content)
    print("Descarga exitosa")
else:
    print("Error al descargar el archivo:", respuesta.status_code)