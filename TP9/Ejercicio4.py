class Agenda:
    def __init__(self):
        self.contactos = []
    
    def menu(self):
        while True:
            print("\n--- Menú de Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            
            opcion = input("Selecciona una opción (1-5): ")
            
            if opcion == '1':
                self.agregar_contacto()
            elif opcion == '2':
                self.lista_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")
    
    def agregar_contacto(self):
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el teléfono del contacto: ")
        email = input("Ingresa el email del contacto: ")
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print(f"Contacto {nombre} añadido exitosamente.")
    
    def lista_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            print("\n--- Lista de Contactos ---")
            for idx, contacto in enumerate(self.contactos, start=1):
                print(f"{idx}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    
    def buscar_contacto(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            nombre = input("Ingresa el nombre del contacto a buscar: ")
            encontrado = False
            for contacto in self.contactos:
                if contacto['nombre'] == nombre:
                    print(f"Contacto encontrado - Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró ningún contacto con el nombre {nombre}.")
    
    def editar_contacto(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            nombre = input("Ingresa el nombre del contacto a editar: ")
            encontrado = False
            for contacto in self.contactos:
                if contacto['nombre'] == nombre:
                    nuevo_telefono = input(f"Nuevo teléfono para {contacto['nombre']}: ")
                    nuevo_email = input(f"Nuevo email para {contacto['nombre']}: ")
                    contacto['telefono'] = nuevo_telefono
                    contacto['email'] = nuevo_email
                    print(f"Contacto {contacto['nombre']} editado exitosamente.")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró ningún contacto con el nombre {nombre}.")

# Ejemplo de uso
agenda = Agenda()
agenda.menu()
