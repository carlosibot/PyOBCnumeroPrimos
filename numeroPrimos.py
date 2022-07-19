numero = (int(input("Introduce un numero: ")))
def numeroPrimo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True
if (numeroPrimo(numero)) == True:
    print("Es un numero primo")
else:
    print("No es un numero primo")


