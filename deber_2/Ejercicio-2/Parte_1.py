# -*- coding: utf-8 -*-
"""
@author: rvillarroel94
"""
# Inicia la ejecución del Script

# Considerando la siguiente lista codifique un programa que permita separar los números pares e impares.
# Identifique también los posibles valores que considere atípicos a ese arreglo.

Datos_2021 = [1, 2, 3, 4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]

# Declaramos la variable donde apuntará a nuestra lista de valores pares
Lista_pares = []
# Declaramos la variable donde apuntará a nuestra lista de valores Impares
Lista_impares = []

# Mediante la estructura de control interactiva FOR vamos a recorrer el array Datos_2021 y separar los valores pares e impares
for item in Datos_2021:
    # Para seleccionar los valores pares se utiliza el operador aritmético mod %, ya que para saber si un número es par el residuo de la división para dos debe ser 0
    if item%2==0:
        # Mediante el metodo Append de la listas se agregan los items Pares
        Lista_pares.append(item)
    else:
        # Mediante el metodo Append de la listas se agregan los items Impares
        Lista_impares.append(item)

# Utilizando la funcion print se muestran la lista creada con solo los valores pares 
print("Valores Pares")
print(Lista_pares)
# Utilizando la funcion print se muestran la lista creada con solo los valores impares 
print("Valores Impares")
print(Lista_impares)



# Declaramos la variable donde apuntará a nuestra lista de valores tipicos
Lista_tipicos = []
# Declaramos la variable donde apuntará a nuestra lista de valores atipicos
Lista_atipicos = []
# Mediante la estructura de control interactiva FOR vamos a recorrer el array Datos_2021 y separar los valores tipicos y atipicos
for item in Datos_2021:
    # Considerando arbitrariamente que los valores mayores a 90 son valores atipicos se realiza la separación
    if item > 90:
        # Mediante el metodo Append de la listas se agregan los items atipicos
        Lista_atipicos.append(item)
    else:
        # Mediante el metodo Append de la listas se agregan los items tipicos
        Lista_tipicos.append(item)

# Utilizando la funcion print se muestran la lista creada con solo los valores tipicos 
print("Valores Típicos")
print(Lista_tipicos)
# Utilizando la funcion print se muestran la lista creada con solo los valores atipicos
print("Valores atípicos")
print(Lista_atipicos)

# Termina la ejecución del Script