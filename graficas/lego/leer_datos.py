import os
os.system('clear')
import csv


#Función para leer el archivo
def leer_archivo(ruta):
    #Abrir el archivo, con permisos de lectura (r)
    with open(ruta, 'r') as csvfile:
        lector = csv.reader(csvfile, delimiter=',')
        #Poner los datos en la cabecera
        cabecera = next(lector)
        #Crear la lista de los datos
        data = []
        for columna in lector:
            iterable = zip(cabecera, columna)
            compras_diccionario = {key:value for key, value in iterable}
            data.append(compras_diccionario)
    return data


#Entry Point (main)
if __name__ == '__main__':
    data = leer_archivo('lego.csv')
    print(data[0])
    compras = list(map(lambda x : x['Theme'], data))
    print(compras)