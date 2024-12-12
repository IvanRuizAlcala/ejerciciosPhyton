class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def crear_desde_cadena(cls, cadena):
        try:
            nombre, edad = cadena.split(", ")
            edad = int(edad)
            return cls(nombre, edad)
        except ValueError:
            print("Error: La cadena debe tener el formato 'Nombre, Edad'.")

    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

cadena = "Juan Perez, 30"
persona = Persona.crear_desde_cadena(cadena)
print(persona) 

