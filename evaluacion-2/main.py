# -*- coding: utf-8 -*-
"""
@author: rvillarroel94
"""

from TiposDeDatos import verTipos,verIntances
from PruebaInput import pruebaInput
from ValidarContraseña import validarConstraseña 
from WorkingList import separarPares, separarValoresAtipicos 
from DibujarRectangulo import dibujarrectangulo 
from WorkingDictionarys import workWithDictionary 
from CalcularPromedio import calcularPromedio 
from VerificarColores import verificarColores 
from PruebaMenu import printMenu 


# Inicia la ejecución del Script
def mostrarEnd():
    print('Fin del programa.')
    input('Presione enter para continuar...')
    print()
    print()


def main():
    run=True
    while run:
        print("Programa Final del Curso de Python Essensials")
        print()
        print("1) Ver tipos básicos de datos.")
        print("2) Verificación de tipos básicos de datos.")
        print("3) Prueba de función input.")
        print("4) Validar contraseña.")
        print("5) Trabajando con listas: Separar pares e impares.")
        print("6) Trabajando con listas: Separar valores típicos y  atípicos.")
        print("7) Dibujar Rectangulo.")
        print("8) Trabajando con diccionarios.")
        print("9) Calcular Promedio.")
        print("10) verificar Colores.")
        print("11) Prueba de un menú.")
        print()
        print("20) Terminar el Programa.")
        print()
        option = input("Selecciones una de las opciones presentadas: ")
        if(option=='1'):
            verTipos()
        elif(option=='2'):
            verIntances()
        elif(option=='3'):
            pruebaInput()
        elif(option=='4'):
            validarConstraseña()
        elif(option=='5'):
            separarPares()
        elif(option=='6'):
            separarValoresAtipicos()
        elif(option=='7'):
            dibujarrectangulo()
        elif(option=='8'):
            workWithDictionary()
        elif(option=='9'):
            calcularPromedio()
        elif(option=='10'):
            verificarColores()
        elif(option=='11'):
            printMenu()
        elif(option=='20'):
            run=False
        else:
            print('Opcion ingresada no valida vuelva a intentar')
            continue
        
        if(option!='20'):
            mostrarEnd()


# Ejecuta el programa
main()
# Termina la ejecución del Script
