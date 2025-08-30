from CUENTA import *
operaciones = OPERACIONES()


def mostrar_menu():
    print("\n===== MENÚ DEL RESTAURANTE =====")
    print("1. Ver Platos Fuertes")
    print("2. Ver Bebidas")
    print("3. Ver Postres")
    print("4. Mostrar cuenta")
    print("5. Calcular propina")
    print("0. Salir")
    print("===============================")

def mostrar_platos(lista, tipo):
    print(f"\n--- {tipo} ---")
    for i, plato in enumerate(lista,1):
        print(f"{i}. {plato.mostrar()}")
        print("-" * 30)



def main():
    while True:
        mostrar_menu()
        op = input("Selecione una opción: ")

        if op == "1":
            mostrar_platos(platosfuertes, "Platos Fuertes")
            eleccion = int(input("Seleccione el número del plato que desea ordenar: "))
            if 1 <= eleccion <= len(platosfuertes):
                operaciones.ordenar(platosfuertes[eleccion - 1])
                print(f"Has ordenado: {platosfuertes[eleccion - 1].nombre} - ${platosfuertes[eleccion - 1].get_precio()}")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        elif op == "2":
            mostrar_platos(bebidas, "Bebidas")
            eleccion = int(input("Seleccione el número de la bebida que desea ordenar: "))
            if 1 <= eleccion <= len(bebidas):
                operaciones.ordenar(bebidas[eleccion - 1])
                print(f"Has ordenado: {bebidas[eleccion - 1].nombre}- ${bebidas[eleccion - 1].get_precio()}")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        elif op == "3":
            mostrar_platos(postres, "Postres")
            eleccion = int(input("Seleccione el número del postre que desea ordenar: "))
            if 1 <= eleccion <= len(postres):
                operaciones.ordenar(postres[eleccion - 1])
                print(f"Has ordenado: {postres[eleccion - 1].nombre}-${postres[eleccion - 1].get_precio()}")
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

        elif op == "4":
            print(f"\nTotal a pagar: ${operaciones.total_pagar()} \n (no incluye propina)")

        elif op == "5":
            porcentaje = float(input("Ingrese el porcentaje de propina que desea dejar: "))
            print(operaciones.propina(porcentaje))
        elif op == "0":
            print("Gracias por visitarnos. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

main()  