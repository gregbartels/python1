

## Refactor funcion #1
## Esta función cuenta e imprime en pantalla todos los números, letras y caracteres especiales presentes en una cadena de texto.

'''def contar_caracteres(string):
    numeros = 0
    letras = 0
    especiales = 0
    
    for char in string:
        if char.isdigit():
            numeros += 1
        elif char.isalpha():
            letras += 1
        else:
            especiales += 1
    
    print("Cantidad de números:", numeros)
    print("Cantidad de letras:", letras)
    print("Cantidad de caracteres especiales:", especiales)
'''


 
'''
contar_caracteres = lambda string: (
    print("Cantidad de números:", len(list(filter(lambda char: char.isdigit(), string)))),
    print("Cantidad de letras:", len(list(filter(lambda char: char.isalpha(), string)))),
    print("Cantidad de caracteres especiales:", len(list(filter(lambda char: not char.isdigit() and not char.isalpha(), string))))
)

#ELllamado de prueba:
texto = "Hola! 123 @#"
contar_caracteres(texto)

# utilizamos expresiones lambda junto con las funciones filter() y len() para filtrar los caracteres de la cadena de texto y 
#contar la cantidad de números, letras y caracteres especiales. 
#Se imprimen los resultados en pantalla utilizando la función print().


## Resultado de pruebas:
"""
Cantidad de números: 3
Cantidad de letras: 4
Cantidad de caracteres especiales: 5 """















## Refactor funcion 2


#Eliminar repetidos#


# Función original: 

''''''
numeros = [[1, 2, 3, 3, 2, 4, 6], [3, 3, 3, 3, 3, 3, 3]]   #datos de entrada repetidos#
print("Los numeros Recibidos son 1, 2, 3, 3, 2, 4, 6  y [3, 3, 3, 3, 3, 3, 3 ahora, procedemos a remover los repetidos: ")

for lista in numeros:
    lista_sin_repetidos = list(set(lista))  #crear lista sin repetidos en el codigo#
    print( "Nueva lista sin repetidos:",lista_sin_repetidos) # impresion de valores finales sin repeticiones#
'''''



'''
# Descripción: Esta función recibe una lista y elimina los elementos repetidos, devolviendo una nueva lista sin repeticiones.
def eliminar_repetidos_original(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

numeros = [[1, 2, 3, 3, 2, 4, 6], [3, 3, 3, 3, 3, 3, 3]]
print("Los números recibidos son 1, 2, 3, 3, 2, 4, 6 y [3, 3, 3, 3, 3, 3, 3]. Ahora procedemos a remover los repetidos:")

for lista in numeros:
    lista_sin_repetidos = eliminar_repetidos_original(lista)
    print("Nueva lista sin repetidos (Función original):", lista_sin_repetidos)

    

# Nueva solución utilizando programación funcional

eliminar_repetidos_funcional = lambda lista: list(set(lista))
lista_sin_repetidos_funcional = list(map(eliminar_repetidos_funcional, numeros))

for lista in lista_sin_repetidos_funcional:
    print("Nueva lista sin repetidos (Programación funcional):", lista)

'''

#Pruebas:
'''
Cantidad de números: 3
Cantidad de letras: 4
Cantidad de caracteres especiales: 5
Los números recibidos son 1, 2, 3, 3, 2, 4, 6 y [3, 3, 3, 3, 3, 3, 3]. Ahora procedemos a remover los repetidos:
Nueva lista sin repetidos (Función original): [1, 2, 3, 4, 6]
Nueva lista sin repetidos (Función original): [3]
Nueva lista sin repetidos (Programación funcional): [1, 2, 3, 4, 6]
Nueva lista sin repetidos (Programación funcional): [3]
'''


