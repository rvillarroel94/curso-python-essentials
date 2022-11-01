# -*- coding: utf-8 -*-
"""
@author: rvillarroel94
"""
# Inicia la ejecución del Script

# Obtiene los valores maximos y minimos
def minMax(dictionary, valueMax, valueMin):
    result = []
    # Copia los valores en formato de lista a una variable local
    dataLocal = list(dictionary.values())
    # Setea la variable para controlar la cantidad de maximos
    cantMin = 0
    # Setea la variable para controlar la cantidad de minimos
    cantMax = 0
    hasTuple = False
    
    # Verifica que si el dicionario seleccionado tiene tuplas
    for index, item in enumerate(dataLocal):
        if(isinstance(item, tuple)):
            hasTuple = True
            # Si el item es una tupla se transforma a una lista para mejorar el procesamiento
            dataLocal[index] = list(item)
    
    # Se obtienen los valores de maximos y minimos ingresados
    while ((cantMin < valueMin) or (cantMax < valueMax)):
        if(hasTuple):
            # Se recorre la dataLocal para obtener los valores
            for index, item in enumerate(dataLocal):
                if(isinstance(item, list)):
                    # Si el item actual ya no tiene elementos disponibles se sigue al siguiente
                    if(len(item)==0):
                        continue
                    # Si aun no se cumple la cantidad de maximos solicitados se vuelve a obtener un maximo
                    if(cantMax < valueMax):
                        tempValue = max(item)
                        result.append(tempValue)
                        cantMax+=1
                        del item[item.index(tempValue)]
                    # Si aun no se cumple la cantidad de minimo solicitados se vuelve a obtener un minimo    
                    if(cantMin < valueMin):
                        tempValue = min(item)
                        result.append(tempValue)
                        del item[item.index(tempValue)]
                        cantMin +=1
                    
        else:
            # Si aun no se cumple la cantidad de maximos solicitados se vuelve a obtener un maximo
            if(cantMax < valueMax):
                tempValue = max(dataLocal)
                result.append(tempValue)
                cantMax+=1
                del dataLocal[dataLocal.index(tempValue)]
            
            # Si aun no se cumple la cantidad de minimo solicitados se vuelve a obtener un minimo
            if(cantMin < valueMin):
                tempValue = min(dataLocal)
                result.append(tempValue)
                del dataLocal[dataLocal.index(tempValue)]
                cantMin +=1
    return result

# optiene del usuario los valores para la cantidad de maximos y minimos validos
def solicitarMinMax(longDictionary):
    while True:
        try:
            # Se imprime en consola las opciones disponibles para el usuario
            minimos=int(input('Digite el número de máximos que desea mostrar: '))
            maximos=int(input('Digite el número de mínimos que desea mostrar: '))
            # verifica que los valores indicados sean mayores a cero y menores a la longitud del diccionario
            minimos=minimos if (minimos > 0 and minimos < longDictionary) else 0
            maximos=maximos if (maximos > 0 and maximos < longDictionary) else 0
            # verifica que los valores indicados sean correctos
            if(minimos > 0 and maximos > 0 and maximos + minimos <= longDictionary):
               return([minimos, maximos])
            else:
                # En caso que los valores ingresados sean incorrectos se vuelve a solicitar al usuario
                print('Ingrese valores minimos y maximos correctamente...')
        except:
            print('Ingrese valores minimos y maximos correctamente...')


# Obtiene los valores maximos y minimos segun lo especificado por el usuario
def workWithDictionary():
    while True:
        dictionary = 0
        # Se imprime en consola las opciones disponibles para el usuario
        print('Elija un diccionario para la demostración:')
        print('1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}')
        print('2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}')
        print('3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}')
        print('4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}')
        option = input('Que diccionario desea: ')
        
        # Segun la opcion ingresada por el usuario se setea la variable dictionary con la cual se trabajara
        if(option=='1'):
            dictionary = {'Raul':34,'Paula':19,'Jorge':43,'Richard':10,'Diana':3,'Isabel':76,'Gustavo':12,'Diego':37}
        elif(option=='2'):
            dictionary = {'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)}
        elif(option=='3'):
            dictionary = {'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)}
        elif(option=='4'):
            dictionary = {'tplA':(4,-12,56,-34,98,102),'tplB':(9,0,1,10,-3,14),'tlpC':(87,12,56,987,-61)}
        else:
            print('El valor ingresado no es correcto. Vuelva a intentarlo...')
            
        if(dictionary!=0):
            # solicita al usuario los valores para la cantidad de maximos y minimos
            cantAvalible = 0
            # Obtiene la cantidad de valores disponibles
            for index, item in enumerate(dictionary):
                if(isinstance(item, tuple)):
                    cantAvalible+=len(item)
                else:
                    cantAvalible+=1
            valuesMinMax = solicitarMinMax(cantAvalible)
            # Obtiene los valores maximos y minimos
            result = minMax(dictionary, valuesMinMax[0], valuesMinMax[1])
            print('Valores calculados en formato LISTA: ', end='')
            # Imprime los valores formato de lista
            print(result)
            print('Valores calculados en formato TUPLA: ', end='')
            # Imprime los valores formato de tupla
            print(tuple(result))
            break
        
        print("")
        print("")
        
# Ejecuta el programa

# Termina la ejecución del Script