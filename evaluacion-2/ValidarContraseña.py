# -*- coding: utf-8 -*-
"""
@author: rvillarroel94
"""

"""
Desarrollar un programa que permita validar la contraseña introducida por un usuario con las siguientes comprobaciones:
 Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.
 Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.
 Debe contener al menos un número entre 0 y 9.
 Debe contener un símbolo especial entre: $,%,*,@
 Tamaño mínimo de 5 caracteres y máximo de 15.
Se debe solicitar la contraseña al usuario, así como informarle sobre estos requisitos para su
contraseña, una vez validada mostrar un mensaje al usuario informándole al respecto
"""
def validarConstraseña():
    # Declaramos la variable donde apuntará a nuestra lista de caracteres en minusculas solicitados
    validMinusculas= ["a","b","c","d","e","f","g","h","i","j"]
    # Declaramos la variable donde apuntará a nuestra lista de caracteres en mayusculas solicitados
    validMayusculas= ["K","L","M","N","O","P","Q","R","S","T"]
    # Declaramos la variable donde apuntará a nuestra lista de caracteres de numeros solicitados
    validNumeros= ["1","2","3","4","5","6","7","8","9"]
    # Declaramos la variable donde apuntará a nuestra lista de caracteres especiales solicitados
    validCharacter= ["$","%","*","@"]
    # Declaramos la variable para a longitud minima de la contraseña
    minLeng= 5
    # Declaramos la variable para la longitud maxima de la contraseña
    maxLeng= 15

    # Declaramos la variable de control para saber si es invalida la contraseña ingresada
    invalid=True
    # Mediante la estructura de control interactiva WHILE vamos a realizar las solicitudes necesarias hasta obtner una contraseña valida
    while invalid:
        # Solicitamos al usuario que ingresa la contraseña mediante el teclado y asignamos ese valor a la variable password
        password = input("Ingrese la contraseña: ")
        # Convertimos la cadena de texto devuelta por la funcion input y la convertimos en una lista
        lstPassword = list(password)
        # Mediante la funcion len() obtenemos la longitud de la contraseña ingresada y comparamos si cumple con el minimo y el maximo de caracteres
        if len(lstPassword)>15 or len(lstPassword)<5:
            # De no cumplir con el maximo y minimo de caracteres se envia un mensaje al usuarios y regresa a solicitar nuevamente una contraseña valida
            print("Ingrese una contraseña que contenga entre 5 a 15 caracteres")
        else:
            # Se declara una variable de control boleana para saber si tiene al menos uno de los caracteres especiales solicitados
            hasValidCharacter= False
            # Se declara una variable de control boleana para saber si tiene al menos uno de los caracteres en minuscula solicitados
            hasValidMinusculas= False
            # Se declara una variable de control boleana para saber si tiene al menos uno de los caracteres en mayuscula solicitados
            hasValidMayusculas = False
            # Se declara una variable de control boleana para saber si tiene al menos uno de los caracteres numericos solicitados
            hasValidNumeros = False
            # Mediante la estructura de control interactiva FOR vamos a recorrer todo la lista de caracteres de la contraseña y verificar que cumpla con todos los requisitos
            for char in lstPassword:
                # busca el caracter actual en la lista de caracteres especiales solicitados
                if char in validCharacter:
                    # cambia el valor a True para indicar que si se encuentra al menos un caracter con la caracteristica solicitada
                    hasValidCharacter = True
                # busca el caracter actual en la lista de caracteres en minusculas solicitados
                if char in validMinusculas:
                    # cambia el valor a True para indicar que si se encuentra al menos un caracter con la caracteristica solicitada
                    hasValidMinusculas = True
                # busca el caracter actual en la lista de caracteres en mayusculas solicitados
                if char in validMayusculas:
                    # cambia el valor a True para indicar que si se encuentra al menos un caracter con la caracteristica solicitada
                    hasValidMayusculas = True
                # busca el caracter actual en la lista de caracteres de numeros solicitados    
                if char in validNumeros:
                    # cambia el valor a True para indicar que si se encuentra al menos un caracter con la caracteristica solicitada
                    hasValidNumeros = True
                    
            # Comprueba si se cumplio esta caracteristica solicida
            if hasValidCharacter:
                # Comprueba si se cumplio esta caracteristica solicida
                if hasValidMinusculas:
                    # Comprueba si se cumplio esta caracteristica solicida
                    if hasValidMayusculas:
                        # Comprueba si se cumplio esta caracteristica solicida
                        if hasValidNumeros:
                            # Al cumplirse todas las caracteristicas solicitadas se cambia el estado de la variable de control al ser una contraseña valida
                            invalid=False
                            # Muestra una cadena con formato para mostrarle al usuario un mensaje
                            print(f"La contraseña ingresada: '{password}'. Es una contraseña valida, gracias....")
                        else:
                            # Al no cumplirse con esta caracteristica muestra un mensaje del error al usuario
                            print("Ingrese una contraseña que contenga al menos un numero del 0 al 9")
                    else:
                        # Al no cumplirse con esta caracteristica muestra un mensaje del error al usuario
                        print("Ingrese una contraseña que contenga al menos uno de los siguientes caracteres en mayusculas 'K,L,M,N,O,P,Q,R,S,T'")
                else :
                    # Al no cumplirse con esta caracteristica muestra un mensaje del error al usuario
                    print("Ingrese una contraseña que contenga al menos uno de los siguientes caracteres en minuscula ' a,b,c,d,e,f,g,h,i,j'")
            else:
                # Al no cumplirse con esta caracteristica muestra un mensaje del error al usuario
                print("Ingrese una contraseña que contenga al menos uno de los siguientes caracteres especiales '$,%,*,@' ")
        

# Termina la ejecución del Script