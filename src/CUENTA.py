from MENU import platosfuertes, bebidas, postres

class OPERACIONES:

    def __init__(self):
        self.platos = []

    def ordenar (self, op)->str:
        for plato in platosfuertes:
            if plato.nombre == op:
                self.platos.append(plato)
                return f"Has ordenado: {plato.nombre } - ${plato.get_precio()}"   
            
        for bebida in bebidas:
            if bebida.nombre == op:
                self.platos.append(bebida)
                return f"Has ordenado: {bebida.nombre } - ${bebida.get_precio()}"
            
        for postre in postres:
            if postre.nombre == op:
                self.platos.append(postre)
                return f"Has ordenado: {postre.nombre}-${postre.get_precio()}"    
        return "Plato no encontrado"    

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