#Eliminar repetidos#

numeros = [[1, 2, 3, 3, 2, 4, 6], [3, 3, 3, 3, 3, 3, 3]]   #datos de entrada repetidos#
print("Los numeros Recibidos son 1, 2, 3, 3, 2, 4, 6  y [3, 3, 3, 3, 3, 3, 3 ahora, procedemos a remover los repetidos: ")

for lista in numeros:
    lista_sin_repetidos = list(set(lista))  #crear lista sin repetidos en el codigo#
    print( "Nueva lista sin repetidos:",lista_sin_repetidos) # impresion de valores finales sin repeticiones#
