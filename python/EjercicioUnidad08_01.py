archivo = open('miArchivo01.txt','w')
archivo.write("Esta es la primer linea de archivo\n")
archivo.close()

archivo = open('miArchivo01.txt','r+')
archivo.readline()
archivo.write('Esta es la segunda linea del archivo creado')

archivo.seek(0)
print(archivo.read())
archivo.close()