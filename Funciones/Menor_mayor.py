# Definimos la función
def ordenar_menor_a_mayor(numeros):
    
    # Sacamos la cantidad de números
    cantidad = len(numeros)
    
    # El bucle principal
    for i in range(cantidad):
        
        # El bucle que va comparando de dos en dos
        for j in range(0, cantidad - i - 1):
            
            # ¡AQUÍ ESTÁ EL CAMBIO CLAVE!
            # Si el número actual es MAYOR que el que tiene a su derecha...
            if numeros[j] > numeros[j + 1]:
                
                # ...los intercambiamos usando nuestra variable temporal.
                # Así, los números más grandes se van yendo hacia el final.
                temporal = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = temporal
                
    # Devolvemos la lista ya ordenada
    return numeros

# --- ZONA DE PRUEBAS ---

# Nuestra lista desordenada
mis_numeros = [4, 1, 9, 3, 7, 2]

# Llamamos a la función
resultado = ordenar_menor_a_mayor(mis_numeros)

# Imprimimos el resultado para comprobar que va del más pequeño al más grande
print("Lista ordenada de menor a mayor:", resultado)