from src.COMIDA import *
class BEBIDA(COMIDA):
    def __init__(self, nombre:str, precio:float, onzas:float):
        super().__init__(nombre, precio)
        self.onzas = onzas
    def mostrar(self)->str:
        return f"{self.nombre}\n Precio: ${self.get_precio()}\n Onzas: {self.onzas} oz"