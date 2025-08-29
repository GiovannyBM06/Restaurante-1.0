from COMIDA import *
class POSTRE(COMIDA):
    def __init__(self, nombre:str, precio:float, sabor:str):
        super().__init__(nombre, precio)
        self.sabor = sabor
    def mostrar(self)->str:
        return f"{self.nombre}\n Precio: ${self.get_precio()}\n Sabor: {self.sabor}"
    