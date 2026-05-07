# Definimos la función y le pasamos una lista de números inventada
def ordenar_mayor_a_menor(numeros):
    
    # Primero sacamos cuántos números hay en la lista
    cantidad = len(numeros)
    
    # Necesitamos un bucle que dé tantas vueltas como números haya
    for i in range(cantidad):
        
        # Dentro, necesitamos otro bucle que vaya comparando de dos en dos.
        # Le restamos 'i' y 1 para no pasarnos del límite de la lista
        # y no volver a mirar los que ya están ordenados al final.
        for j in range(0, cantidad - i - 1):
            
            # Aquí viene la magia: Si el número actual es MENOR que el siguiente...
            if numeros[j] < numeros[j + 1]:
                
                # ...los intercambiamos de posición usando una variable temporal
                # para no perder el dato mientras hacemos el cambio.
                temporal = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = temporal
                
    # Cuando terminan los bucles, la lista ya está ordenada y la devolvemos
    return numeros

# --- ZONA DE PRUEBAS ---

# Creamos una lista desordenada para probar si funciona
mis_numeros = [4, 1, 9, 3, 7, 2]

# Llamamos a nuestra función, le pasamos la lista y guardamos el resultado
resultado = ordenar_mayor_a_menor(mis_numeros)

# Imprimimos el resultado para comprobar que va del más grande al más pequeño
print("Lista ordenada:", resultado)