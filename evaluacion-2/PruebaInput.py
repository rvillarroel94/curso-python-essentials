# -*- coding: utf-8 -*-
"""
@author: rvillarroel94
"""
# Inicia la ejecución del Script

def pruebaInput():
    # la funcion print() muestra en la consola el parametro que se envía
    print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")
    print()

    # la funcion input() muestra en la consola el texto que se envía como parametro y se detiene el programa hasta que el usuario ingrese algo mediante el teclado
    var1=input("Primera Interacción, ingrese un valor cualquiera: ")
    print("Este tipo de dato en Python es:")
    # Imprime el tipo del valor ingresado por el usuario
    print(type(var1))
    print()

    # En las siguientes lineas seguimos con las mismas instrucciones a python como en las anteriores que se especificaron
    var2=input("Segunda Interacción, ingrese un valor cualquiera: ")
    print("Este tipo de dato en Python es:")
    print(type(var2))
    print()

    var3=input("Tercera Interacción, ingrese un valor cualquiera: ")
    print("Este tipo de dato en Python es:")
    print(type(var3))
    print()

    var4=input("Cuarta Interacción, ingrese un valor cualquiera: ")
    print("Este tipo de dato en Python es:")
    print(type(var4))
    print()

    var5=input("Quinta Interacción, ingrese un valor cualquiera: ")
    print("Este tipo de dato en Python es:")
    print(type(var5))
    print()

    print("¡YA NO SE HARÁN MÁS INTERACCIONES")

# Termina la ejecución del Script