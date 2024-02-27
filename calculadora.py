def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir entre cero"
    return num1 // num2

print("Calculadora")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Selecciona una opción (1-4): ")

if opcion in ['1', '2', '3', '4']:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    if opcion == '1':
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == '2':
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    else:
        resultado = division(num1, num2)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print("El resultado de la división es:", resultado)
else:
    print("Opción inválida. Por favor, selecciona una opción válida del 1 al 4.")