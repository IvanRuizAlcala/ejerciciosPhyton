class Motor:
    def __init__(self):
        self.en_marcha = False

    def encender(self):
        self.en_marcha = True

    def apagar(self):
        self.en_marcha = False

    def estado(self):
        return self.en_marcha

class Coche:
    def __init__(self):
        self.motor = Motor()

    def arrancar_motor(self):
        self.motor.encender()
        print("El motor está en marcha.")

    def parar_motor(self):
        self.motor.apagar()
        print("El motor está apagado.")

    def estado_motor(self):
        if self.motor.estado():
            print("El motor está en marcha.")
        else:
            print("El motor está apagado.")

mi_coche = Coche()
mi_coche.estado_motor()  
mi_coche.arrancar_motor()  
mi_coche.estado_motor() 
mi_coche.parar_motor()  
mi_coche.estado_motor()  
