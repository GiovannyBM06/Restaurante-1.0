from PLATOFUERTE import *
from BEBIDA import *
from POSTRES import *  
from COMIDA import *

bandeja1 = PLATOFUERTE("Arroz con pollo", 12.50, ["arroz", "pollo", "verduras"])
bandeja2 = PLATOFUERTE("Carne asada", 15.00, ["carne", "papas", "ensalada"])
bandeja3 = PLATOFUERTE("Pasta Alfredo", 13.00, ["pasta", "crema", "pollo"])
bandeja4 = PLATOFUERTE("Pescado frito", 14.50, ["pescado", "limón", "yuca"])
bandeja5 = PLATOFUERTE("Tacos", 11.00, ["tortilla", "carne", "salsa"])

bebida1 = BEBIDA("Jugo de naranja", 3.50, 12)
bebida2 = BEBIDA("Coca Cola", 2.50, 16)
bebida3 = BEBIDA("Agua", 1.00, 20)
bebida4 = BEBIDA("Café", 2.00, 8)
bebida5 = BEBIDA("Té helado", 2.75, 14)

postre1 = POSTRE("Flan", 4.00, "vainilla")
postre2 = POSTRE("Pastel", 5.00, "chocolate")
postre3 = POSTRE("Helado", 3.50, "fresa")
postre4 = POSTRE("Tarta", 4.50, "manzana")
postre5 = POSTRE("Gelatina", 2.00, "uva")

platosfuertes = [bandeja1, bandeja2, bandeja3, bandeja4, bandeja5]
bebidas = [bebida1, bebida2, bebida3, bebida4, bebida5]
postres = [postre1, postre2, postre3, postre4, postre5] 
