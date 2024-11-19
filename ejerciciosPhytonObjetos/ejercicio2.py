class Calculadora :
    def sumar(num1,num2):
        return num1+num2
    
print(Calculadora.sumar(1,2))

class Vector :
    def __init__(self,x,y):
        self.__x =x
        self.__y =y
    

    @property
    def _x(self):
        return self.__x

    @_x.setter
    def _x(self, value):
        self.__x = value

    @property
    def _y(self):
        return self.__y

    @_y.setter
    def _y(self, value):
        self.__y = value

    def sumarVectores(self,vectorIntroducido) :
        sumaX =vectorIntroducido.__x + self.__x
        sumaY=vectorIntroducido.__y + self.__y
        nuevoVector = Vector(sumaX,sumaY)
        return nuevoVector
    def __str__(self):
        datos = str(self.__x) +" "+ str(self.__y)
        return datos
    
vector = Vector(5,6)
print(vector.sumarVectores(vectorIntroducido=Vector(1,2)))

class Persona :
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    def crearDesdeCadena(cadena) :
            atributos = cadena.split()
            nombre = atributos[0]
            edad = atributos[1]
            persona = Persona(nombre,edad)
            return persona

class Motor :
    
    def __init(self,accion):
        self.__accion = accion
    def enMarcha(self):
        if(self.__accion==True):
            return print("coche en marcha")
        else:
            return print("coche parado")
    


        