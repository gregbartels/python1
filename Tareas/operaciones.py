#En este codigo se declaran las variables aritmeticas
# se puede invocar en el codigo principal  usando import operaciones
#esto se invoca la codigo principal 
def sumar(a,b):
     resultado = a + b 
     return resultado

def new_func(resultado):
  return resultado

def restar (a,b):
  resultado = a - b
  return resultado

def multiplicar(a, b):
    resultado = a*b
    return resultado

def dividir (a, b):
 if b==(0):
  print ("0 no es un numero divisible")
 else:
    resultado = a / b
    return resultado
 
 def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
    
def potencia(a, b):
    resultado = a ** b
    return resultado

def potencia(base, exponente):
    return base ** exponente
