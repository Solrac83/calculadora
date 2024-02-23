def suma(a, b) :
    return a + b

def resta(a, b) :
    return a - b

def multiplicacion(a, b) :
    return a * b

def division(a, b) :
    if b != 0:
        return a /b
    else:
        return "Error: No esa posible dividir entre cero."
    
# Ejemplo de uso:

numero1 = float(input("ingresa el primer numero: "))
numero2 = float(input("ingresa el segundo numero: "))

print("suma:", suma(numero1, numero2))
print("resta:", resta(numero1, numero2))
print("multiplicacion:", multiplicacion(numero1, numero2))
print("division:", division(numero1, numero2))