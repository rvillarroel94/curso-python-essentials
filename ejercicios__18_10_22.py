# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:11:41 2022

@author: ricardo.villarroel
"""

"""

Se necesita una aplicación que muestre un menú con tres
opciones:  “1. Comenzar programa, 2. Mostrar segundo mensaje,
3. Finalizar programa”. El usuario debe poder seleccionar una
opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del
error. El menú se debe volver a mostrar luego de ejecutada cada
opción excepto en la opción 3, se interrumpirá la impresión del
menú y el programa finalizará.

"""

var = True
while var:
    op = int(input("1. Comenzar programa\n2. Mostrar segundo mensaje\n3. Finalizar programa\nIngrese la opción que desea: "))
    if op == 1:
        print("Programa Inicio")
    elif op == 2:
        print("Mensaje Mostrado")
    elif op == 3:
        print("Saliendo del Programa")
        var  = False
    else:
        print(f"La opción ingresada {op} no válida")
        var  = False
        
        

