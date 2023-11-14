'''26.- Declarar una clase Cuenta y dos subclases CajaAhorro y PlazoFijo.
Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.'''

import operaciones

cajaAhorro_usera = operaciones.CajaAhorro("Dario", 34000)
cajaAhorro_usera.imprimir()

plazoFijo_usera = operaciones.PlazoFijo("Dario", 40000, 20, 1.25)
plazoFijo_usera.imprimir()