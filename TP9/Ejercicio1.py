class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    # Setter y Getter para nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre
    
    # Setter y Getter para edad
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo.")
    
    def get_edad(self):
        return self.edad
    
    # Setter y Getter para DNI
    def set_dni(self, dni):
        if len(dni) == 9 and dni.isdigit():
            self.dni = dni
        else:
            print("El DNI debe contener 9 dígitos.")
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")
    
    def esMayorDeEdad(self):
        return self.edad >= 18

# Ejemplo de uso
persona1 = Persona("Juan", 25, "123456789")
persona1.mostrar()
print(f"¿Es mayor de edad?: {persona1.esMayorDeEdad()}")

persona2 = Persona()
persona2.set_nombre("Maria")
persona2.set_edad(16)
persona2.set_dni("987654321")
persona2.mostrar()
print(f"¿Es mayor de edad?: {persona2.esMayorDeEdad()}")
