# Ejercicio 1: Calculadora simple

# Instrucciones:
# - Pedir al usuario el primer número.
# - Pedir al usuario el segundo número.
# - Preguntar qué operación desea realizar (+, -, *, /).
# - Mostrar el resultado con el mensaje: "El resultado es: "

# Tu código aquí:

# Solicitar el primer número:
num1 = float(input("Primer numero: "))

# Pedir la operación a realizar:
op = input("Operacion (+, -, *, /): ")

# Solicitar el segundo número:
num2 = float(input("Segundo numero: "))


# Calcular el resultado según la operación:
if op == '+':
  print("El resultado es:", num1 + num2)
elif op == '-':
  print("El resultado es:", num1 - num2)
elif op == '*':
  print("El resultado es:", num1 * num2)
elif op == '/':
  print("El resultado es:", num1 / num2)

# Mostrar el resultado:
# print("El resultado es:", ...)
