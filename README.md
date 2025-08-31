# Restaurante

## Autores
**Giovanny Bedoya Montes**  
**Sergio Alejandro Diosa Laverde**  
Instituto Tecnológico Metropolitano (ITM)  
Período Académico: 2025-2

## Descripción

Este proyecto es una simulación básica de un sistema de pedidos en un restaurante.  
Está desarrollado en **Python** aplicando los principios de **Programación Orientada a Objetos (POO)**.

Mediante un menú de opciones ejecutado por consola el programa permite:
- Visualizar un menú con los diferentes tipos de platos que se ofrecen **Platos fuertes, Bebidas y Postres**.
- Ordenar productos y agregarlos a la cuenta.
- Mostrar los platos que han sido consumidos y así mismo calcular el **total a pagar**.
- Añadir una **propina** y mostrar el total final.

## Estructura del programa
- **Clase COMIDA**: Clase padre que contiene los atributos comunes como nombre y precio.
- **Clases hijas**:
  - `PLATOFUERTE`: incluye la lista de ingredientes de cada  plato.
  - `BEBIDA`: incluye el tamaño en onzas.
  - `POSTRE`: incluye el sabor.
- **Clase CUENTA**: almacena los pedidos, calcula el total y la propina.

## Menú principal
Al ejecutar el programa se muestra el siguiente menú en consola:

```bash
   ===== MENÚ DEL RESTAURANTE =====
    1. Ver Platos Fuertes
    2. Ver Bebidas
    3. Ver Postres
    4. Mostrar cuenta
    5. Calcular propina
    0. Salir
    ===============================
```

## Propósito del proyecto

El propósito de este proyecto es aplicar los conceptos de **Programación Orientada a Objetos** en Python mediante la simulación de un sistema de pedidos para un restaurante.  

De igual manera se busca poener en práctica el uso de **Git y GitHub** como herramientas de control de versiones. También el uso de las buenas prácticas en el desarrollo colaborativo, esto mediante **la protección de ramas, pull requests y el manejo de coversaciones**. 

## Ejecutar el programa

#### 1.Verificar la instalación de phyton y de Git
Para comprobarlo ejecuta los comandos
```bash
py --version
```
y 
```bash
git --version
```
Luego de comprobar que ambos estan instalados podemos seguir.
#### 2. Clonar el repositorio 
Primero debes clonar el repositorio desde GitHub. Abre la terminal y ejecuta:
```bash
git clone https://github.com/GiovannyBM06/Restaurante.git
```
#### 3. Entra a la carperta del proyecto
Ejecuta lo siguente 
```bash
cd Restaurante
```

#### 4.  Cambia de rama 
Una vez en la carpeta el proyecto cambia a la rama Dev, QA o Prod
```bash
git checkout Prod
```
#### 5. Entra a la carpeta src
posteriormente entraremos a la carpeta src, ejecuta el siguente comando
```bash
cd src
```

#### 6. Correr el programa
Una vez hecho todo esto podemos ejecutar el archivo principal para correr el programa.
```bash
py main.py
```

### 7. Interartuar con el menú
Una vez en ejecución, aparecerá el menú del restaurante en consola y podremos interacctuar con el mismo.