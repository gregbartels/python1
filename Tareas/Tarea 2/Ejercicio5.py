#Diccionario que muestre el promedio de notas del estudiante Mike#

sampleDict = {
"class": {
"student": {
"name": "Mike",
"marks": {
"physics": 70,
"history": 80,
"math":90 
},
    }
}
}

print(sampleDict)

##Obtener notas del estudiante
Notas= sampleDict ["name:"],["marks:"]


# Obtenemos las notas del estudiante
Notas = sampleDict["class"]["student"]["marks"]

# Calculamos el promedio de notas
Promedio = sum(Notas.values()) / len(Notas)

# Creamos el diccionario de salida con el nombre y la nota promedio
Promediofinal = {
    "nombre": sampleDict["class"]["student"]["name"],
    "nota": Promedio
}

# Imprimimos el diccionario de salida
print(" El promedio del estudiante:",Promediofinal)