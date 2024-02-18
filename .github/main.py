class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio= precio
        self.registro = registro

    def cambiarColor(self,color):
        if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
           self.color= color


class Motor:
    def __init__(self, numeroCilindro,tipo,registro):
        self.numeroCilindro = numeroCilindro
        self.tipo=tipo
        self.registro = registro

    def asignarTipo(self,tipo):
        self.tipo= tipo
    
    def cambiarRegistro(self,registro):
        self.registro= registro

