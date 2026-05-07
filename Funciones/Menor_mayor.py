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





#MAS ARTESANAL AUN






# 1. NUESTRA FUNCIÓN CASERA PARA CONTAR (Reemplaza a len)
def contar_elementos(lista):
    total = 0
    for elemento in lista:
        total = total + 1
    return total

# 2. NUESTRA FUNCIÓN PARA ORDENAR DE MENOR A MAYOR (Sin usar range ni len)
def ordenar_menor_a_mayor(numeros):
    
    # Usamos nuestra propia función para saber cuántos números hay
    cantidad = contar_elementos(numeros)
    
    # Creamos el contador para el primer bucle
    i = 0
    
    # El bucle principal (mientras 'i' sea menor que la cantidad)
    while i < cantidad:
        
        # Creamos el contador para el segundo bucle que va comparando
        j = 0
        
        # Bucle secundario: restamos 'i' y 1 para no salirnos del límite
        while j < (cantidad - i - 1):
            
            # ¡AQUÍ ESTÁ EL CAMBIO CLAVE!
            # Si el número actual es MAYOR que el que tiene a su derecha...
            if numeros[j] > numeros[j + 1]:
                
                # ...los intercambiamos usando nuestra variable temporal.
                # Así, los números más grandes se van yendo hacia el final.
                temporal = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = temporal
                
            # ¡CRÍTICO! Sumamos 1 a 'j' a mano para que el bucle avance
            j = j + 1
            
        # ¡CRÍTICO! Sumamos 1 a 'i' a mano antes de la siguiente vuelta
        i = i + 1
        
    # Devolvemos la lista ya ordenada
    return numeros

# --- ZONA DE PRUEBAS ---

# Nuestra lista desordenada
mis_numeros = [4, 1, 9, 3, 7, 2]

# Llamamos a la función
resultado = ordenar_menor_a_mayor(mis_numeros)

# Imprimimos el resultado para comprobar que va del más pequeño al más grande
print("Lista ordenada de menor a mayor nivel artesano:", resultado)