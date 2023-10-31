class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        # Constructor de la clase Persona
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Setters y Getters para nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre
    
    # Setters y Getters para edad
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo.")
    
    def get_edad(self):
        return self.edad
    
    # Setters y Getters para DNI
    def set_dni(self, dni):
        if len(dni) == 9 and dni.isdigit():
            self.dni = dni
        else:
            print("El DNI debe contener 9 dígitos.")
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        # Muestra los datos de la persona
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")
    
    def esMayorDeEdad(self):
        # Devuelve True si la persona es mayor de edad
        return self.edad >= 18


class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        # Constructor de la clase Cuenta
        self.titular = titular
        self.cantidad = cantidad
    
    # Setters y Getters para titular
    def set_titular(self, titular):
        self.titular = titular
    
    def get_titular(self):
        return self.titular
    
    # Setters y Getters para cantidad
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar(self):
        # Muestra los datos de la cuenta
        print(f"Titular: {self.titular.get_nombre()}, Cantidad: {self.cantidad}")
    
    def ingresar(self, cantidad):
        # Ingresa una cantidad a la cuenta si es positiva
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        # Retira una cantidad de la cuenta
        self.cantidad -= cantidad
