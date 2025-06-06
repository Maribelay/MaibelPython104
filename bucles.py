print("Ejemplo de bucles")
nombres = ["Ana", "Luis", "Carlos"]
edades = [23, 34, 19]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")