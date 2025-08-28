class COMIDA:
    def __init__(self, nombre:str, precio:float):
        self.nombre = nombre
        self.__precio = precio # atributo privado
    def get_precio(self)->float:
        return self.__precio   