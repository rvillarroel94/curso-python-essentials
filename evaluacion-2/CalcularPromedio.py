# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:11:15 2022

@author: rvillarroel94
"""
#lst1 = ["azul", "amarillo", "verde", "rojo", "blanco"]
#var1 = input("Ingrese un color: ")
#if var1 in lst1:
#    print(f"El color {var1} es válido.")
#else:
#    print(f"El color {var1} no es válido.")

def calcularPromedio():
    indice = 0
    arreglo=[0,0,0,0,0]
    while indice < 5:
        try:
            arreglo[indice]=int(input(f"Ingreso de valores: "))
        except:
            print('Ingrese un valor entero valido')
            continue
        indice+=1
        
    indice = 0
    suma = 0
    while indice < 5:
        print(f"el valor {indice+1} ingresado fue: {arreglo[indice]}")
        suma+=arreglo[indice]
        indice+=1

    print(f"El promedio de los valores ingresados es: {suma/(indice)}")