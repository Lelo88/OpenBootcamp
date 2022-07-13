lista = input("Ingrese la cantidad de países que desee: ")
paises = [pais for pais in lista.split(',')]
print(",".join(sorted(list(set(paises)))))


