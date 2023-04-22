# numeros aleatorios y aplicar el cubico#

import random
aleatorio= [random.randint(0,6) for i in range(5)]
print("Estos son tus numeros aleatorios:", aleatorio)   #imprime una lista de 5 numeros aleatrios.
numerocubico = [numerocubico **3 for numerocubico in aleatorio]
print("numeros elevados al cubo:", numerocubico)