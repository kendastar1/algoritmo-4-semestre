import time

def archivo(n, filename ="archivo24.txt"):
    inicio_archivo = time.time()
    try:
        with open(filename, "w") as file:
            for i in range(n + 1):
                file.write(str(i) + "\n")
        print(f"Se ha creado el documento {filename}")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")
    finally:
        fin_archivo = time.time()
        tiempo_archivo = fin_archivo - inicio_archivo
        print(f"Tiempo de ejecución de la función archivo: {tiempo_archivo:.4f} segundos")

inicio_total = time.time()
try: 
    n = int(input("ingresa el valor de N: "))
    if n < 0:
        print("Ingrese un numero positivo.")
    else:
        inicio_calculo = time.time()
        n = 2**n
        fin_calculo = time.time()
        tiempo_calculo = fin_calculo - inicio_calculo
        print(f"Tiempo de cálculo de 2**n: {tiempo_calculo:.4f} segundos")
        archivo(n)
except ValueError:
    print("Error, ingrese un valor numerico")
finally:
    fin_total = time.time()
    tiempo_total = fin_total - inicio_total
    print(f"Tiempo de ejecución total del programa: {tiempo_total:.4f} segundos")

try: 
    for i in range (15, 25): 
        print (f'se esta creando el archivo {i}...') 
    if i < 0: 
        print("Ingrese un numero positivo.") 
    else: 
        n = 2 ** i 
        archivo(n, 'archivo' + str(i) + '.txt') 
except ValueError: 
    print("solo se permiten numeros.")

                
                