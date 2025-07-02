
import pandas as pd
import os
import shutil

#cantidad = input("ingrese la cantidad de archivos excel que deseas leer ? : ")
##cantidad = int(cantidad)

#archivo = input("ingrese el nombre completo del archivo: ")
#contador = 1

nombresArchivos = os.listdir("modelosgenerados")

lista_archivos = []

if not os.path.exists("leidos2"):
    os.makedirs("leidos2")

for nombre in nombresArchivos:

    extension = os.path.splitext(nombre)[1]
    
    print("=============== Nombre del Archivo=================")
    print(nombre)
    print(extension)
    ruta_archivo = ""
    ruta_archivo = os.path.join("modelosgenerados",nombre)

    pd.set_option('display.max_rows', None)
         # intentar leer con autodetección del separador
    if (extension == ".csv"):
        df = pd.read_csv(ruta_archivo, sep=None, engine='python', encoding='windows-1252', on_bad_lines='skip')

    if (extension == ".xlsx" or extension == ".xls"):
        df = pd.read_excel(ruta_archivo, sheet_name ="Sheet1")

        # Mostrar las primeras filas del archivo
    print(df.head())
    #print(df)
    lista = df.to_dict(orient = 'records') # Lista de filas como diccionarios
    lista_archivos.append({
           "nombre" : nombre,
           "datos" :  lista
         })

    # Mover el archivo a la carpeta "leidos"
    shutil.move(ruta_archivo, os.path.join("leidos2", nombre))
    print(f" Archivo {ruta_archivo} movido a 'leidos2'")
    break



for archivo in lista_archivos:
    print(f"📄 Analizando archivo : {archivo ['nombre']}")
    for fila in archivo ["datos"]:
        # Aplicar filtros o logicas aqui, por ejemplo:
        if 'nombre' in fila and 'No disponible' in fila ['TELEFONO'].lower():
            print (f"🔹 Coincidencia: {fila}")



    


# Ruta del archivo Excel



'''
while contador <= cantidad:
    #archivo_excel = archivo + "_" +str(contador)+".csv"  
    #archivo = archivo +".csv" 

    if os.path.exists(archivo):

        # Leer la hoja específica (puedes cambiar el nombre de la hoja)
        #df = pd.read_excel(archivo_excel, sheet_name="Padron-Instituciones")
        #df = pd.read_csv(archivo_excel)

        try:
            # intentar leer con autodetección del separador

            if (extension == ".csv"):
                df = pd.read_csv(archivo, sep=None, engine='python', encoding='windows-1252', on_bad_lines='skip')

            if (extension == ".xlsx" or extension == ".xls"):
                df = pd.read_excel(archivo, sheet_name="Sheet1")

            # Mostrar las primeras filas del archivo
            print(df.head())
            # Mover el archivo a la carpeta "leidos"
            shutil.move(archivo, os.path.join("leidos", archivo))
            print(f" Archivo {archivo} movido a 'leidos'")

        except Exception as e:
            print(f"X Error al leer el archivo {archivo}:{e}")
    else:
        print(f"El {archivo} no existe")

    contador +=1

print ("=====================Fin de lectura================0")

'''

            