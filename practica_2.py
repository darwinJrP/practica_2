"""
2. Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas.
"""
class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad='peruana'):
        self.nombre = nombre
        self.edad = self.verificar(edad)
        self.__saldo = saldo
        self.nacionalidad = nacionalidad

    def solicitar(self):
        try:
            self.nombre = input("Ingrese el nombre de la persona: ")
            edad = input("Ingrese la edad de la persona: ")
            self.edad = self.verificar(edad)
        except ValueError as x:
            print(f"Error: {x}")


    def cumpleanios(self):
        self.edad += 1
        print(f"{self.nombre} Ha cumplido años. Su edad actual es {self.edad} años.")

    def verificar(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa.")
            return edad
        except ValueError:
            raise ValueError("La edad debe ser un número entero válido.")

    def transferencia(self, otra_persona, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            otra_persona.__saldo += monto
            print(f"Transferencia de {monto} realizada de {self.nombre} a {otra_persona.nombre}.")
            print(f"Saldo actual de {self.nombre}: {self.__saldo}")
            print(f"Saldo actual de {otra_persona.nombre}: {otra_persona.__saldo}")
        else:
            print("Saldo insuficiente.")

    def obtener_saldo(self):
        return self.__saldo


# Crear instancias de la clase Persona
persona1 = Persona(nombre="", edad=0, saldo=5000)

persona1.solicitar()

persona2 = Persona(nombre="", edad=0, saldo=3000)

persona2.solicitar()

persona1.transferencia(persona2, 1000)

print(f"Saldo actual de {persona1.nombre}: {persona1.obtener_saldo()}")
print(f"Saldo actual de {persona2.nombre}: {persona2.obtener_saldo()}")


