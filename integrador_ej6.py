
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

def get_edad(self):
    return self.__edad

def set_edad(self, edad):
    if 0 <= edad <= 150:  # Validar que la edad esté en un rango razonable
        self.__edad = edad
    else:
        print("Error: Edad fuera de rango")

def get_dni(self):
    return self.__dni

def set_dni(self, dni):
    if dni.isdigit() and len(dni) == 8:  # Validar que el DNI sea numérico y tenga 8 dígitos
        self.__dni = dni
    else:
        print("Error: DNI inválido")

def mostrar(self):
    print("Nombre:", self.__nombre)
    print("Edad:", self.__edad)
    print("DNI:", self.__dni)

def es_mayor_de_edad(self):
    return self.__edad >= 18

# Pedir datos al usuario
nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad: "))
dni = input("Ingrese el DNI: ")

# Crear instancia de Persona con los datos ingresados
persona = Persona(nombre, edad, dni)

# Mostrar los detalles de la persona
persona.mostrar()

if persona.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")