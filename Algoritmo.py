print("hola como estan")
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(mcd(48, 18)) 