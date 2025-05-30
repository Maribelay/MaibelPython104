print("Ejemplos de condicionales")
valores = [4, 6, 8, 10]
if all(x % 2 == 0 for x in valores):
    print ("Todos son pares")
elif any (x % 2 == 0 for x in valores): 
    print ("Algunos son pares")
else:
    print("Ninguno es par")