def esPrimo(numero):
    i = 1
    cont = 0
    while i <= numero:
        if numero % i == 0:
          cont += 1
        i += 1

    if cont == 2:
        print("El numero ingresado es primo")
    else:
        print("El numero ingresado no es primo")

numero=int(input("Ingrese un numero: "))
esPrimo(numero)
