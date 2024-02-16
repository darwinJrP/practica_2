from datetime import datetime

class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad='peruana'):
        self.nombre = nombre
        self.edad = self.verificar(edad)
        self.saldo = saldo
        self.nacionalidad = nacionalidad

    def solicitar(self):
        try:
            self.nombre = input("Ingrese el nombre de la persona: ")
            edad = input("Ingrese la edad de la persona: ")
            self.edad = self.verificar(edad)
        except ValueError as x:
            print(f"Error: {x}")

    def cumpleanios(self):
        self.edad = self.edad + 1
        print(f"{self.nombre} Ha cumplido años. Su edad actual es {self.edad} años.")

    def verificar(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad no puede ser negativa.")
            return edad
        except ValueError:
            raise ValueError("La edad debe ser un número entero válido.")

#CREAMOS OTRA FUNCIÓN
def obtener_fecha_hora_actual():
    tiempo_actual = datetime.now()
    return tiempo_actual.strftime("%Y-%m-%d %H:%M")

# INSTANCIANDO LAS PERSONAS
persona1 = Persona(nombre="", edad=0, saldo=4000)

persona1.solicitar()
persona1.cumpleanios()

fecha_registro_persona1 = obtener_fecha_hora_actual()
print(f"Fecha de registro de la persona 1: {fecha_registro_persona1}")

persona2 = Persona(nombre="", edad=0, saldo=6000)

persona2.solicitar()
persona2.cumpleanios()

fecha_registro_persona2 = obtener_fecha_hora_actual()
print(f"Fecha de registro de la persona 2: {fecha_registro_persona2}")
