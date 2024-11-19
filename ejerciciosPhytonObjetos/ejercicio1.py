class Persona :
    __especie = "Humano"
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def get_Object(self) :
        return self.__nombre,self.__edad
    
    def anadir_Anos(self) :
        return self.__edad+1
    def __str__(self) :
        datos =str("mi nombre es :" + self.__nombre +" y mi edad es : " + str(self.__edad) + " y soy : "+ self.__especie)
        return datos
    def get_Edad(self):
        return self.__edad
    def set_Edad(self,edadModificada):
        self.__edad=edadModificada
        return self.__edad
    
class Estudiante(Persona) :
    def __init__(self, nombre, edad,universidad):
        super().__init__(nombre, edad)
        self.__universidad = universidad

    def __str__(self):
        datos = str(" y la universidad es : " + self.__universidad)
        return super().__str__() + datos
    
class Profesor(Persona) :
    def __init__(self, nombre, edad,asignatura):
        super().__init__(nombre, edad)
        self.__asignatura = asignatura
    
    def __str__(self):
        datos = str(" la asignatura es :" + self.__asignatura)
        return super().__str__() + datos
    
persona = Persona("ivan",33,)
estudiante = Estudiante("raul",22,"miami")
profesor = Profesor("santi",46,"lenguaje de marcas")

list = [persona,estudiante,profesor]
for i in list :
    print(i)

persona.set_Edad(24)
print(persona)
    
        