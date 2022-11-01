# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:14:52 2022

@author: DGIP-Admin
"""
def dibujarrectangulo():
    
    print("Programa para Dibujar Rectangulo")
    largo = 0
    ancho = 0
    while True:
        try:
            largo = int(input("Ingrese el largo del rectangulo: "))
            ancho = int(input("Ingrese el ancho del rectangulo: "))
        except:
            print("Ingrese valores enteros validos para ancho y largo")
            continue
        if(largo > 0 and ancho > 0):
            if(largo != ancho):
                break
            else:
                print("Los valores de ancho y largo deben ser diferentes")
        else:
            print("Ingrese valores para ancho y largo diferentes de cero")
        
    largo = range(0,largo)
    ancho = range(0,ancho)
    for col in largo:
        for row in ancho:
            print("R", end="")
        print()
