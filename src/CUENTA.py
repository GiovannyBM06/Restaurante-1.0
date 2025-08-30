from MENU import platosfuertes, bebidas, postres
from COMIDA import COMIDA
class OPERACIONES:

    def __init__(self):
        self.platos = []

    def ordenar (self, item):
        if isinstance(item,COMIDA):
            self.platos.append(item)

    def total_pagar(self)-> float:
        total:float = sum(plato.get_precio() for plato in self.platos)
        print(f"Detalle de la cuenta:")
        print("-"*30)
        for plato in self.platos:
            print(f"{plato.nombre} - ${plato.get_precio()}")
        print("-"*30)
        return total
    

    def propina(self, porcentaje:float)->str:
        total:float = sum(plato.get_precio() for plato in self.platos)
        propina =total*(porcentaje/100)
        total_propina = total + propina
        return f"La propina es de ${propina}\n El total con propina es de ${total_propina}"