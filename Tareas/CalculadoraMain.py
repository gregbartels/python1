#CALCULADORA 1.0  
#Se importan las funciones
#Cada resultado se va a guardar en una carpeta llamada RESULTADOS en el folder principal
#Cualquier duda o consulta pueden escribir al desarrollador gregorybadilla@gmail.com
# El codigo puede ser compartido y tambien mejorado por otros, solamente se debe mencionar el creador original en el codigo mejorado.

import os
import operaciones
import math

# Crear la carpeta "resultados" en el directorio principal
if not os.path.exists("resultados"):
    os.mkdir("resultados")

#Se Define la funcion calculadora
def calculadora():
    opcion = 0
#MENU
    while opcion != 7:
        print ('''
        
        
       -----------BIENVENIDO A LA CALCULADORA------------------ 
        
        Que deseas realizar?:\n
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Factorial
              6. Exponente
              7. Salir''')
        opcion = int(input("Ingrese una opción: "))
        print('----------------------')
            #Opciones que se pueden elegir para ingresar mas de 2 numeros
        if opcion in [1,2,3,4,6]:
            a = int(input('Ingrese un número: '))
            b = int(input('Ingrese otro número: '))


        if opcion == 1: #Sumar
            resultado = operaciones.sumar(a, b)

             #Guardar en archivo de texto el resultado.
            archivo = open("resultados/suma.txt", "w")
            archivo.write("El resultado de la suma es: " + str(resultado))
            archivo.close()
            print("\n El resultado de la suma es:", resultado)
           

        elif opcion == 2: #Resta
            resultado = operaciones.restar(a, b)

             #Guardar en archivo de texto el resultado.
            archivo = open("resultados/resta.txt", "w")
            archivo.write("El resultado de la resta es: " + str(resultado))
            archivo.close()
            print("\n El resultado de la resta es:" ,resultado)
            

        elif opcion == 3: #Mutiplicacion
            resultado = operaciones.multiplicar(a, b)
            archivo = open("resultados/multiplicacion.txt", "w")
            archivo.write("El resultado de la multiplicacion es: " + str(resultado))
            archivo.close()
            print("\n El resultado de la multiplicación es: ", resultado)
            

        elif opcion == 4:  #Division
            try:
                resultado = operaciones.dividir(a, b)
                print("\n El resultado de la división es: ", resultado)
            except ZeroDivisionError:
                print("\n Error: el segundo número no puede ser cero")
               
                #Guardar en archivo de texto el resultado.
            archivo = open("resultados/division.txt", "w")
            archivo.write("El resultado de la division es: " + str(resultado))
            archivo.close()
                

        elif opcion == 5:  #Factorizacion 
            print('Factorial:\n')    
            n = int(input('Ingrese un número para calcular su factorial: '))
            resultado = math.factorial(n)

             #Guardar en archivo de texto el resultado.
            archivo = open("resultados/factorizacion.txt", "w")
            archivo.write("El resultado de la factorizacion es:" + str(resultado))
            archivo.close()
            print("\n El factorial de", n, "es: ", resultado)

            

        elif opcion == 6:
            resultado = math.pow(a, b)

             #Guardar en archivo de texto el resultado.
            archivo = open("resultados/exponente.txt", "w")
            archivo.write("El resultado de exponente es: " + str(resultado))
            archivo.close()
            print(a, "\n El Resultado de elevado a ", b, "es igual a ", resultado)
              

        elif opcion == 7:
            #Salida de la Calculadora
            print(" Gracias por usar Calcu-python, Hasta luego!")
            #Si se equivoca, dispara este mensaje:
        else:
            print("\n Opción inválida, revise las opciones e intente de nuevo.")


calculadora()
