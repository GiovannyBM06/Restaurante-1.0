from CUENTA import *
operaciones = OPERACIONES()

while True:
    opcion = input("¿Qué deseas ordenar? ")
    print(operaciones.ordenar(opcion))
    print(f"El total a pagar es de : ${operaciones.total_pagar()}")
    print(operaciones.propina(10.0))
    if input("¿Deseas ordenar algo más? (s/n): ").lower() != 's': 
          break
