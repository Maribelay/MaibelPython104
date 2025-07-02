#leer extensiones

import pandas as pd
import os
import shutil

cantidad = input("ingrese la cantidad de archivos excel que deseas leer ? : ")
cantidad = int(cantidad)

archivo = input("ingrese el nombre completo del archivo: ")
contador =1

extension= os.path.splitext(archivo)[1]
print (extension)

# Ruta del archivo Excel

if not os.path.exists("leidos"):
    os.makedirs("leidos")