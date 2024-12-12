class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad 

    def get_edad(self):
        return self.__edad

    
    def set_edad(self, edad):
        if edad >= 0:  
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")

    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.__edad})"


persona = Persona("Juan Perez", 30)
print(persona) 


edad_actual = persona.get_edad()
print(f"Edad actual: {edad_actual}") 

persona.set_edad(35)
print(persona) 


persona.set_edad(-5)  
