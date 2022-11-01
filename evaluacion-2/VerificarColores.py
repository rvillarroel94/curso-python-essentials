# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:11:15 2022

@author: rvillarroel94
"""
def verificarColores():
    lst1 = ["azul", "amarillo", "verde", "rojo", "blanco"]
    var1 = input("Ingrese un color: ")
    if var1 in lst1:
        print(f"El color {var1} es válido.")
    else:
        print(f"El color {var1} no es válido.")