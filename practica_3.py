"""
3. Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente.
"""
def ingresar_datos():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Por favor ingrese números válidos.")

def division(num1, num2):
    while True:
        try:
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
            break
        except ZeroDivisionError:
            print("Error: División indeterminada")
            num2 = float(input("Ingrese un segundo número distinto de cero: "))

def evaluar_suma_datos_correctos():
    while True:
        try:
            num1, num2 = ingresar_datos()
            suma = num1 + num2
            print("La suma de los números es:", suma)
            break
        except ValueError:
            print("Error: Por favor ingrese números válidos.")

def ingresar_datos_lista():
    while True:
        try:
            n = int(input("Ingrese la cantidad de datos que desea ingresar a la lista: "))
            lista = []
            for i in range(n):
                dato = input("Ingrese el dato {}: ".format(i+1))
                lista.append(dato)
            indice = int(input("Ingrese el índice que desea consultar: "))
            print("El dato en el índice {} es: {}".format(indice, lista[indice]))
            break
        except ValueError:
            print("Error: Por favor ingrese un número entero.")
        except IndexError:
            print("Error: El índice ingresado está fuera de rango.")

if __name__ == "__main__":
    division(1, 0)
    evaluar_suma_datos_correctos()
    ingresar_datos_lista()

