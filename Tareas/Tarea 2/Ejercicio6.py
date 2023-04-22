##
#Definir la lista de datos
inputList = [1, 2, 3, 3, 2, 4, 6]
print("Los numeros son 1, 2, 3, 3, 2, 4, 6 ahora, procedemos a remover los repetidos: ")
#Crear una lista para almacenar los datos sin repetir
listaunica= []

 #Iteramos sobre la lista de entrada
for numero in inputList:
    # Si el elemento no está en la lista temporal, lo agregamos
    if numero not in listaunica:
        listaunica.append(numero)

# Imprimimos la lista de elementos únicos
print("Numeros sin repetir:",listaunica)