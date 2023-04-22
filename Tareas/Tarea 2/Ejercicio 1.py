numero=int(input("numero:"))
factorial=1  ##aqui inicia con el valor factorial de 1

if numero == 0:
    print("El número 0 no es un número factorial")
elif numero < 0:
   print('No es numero factorial')
else:
 for i in range(1,numero+1):
    factorial=factorial*i
    print(" Los numeros Factoriales son:",factorial)
    


