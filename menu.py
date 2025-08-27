from platos import platofuerte, bebida, postre

bandeja1 = platofuerte("Arroz con pollo", 12.50, ["arroz", "pollo", "verduras"])
bandeja2 = platofuerte("Carne asada", 15.00, ["carne", "papas", "ensalada"])
bandeja3 = platofuerte("Pasta Alfredo", 13.00, ["pasta", "crema", "pollo"])
bandeja4 = platofuerte("Pescado frito", 14.50, ["pescado", "limón", "yuca"])
bandeja5 = platofuerte("Tacos", 11.00, ["tortilla", "carne", "salsa"])

bebida1 = bebida("Jugo de naranja", 3.50, 12)
bebida2 = bebida("Coca Cola", 2.50, 16)
bebida3 = bebida("Agua", 1.00, 20)
bebida4 = bebida("Café", 2.00, 8)
bebida5 = bebida("Té helado", 2.75, 14)

postre1 = postre("Flan", 4.00, "vainilla")
postre2 = postre("Pastel", 5.00, "chocolate")
postre3 = postre("Helado", 3.50, "fresa")
postre4 = postre("Tarta", 4.50, "manzana")
postre5 = postre("Gelatina", 2.00, "uva")

PLATOFUERTES = [bandeja1, bandeja2, bandeja3, bandeja4, bandeja5]
BEBIDAS = [bebida1, bebida2, bebida3, bebida4, bebida5]
POSTRES = [postre1, postre2, postre3, postre4, postre5] 

for plato in PLATOFUERTES:
    print(plato.mostrar())