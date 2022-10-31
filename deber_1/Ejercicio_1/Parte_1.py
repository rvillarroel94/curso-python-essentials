# -*- coding: utf-8 -*-
"""
@author: rvillarroel94
"""
# Inicia la ejecución del Script

# la funcion print() muestra en la consola el parametro que se envía
print("Empezando a trabajar con Python")
print("Realizado por: Ricardo Villarroel")
print()
print("Consultando los tipos de valores:")
print()

# Declaramos las variables las cuales vamos a utilizar luego
var1=875
# Mostramos un print con formato para eso indicamos la f antes de la cadena de texto a formatear
print(f"El tipo de dato de {var1} es:")
# mandamos a impimir en consola el tipo de la variable que se obtiene con la funcion nativa de Python type()
print(type(var1))
print()

# En las siguientes lineas seguimos con las mismas instrucciones a python como en las anteriores que se especificaron
var2=4.89
print(f"El tipo de dato de {var2} es:")
print(type(var2))
print()


var3="Now is better than never"
print(f"El tipo de dato del texto: {var3} es:")
print(type(var3))
print()

var4=1.32
print(f"El tipo de dato del texto: {var4} es:")
print(type(var4))
print()


var5=5+8j
print("¿El valor 5 + 8i corresponde a un valor entero?")
# para saber si una variable es de un tipo en especifico se ultiliza la funcion nativa de isinstance()
print(isinstance(var5,int))
print()


# En las siguientes lineas seguimos con las mismas instrucciones a python como en las anteriores que se especificaron
var6=8.2
print("¿El valor 8.2 corresponde a un valor entero?")
print(isinstance(var6,int))
print()

var7="Readability counts"
print("¿El texto: Readability counts. corresponde a un string?")
print(isinstance(var7,str))

# Termina la ejecución del Script