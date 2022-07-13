from functools import reduce

def listaImpares(listado):
    resultado = list(filter(lambda a: a % 2),listado)
    print(resultado)
    resultado = reduce(lambda a,b: a + b, resultado)
    print (resultado)


lista = list(range(100))
listaImpares(lista)