import time
from typing import List


def archivo(n: int, filename: str):
    num_elements = 2 ** n
    print(f'Creando una lista de {num_elements} elementos.')
    my_list = list(range(num_elements))


    with open(filename, 'w') as f:
        for item in my_list:
            f.write(str(item) + '\n')


n = 23  
filename = "list.txt"

start_time = time.time()  
archivo(n, filename)
end_time = time.time() 
print(f"Tiempo para crear el archivo: {end_time - start_time:.4f} segundos")

def busqueda_binaria(lista: List[int], x: int) -> int:
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2

        if lista[medio] == x:
            return medio  
        elif lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1  

with open(filename, 'r') as f:
    lista = [int(line.strip()) for line in f]


search_item = 100

start_time = time.time()  
result = busqueda_binaria(lista, search_item)
end_time = time.time() 

if result != -1:
    print(f'Elemento encontrado en el índice {result}')
else:
    print('Elemento no encontrado')

print(f"Tiempo para la búsqueda binaria: {end_time - start_time:.4f} segundos")



