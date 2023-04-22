# 
input("Intercalando palabras")
stringword1= input("Ingrese la primera palabra:")
stringword2= input ("Ingrese la segunda palabra:")

if len(stringword1) != len(stringword2):
 print ("las palabras no tienen la misma cantidad de palabras, intente de nuevo")
else:
 result= ""
 for i in range(len(stringword1)):                 
  result += stringword1[i] + stringword2[i] ## += agrega rl evalor del operador de la recha al operador de la idzquierda, es el que hace el mix por asi decirlo
  print("Las palabras intercaladas serian asi",result)
  
  








