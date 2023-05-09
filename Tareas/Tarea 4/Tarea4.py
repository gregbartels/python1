
#Ejercicio 1

#Función que cuente e imprima en pantalla todos los números,
#letras y caracteres especiales presentes en una string
'''
def contar_caracteres(cadena):
    letras = 0
    numeros = 0
    especiales = 0

    # Recorrer la cadena de texto
    for caracter in cadena:
        # Si el carácter es una letra, aumentar el contador de letras
        if caracter.isalpha():
            letras += 1
        # Si el carácter es un número, aumentar el contador de números
        elif caracter.isdigit():
            numeros += 1
        # Si el carácter no es una letra ni un número, aumentar el contador de caracteres especiales
        else:
            especiales += 1
 
    # Imprimir los resultados
    print("Letras =", letras)
    print("Números =", numeros)
    print("Caracteres especiales =", especiales)

# Pedir al usuario que ingrese la cadena a analizar
cadena = input("Ingrese un texto: ")

# Llamar a la función con la cadena ingresada por el usuario
contar_caracteres(cadena)
'''

#Ejercicio 2

# función que cuente todas las apariciones de cada caracter en una
#string; esta string debe recibirse como parámetro. El resultado debe ser un
#diccionario y debe ser impreso en pantalla.

'''
def contar_caracteres(cadena):
      # Creamos un diccionario vacío para ir guardando la cantidad de apariciones de cada caracter
    diccionario = {}
    # Recorremos la cadena de texto y contamos las apariciones de cada caracter
    for caracter in cadena:
        if caracter in diccionario:
            #Contamos cada uno de los caracteres
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    print(diccionario)

# Pedir al usuario una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Llamar a la función con la cadena de texto como parámetro
contar_caracteres(cadena)

'''

#Ejercicio 3 función que elimine todas las apariciones de un elemento en una
#lista.

'''

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

# Llamamos a la función con la lista y el elemento a eliminar
resultado = eliminar_elemento(mi_lista, elem_eliminar)

# Imprimimos el resultado
print (resultado)

'''

#En este codigo, estamos creando una lista llamada mi_lista y luego llamando a la función eliminar_elemento() pasándole la lista y el elemento a eliminar. En este caso, estamos eliminando todas las apariciones del número 2 en la lista.

#Después de llamar a la función, guardamos el resultado en la variable resultado y luego lo imprimimos. En este ejemplo, la lista resultante después de eliminar todas las apariciones del número 2 es [1, 3, 4, 5], por lo que se imprimirá esa lista.

#Puedes cambiar los valores de la lista y el elemento a eliminar según tus necesidades para probar diferentes escenarios.



#Ejercicio 4 Función que reciba una secuencia de números separados por coma
#por parte del usuario e imprima una lista y una tupla que contengan dichos
#valores. El usuario debe ingresar un único input con los valores separados
#por comas.

'''
def lista_y_tupla(input_usuario):
    numeros = input_usuario.split(',')
    numeros = [int(n) for n in numeros]
    mi_lista = list(numeros)
    mi_tupla = tuple(numeros)
    print("Lista: ", mi_lista)
    print("Tupla: ", mi_tupla)

input_usuario = input("Ingrese una secuencia de números separados por coma: ")
lista_y_tupla(input_usuario)

'''


#-------------------------------------- Pruebas realizadas ------------------------------------------------------------##



#Pruebas Ejercicio 1

#Ingrese un texto: a@rrozconl3che
#Letras = 12
#Números = 1
#Caracteres especiales = 1


#Ingrese un  texto: @arbold3arros
#Letras = 11
#Números = 1
#Caracteres especiales = 1


#Ingrese un texto: f1sica
#Letras = 5
#Números = 1
#Caracteres especiales = 0


#Ingrese un texto: c@art@go
#Letras = 6
#Números = 0
#Caracteres especiales = 2


#Pruebas Ejercicio 2

#Ingresa una cadena de texto: papaya
#{'p': 2, 'a': 3, 'y': 1}


#Ingresa una cadena de texto: arroz
#{'a': 1, 'r': 2, 'o': 1, 'z': 1}


#Ingresa una cadena de texto: masterclass
#{'m': 1, 'a': 2, 's': 3, 't': 1, 'e': 1, 'r': 1, 'c': 1, 'l': 1}

#Ingresa una cadena de texto: radioaficion
#{'r': 1, 'a': 2, 'd': 1, 'i': 3, 'o': 2, 'f': 1, 'c': 1, 'n': 1}

#
#Pruebas Ejercicio 3


#Ingresa una lista de al menos 5 elementos separados por comas: arroz,frijoles,perro,paco,lola
#Ingresa el elemento que deseas eliminar: lola
#['arroz', 'frijoles', 'perro', 'paco']


#Ingresa una lista de al menos 5 elementos separados por comas: 1,4,5,8,9,6
#Ingresa el elemento que deseas eliminar: 5
#['1', '4', '8', '9', '6']


#Ingresa una lista de al menos 5 elementos separados por comas: 1,4,5,6,8,9,2,4
#Ingresa el elemento que deseas eliminar: 4
#['1', '5', '6', '8', '9', '2']


#Ingresa una lista de al menos 5 elementos separados por comas: 1,4,5,6,8,9,2,4
#Ingresa el elemento que deseas eliminar: 4
#['1', '5', '6', '8', '9', '2']

#  Pruebas Ejercicio 4

#Ingrese una secuencia de números separados por coma: 1,2,3,4,5,6,9,8,7,9
#Lista:  [1, 2, 3, 4, 5, 6, 9, 8, 7, 9]
#Tupla:  (1, 2, 3, 4, 5, 6, 9, 8, 7, 9)

#Ingrese una secuencia de números separados por coma: 1,2,3,4,5,6,9,8,7,9
#Lista:  [1, 2, 3, 4, 5, 6, 9, 8, 7, 9]
#Tupla:  (1, 2, 3, 4, 5, 6, 9, 8, 7, 9)

#Ingrese una secuencia de números separados por coma: 4,4,4,4,4
#Lista:  [4, 4, 4, 4, 4]
#Tupla:  (4, 4, 4, 4, 4)

#Ingrese una secuencia de números separados por coma: 8,8,8,8
#Lista:  [8, 8, 8, 8]
#Tupla:  (8, 8, 8, 8)