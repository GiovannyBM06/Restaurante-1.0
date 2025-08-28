from src.COMIDA import *
class PLATOFUERTE(COMIDA):
    def __init__(self, nombre:str, precio:float, ingredientes:list):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes
    def mostrar(self)->str:
        return f"{self.nombre}\n Precio: ${self.get_precio()}\n Ingredientes: {(', '.join(self.ingredientes))}"