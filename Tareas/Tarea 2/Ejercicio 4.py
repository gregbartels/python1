# numeros aleatorios y aplicar el cubico#

import random  #Usamos el modulo random para que nos  devuelva numeros aleatorios.#
aleatorio= [random.randint(0,6) for i in range(5)]
print("Estos son tus numeros aleatorios:", aleatorio)   #imprime una lista de 5 numeros aleatorios.#
numerocubico = [numerocubico **3 for numerocubico in aleatorio] #sacamos el cubo de los numeros aleatorios#
print("numeros elevados al cubo:", numerocubico)  # Se imprime el resultado final#