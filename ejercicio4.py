# Ejercicio 4: Mayor de tres números
# Instrucciones:
# - Pedir tres números al usuario.
# - Determinar cuál es el mayor utilizando condicionales (if, elif, else).
# - Mostrar el número mayor con el mensaje: "El número mayor es: ".

# Tu código aquí:

# Pedir el primer número:
num1 = float(input("Ingresa el primer número: "))

# Pedir el segundo número:
num2 = float(input("Ingresa el segundo número: "))

# Pedir el tercer número:
num3 = float(input("Ingresa el tercer número: "))

# Comparar los números para saber cuál es el mayor:
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3


# Mostrar el resultado:
# print("El número mayor es:", ...)
print("El número mayor es:", mayor)