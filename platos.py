class comida:
    def __init__(self, nombre:str, precio:float):
        self.nombre = nombre
        self.__precio = precio # atributo privado
    def get_precio(self)->float:
        return self.__precio   

class platofuerte(comida):
    def __init__(self, nombre:str, precio:float, ingredientes:list):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes
    def mostrar(self)->str:
        return f"{self.nombre}\n Precio: ${self.get_precio()}\n Ingredientes: {(', '.join(self.ingredientes))}"
    
class bebida(comida):
    def __init__(self, nombre:str, precio:float, onzas:float):
        super().__init__(nombre, precio)
        self.onzas = onzas
    def mostrar(self)->str:
        return f"{self.nombre}\n Precio: ${self.get_precio()}\n Onzas: {self.onzas} oz"

class postre(comida):
    def __init__(self, nombre:str, precio:float, sabor:str):
        super().__init__(nombre, precio)
        self.sabor = sabor
    def mostrar(self)->str:
        return f"{self.nombre}\n Precio: ${self.get_precio()}\n Sabor: {self.sabor}"
    
# Pruebas