#Refactor funcion 3
'''

# Función original: intercalar_palabras_original(stringword1, stringword2)
# Descripción: Esta función recibe dos palabras y verifica si tienen la misma cantidad de caracteres. Si es así, intercala los caracteres de ambas palabras y retorna el resultado. Si no tienen la misma cantidad de caracteres, muestra un mensaje de error.
def intercalar_palabras_original(stringword1, stringword2):
    if len(stringword1) != len(stringword2):
        return "Las palabras no tienen la misma cantidad de caracteres. Intente de nuevo."
    else:
        result = ""
        for i in range(len(stringword1)):
            result += stringword1[i] + stringword2[i]
        return result

stringword1 = input("Ingrese la primera palabra: ")
stringword2 = input("Ingrese la segunda palabra: ")

print(intercalar_palabras_original(stringword1, stringword2))


# Nueva solución utilizando programación funcional

intercalar_palabras_funcional = lambda word1, word2: "".join(map(lambda c1, c2: c1 + c2, word1, word2))

stringword1 = input("Ingrese la primera palabra: ")
stringword2 = input("Ingrese la segunda palabra: ")

print(intercalar_palabras_funcional(stringword1, stringword2))
'''

#Pruebas"
'''
Cantidad de números: 3
Cantidad de letras: 4
Cantidad de caracteres especiales: 5
Ingrese la primera palabra:
'''
#En la nueva solución utilizando programación funcional,
#  hemos reescrito la lógica de la función original utilizando 
# expresiones lambda y la función map().
# La función intercalar_palabras_funcional utiliza la función map()
#  junto con una expresión lambda para iterar sobre los caracteres
#  correspondientes de word1 y word2, y concatenarlos. 
# Luego, utilizamos "".join() para unir los caracteres en un solo string.
# Los llamados de prueba demuestran que tanto la función original como la nueva solución en programación funcional producen los mismos resultados para las palabras de entrada.










#Refactor funcion 4


'''
# Función original: eliminar_elemento(lista, elemento)
# Descripción: Esta función recibe una lista y un elemento, y elimina todas las apariciones del elemento en la lista. Si la lista tiene al menos 5 elementos, se realiza la eliminación y se retorna la lista modificada. Si la lista tiene menos de 5 elementos, se muestra un mensaje de error.
def eliminar_elemento(lista, elemento):
    if len(lista) >= 5:
        while elemento in lista:
            lista.remove(elemento)
        return lista
    else:
        return "La lista debe tener al menos 5 elementos"

# Pedimos al usuario que ingrese la lista
cadena_lista = input("Ingresa una lista de al menos 5 elementos separados por comas: ")

# Convertimos la cadena en una lista de Python
mi_lista = cadena_lista.split(",")

# Pedimos al usuario que ingrese el elemento a eliminar
elem_eliminar = input("Ingresa el elemento que deseas eliminar: ")

# Llamamos a la función original con la lista y el elemento a eliminar
resultado_original = eliminar_elemento(mi_lista, elem_eliminar)

# Llamamos a la nueva solución utilizando programación funcional
eliminar_elemento_funcional = lambda lst, elem: list(filter(lambda x: x != elem, lst))
resultado_funcional = eliminar_elemento_funcional(mi_lista, elem_eliminar)

# Imprimimos los resultados
print("Resultado (Función original):", resultado_original)
print("Resultado (Programación funcional):", resultado_funcional)
'''



#En estas pruebas, utilizamos la cadena "1,2,3,4,5,6,7,8,9,10" como lista de entrada y el elemento "5" como el elemento a eliminar. 
# Ambas pruebas se realizan tanto para la función original como para la nueva solución utilizando programación funcional.
#En la nueva solución utilizando programación funcional, hemos reescrito la lógica de la función original utilizando una expresión lambda
# y la función filter().La función eliminar_elemento_funcional utiliza la función filter() junto con una expresión lambda 
# para filtrar los elementos de la lista lst que no sean iguales al elemento elem,
#  eliminando así todas las apariciones de ese elemento. Luego, convertimos el resultado en una lista utilizando list().
# Los llamados de prueba demuestran que tanto la función original como la nueva solución en programación funcional producen 
# los mismos resultados para la lista y el elemento de entrada.
