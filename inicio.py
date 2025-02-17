#import random
#lista2 = [random.randint(0,100) for _ in range(100)]


#def busquedaSecuencial(unaLista, item):
#    pos = 0
#    encontrado = False
#    while pos < len(unaLista) and not encontrado:
#        if unaLista[pos] == item:
#            encontrado = True
#        else:
#            pos = pos + 1
#    return encontrado

#listaPrueba = [1,2,32,8,17,19,42,13,0]
#print(busquedaSecuencial(listaPrueba, 3))
#print(busquedaSecuencial(listaPrueba, 13))  



import time
import random

def busquedaSecuencial(unaLista, item):
    pos = 0
    encontrado = False
    inicio = time.time()
    while pos < len(unaLista) and not encontrado:
        if unaLista[pos] == item:
            encontrado = True
        else:
            pos = pos + 1
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return encontrado, tiempo_ejecucion

# Crear una lista de 1000 números aleatorios
listaPrueba = random.sample(range(10000), 1000)

# Número de repeticiones para obtener un tiempo promedio
num_repeticiones = 1000

# Prueba para el número 3
tiempo_total = 0
for _ in range(num_repeticiones):
    resultado, tiempo = busquedaSecuencial(listaPrueba, 3)
    tiempo_total += tiempo
tiempo_promedio = tiempo_total / num_repeticiones
print(f"¿Se encontró el número 3?: {resultado}, Tiempo de ejecución promedio: {tiempo_promedio:.7f} segundos")

# Prueba para un número que sabemos que está en la lista (ejemplo: el primer elemento)
elemento_a_buscar = listaPrueba[0]
tiempo_total = 0
for _ in range(num_repeticiones):
    resultado, tiempo = busquedaSecuencial(listaPrueba, elemento_a_buscar)
    tiempo_total += tiempo
tiempo_promedio = tiempo_total / num_repeticiones
print(f"¿Se encontró el número {elemento_a_buscar}?: {resultado}, Tiempo de ejecución promedio: {tiempo_promedio:.7f} segundos")

      


