# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:14:52 2022

@author: ricardo.villarroel
"""

"""
Se necesita una aplicación que disponga de un menú de 5 opciones con las siguientes funcionalidades:
1.    Dibuje un rectángulo con la letra “R”, el largo y ancho debe ser ingresado por el usuario.
2.    Partiendo de esta lista y tupla crear un diccionario que mantenga la información, todo en mayúsculas y con los parámetros numéricos codificados 
según la relación (raíz cuadrada(valor*45/100)).
[Sara, Pedro,Juan,María,Esther,Katalina,Jessica,Pierre,Galo]
(56,12,45,12,67,89,12,78,19)
3.    Solicitar un string al usuario y que se le devuelva una lista con las letras individuales del string y todo el string invertido.
4.    Solicitar tres números al usuario y que se muestren ordenados de menor a mayor y visceversa.
5.    Detener la operación de todo el programa.

En cada opción se deben enviar los resultados a un archivo de texto para registro.

"""
def saltar(lineas):
    for linea in range(0,lineas):
        print()

def printTitle(title):
    saltar(2)
    print("*"*(len(title)+5))
    print(title)
    print("*"*(len(title)+5))
    saltar(2)

def solicitarEntero(message):
    return(int(input(message))) 

def dibujarrectangulo():
    
    printTitle("Programa para Dibujar Rectangulo")
    largo = 0
    ancho = 0
    while True:
        largo = solicitarEntero("Ingrese el largo del rectangulo: ")
        ancho = solicitarEntero("Ingrese el ancho del rectangulo: ")
        if(largo > 0 and ancho > 0):
            if(largo != ancho):
                break
            else:
                print("Los valores de ancho y largo deben ser diferentes")
        else:
            print("Ingrese valores para ancho y largo diferentes de cero")
        
    saltar(2)
    largo = range(0,largo)
    ancho = range(0,ancho)
    for col in largo:
        for row in ancho:
            print("R", end="")
        print()
    
def procesarLista():
    print("procesarLista")
    
def invertirCadena():
    print("invertirCadena")
    
def ordenarNumeros():
    print("ordenarNumeros")

def mostrarMenu():
    printMenu = True
    while printMenu:
        printTitle("Programa de la clase del 20 de Octubre del 2022")
        print("1) Dibujar un rectangulo.\n2) Mostrar lista y tupla procesada.\n3) Split e invertir una cadena de texto.\n4) Ordenar números.\n5) Detener el programa")
        op=int(input("Ingrese la opción deseada: "))
        if(op==1):
            dibujarrectangulo()
        elif(op==2):
            procesarLista()
        elif(op==3):
            invertirCadena()
        elif(op==4):
            ordenarNumeros()
        elif(op==5):
            print("El programa se detendrá...")
            printMenu = False
        else:
            print("Opción no válida")
            printMenu = False
        if printMenu:
            saltar(4)

mostrarMenu()