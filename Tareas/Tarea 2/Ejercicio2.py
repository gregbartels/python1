numero=int(input("Bienvenido, ingresa un valor y te dire el patron que debes seguir para alcanzar este numero:"))
if numero < 1:
    print("El numero debe ser mayor al O")

else:
    for i in range(1, numero+1):
        if i == 1:
            print(i)
        else:
            for segundo in range(1, i+1):
                print(segundo, end=" ")
            print()